#!/usr/bin/env python3
"""Announcement Script PDF Generator"""

import json
import re
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
    NAVY, GOLD, BODY_COLOR, SLATE, MED_GRAY,
    build_styles, make_page_footer, create_doc, add_bullet_list,
)
from reportlab.platypus import Paragraph, HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER


def build_script_styles(base_styles):
    s = dict(base_styles)
    s["script_title"] = ParagraphStyle(
        "ScriptTitle", fontName="Helvetica-Bold", fontSize=18, leading=22,
        textColor=NAVY, alignment=TA_CENTER, spaceAfter=4,
    )
    s["script_meta"] = ParagraphStyle(
        "ScriptMeta", fontName="Helvetica", fontSize=9, leading=13,
        textColor=MED_GRAY, alignment=TA_CENTER, spaceAfter=16,
    )
    s["script_body"] = ParagraphStyle(
        "ScriptBody", fontName="Times-Roman", fontSize=12, leading=19,
        textColor=BODY_COLOR, spaceAfter=10,
    )
    s["script_note"] = ParagraphStyle(
        "ScriptNote", fontName="Helvetica-Oblique", fontSize=9.5, leading=14,
        textColor=SLATE, spaceAfter=16,
    )
    s["bumped_header"] = ParagraphStyle(
        "BumpedHeader", fontName="Helvetica-Bold", fontSize=10, leading=14,
        textColor=NAVY, spaceBefore=16, spaceAfter=8,
    )
    return s


def format_script_text(text):
    """Convert [delivery cues] to italic slate-colored inline markup."""
    slate_hex = SLATE.hexval()[2:] if hasattr(SLATE, 'hexval') else "4A5568"
    def replace_cue(match):
        cue = match.group(1)
        return f'<font color="#{slate_hex}"><i>({cue})</i></font>'
    return re.sub(r'\[([^\]]+)\]', replace_cue, text)


def generate_pdf(json_path, output_path=None):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not output_path:
        date = data.get("date", "script")
        safe_name = date.replace("/", "-").replace(" ", "-").replace(",", "")
        output_path = f"Announcement-Script-{safe_name}.pdf"

    doc = create_doc(
        output_path,
        title=f"Announcement Script: {data.get('date', '')}",
        author="",
    )
    base_styles = build_styles()
    styles = build_script_styles(base_styles)
    story = []

    # Header
    story.append(Paragraph("Sunday Announcements", styles["script_title"]))

    meta_parts = []
    if data.get("date"):
        meta_parts.append(data["date"])
    if data.get("estimated_seconds"):
        meta_parts.append(f"~{data['estimated_seconds']} seconds")
    if data.get("items_covered") and data.get("items_submitted"):
        meta_parts.append(f"{data['items_covered']} of {data['items_submitted']} items")
    if meta_parts:
        story.append(Paragraph("  |  ".join(meta_parts), styles["script_meta"]))

    story.append(HRFlowable(width="100%", thickness=2, color=GOLD, spaceBefore=4, spaceAfter=20))

    # Deliverer / tone notes
    if data.get("deliverer") or data.get("tone_notes"):
        note_parts = []
        if data.get("deliverer"):
            note_parts.append(f"Deliverer: {data['deliverer']}")
        if data.get("tone_notes"):
            note_parts.append(data["tone_notes"])
        story.append(Paragraph("  |  ".join(note_parts), styles["script_note"]))

    # Script body
    if data.get("script_body"):
        formatted = format_script_text(data["script_body"])
        for p in formatted.split("\n\n"):
            p = p.strip()
            if p:
                story.append(Paragraph(p, styles["script_body"]))

    # Bumped items
    if data.get("bumped_items"):
        story.append(HRFlowable(width="100%", thickness=0.5, color=MED_GRAY, spaceBefore=20, spaceAfter=8))
        story.append(Paragraph("For the Bulletin / Slides / Email", styles["bumped_header"]))
        items = []
        for bi in data["bumped_items"]:
            item_name = bi.get("item", "")
            summary = bi.get("summary", "")
            items.append(f"<b>{item_name}:</b> {summary}")
        add_bullet_list(story, items, styles)

    page_footer = make_page_footer("church")
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
