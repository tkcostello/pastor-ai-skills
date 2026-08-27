#!/usr/bin/env python3
"""Meeting Agenda PDF Generator"""

import json
import sys
import os

_here = os.path.dirname(os.path.abspath(__file__))


def _find_shared():
    """Locate shared/pdf_utils.py regardless of how the skill was installed."""
    candidates = [_here, os.environ.get("CLAUDE_PLUGIN_ROOT") or ""]
    d = _here
    for _ in range(6):
        d = os.path.dirname(d)
        candidates.append(d)
    for base in candidates:
        if not base:
            continue
        for sub in ("", "shared"):
            cand = os.path.join(base, sub) if sub else base
            if os.path.isfile(os.path.join(cand, "pdf_utils.py")):
                return cand
    return os.path.join(_here, "..", "..", "shared")


sys.path.insert(0, _find_shared())

from pdf_utils import (
    SLATE, RULE_GRAY,
    build_styles, section_header, add_title_banner,
    add_reachright_footer, make_page_footer, create_doc,
    add_bullet_list, add_shaded_box,
)
from reportlab.platypus import Paragraph, Spacer, HRFlowable


def add_time_check(story, time_check, styles):
    allocated = time_check.get("allocated", "")
    available = time_check.get("available", "")
    text = f"<b>{allocated} minutes allocated</b>  /  {available} minutes available"
    elements = [Paragraph(text, styles["body_content"])]
    add_shaded_box(story, elements, styles)
    story.append(Spacer(1, 16))


def add_agenda_item(story, item, styles):
    title = item.get("title", "")
    minutes = item.get("minutes", "")
    purpose = item.get("purpose", "")
    lead = item.get("lead", "")

    slate_hex = SLATE.hexval()[2:] if hasattr(SLATE, 'hexval') else "4A5568"
    header_text = f"{title}  <font color=\"#{slate_hex}\">[{purpose}]</font>"
    story.append(Paragraph(header_text, styles["body_bold"]))

    meta_line = f"{minutes} min"
    if lead:
        meta_line += f"  |  Lead: {lead}"
    story.append(Paragraph(meta_line, styles["body_label"]))
    story.append(Spacer(1, 4))

    if item.get("context"):
        story.append(Paragraph(item["context"], styles["body_content"]))

    if item.get("discussion_question"):
        story.append(Paragraph("DISCUSSION QUESTION", styles["body_label"]))
        story.append(Paragraph(item["discussion_question"], styles["body_content"]))

    if item.get("decision_needed") and item["decision_needed"].lower() != "no":
        story.append(Paragraph("DECISION NEEDED", styles["body_label"]))
        detail = item.get("decision_detail", "Yes")
        story.append(Paragraph(detail, styles["body_content"]))

    story.append(HRFlowable(width="100%", thickness=0.5, color=RULE_GRAY, spaceBefore=8, spaceAfter=12))


def generate_pdf(json_path, output_path=None):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not output_path:
        date = data.get("date", "agenda")
        safe_name = date.replace("/", "-").replace(" ", "-").replace(",", "")
        output_path = f"Meeting-Agenda-{safe_name}.pdf"

    meeting_type = data.get("meeting_type", "Meeting")
    doc = create_doc(
        output_path,
        title=f"{meeting_type} Agenda: {data.get('date', '')}",
        author=data.get("pastor_name", ""),
    )
    styles = build_styles()
    story = []

    meta_parts = []
    if data.get("date"):
        meta_parts.append(data["date"])
    time_str = ""
    if data.get("start_time"):
        time_str = data["start_time"]
        if data.get("end_time"):
            time_str += f" - {data['end_time']}"
        if data.get("total_minutes"):
            time_str += f" ({data['total_minutes']} min)"
        meta_parts.append(time_str)
    if data.get("location"):
        meta_parts.append(data["location"])

    add_title_banner(story, f"{meeting_type.upper()} AGENDA", "", meta_parts, styles)

    if data.get("time_check"):
        add_time_check(story, data["time_check"], styles)

    if data.get("opening"):
        opening = data["opening"]
        section_header(story, f"Opening ({opening.get('minutes', 5)} min)", styles)
        if opening.get("prayer_note"):
            story.append(Paragraph(opening["prayer_note"], styles["body"]))
        if opening.get("checkin_question"):
            story.append(Paragraph(f"<b>Check-in:</b> {opening['checkin_question']}", styles["body"]))

    if data.get("agenda_items"):
        for item in data["agenda_items"]:
            add_agenda_item(story, item, styles)

    if data.get("action_items"):
        section_header(story, "Action Items and Next Steps", styles)
        items = []
        for ai in data["action_items"]:
            action = ai.get("action", "")
            owner = ai.get("owner", "")
            deadline = ai.get("deadline", "")
            parts = [f"<b>{action}</b>"]
            if owner:
                parts.append(f"Owner: {owner}")
            if deadline:
                parts.append(f"By: {deadline}")
            items.append("  |  ".join(parts))
        add_bullet_list(story, items, styles)

    if data.get("closing"):
        closing = data["closing"]
        section_header(story, f"Closing ({closing.get('minutes', 2)} min)", styles)
        if closing.get("note"):
            story.append(Paragraph(closing["note"], styles["body"]))

    if data.get("parking_lot"):
        section_header(story, "Parking Lot", styles)
        add_bullet_list(story, data["parking_lot"], styles)

    add_reachright_footer(story, styles)
    page_footer = make_page_footer("reachright")
    doc.build(story, onFirstPage=page_footer, onLaterPages=page_footer)
    return os.path.abspath(output_path)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate-pdf.py <input.json> [output.pdf]")
        sys.exit(1)
    json_input = sys.argv[1]
    pdf_output = sys.argv[2] if len(sys.argv) > 2 else None
    result_path = generate_pdf(json_input, pdf_output)
    print(f"PDF generated: {result_path}")
