#!/usr/bin/env python3
"""Sermon Series PDF Generator"""

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
    build_styles, section_header, add_section, add_title_banner,
    add_reachright_footer, make_page_footer, create_doc, add_table,
)
from reportlab.platypus import Paragraph


def add_practical_notes(story, notes, styles):
    section_header(story, "Practical Notes", styles)
    if notes.get("duration_check"):
        story.append(Paragraph("DURATION CHECK", styles["body_label"]))
        story.append(Paragraph(notes["duration_check"], styles["body_content"]))
    if notes.get("special_attention"):
        story.append(Paragraph("WEEKS NEEDING SPECIAL ATTENTION", styles["body_label"]))
        story.append(Paragraph(notes["special_attention"], styles["body_content"]))
    if notes.get("launch_recommendation"):
        story.append(Paragraph("SERIES LAUNCH RECOMMENDATION", styles["body_label"]))
        story.append(Paragraph(notes["launch_recommendation"], styles["body_content"]))


def generate_pdf(json_path, output_path=None):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not output_path:
        title = data.get("series_title", "series")
        safe_name = title.replace(" ", "-").replace(":", "-")
        output_path = f"Sermon-Series-{safe_name}.pdf"

    doc = create_doc(
        output_path,
        title=f"Sermon Series: {data.get('series_title', '')}",
        author=data.get("pastor_name", ""),
    )
    styles = build_styles()
    story = []

    meta_parts = [p for p in [data.get("date"), data.get("pastor_name"), data.get("church_name")] if p]
    subtitle = data.get("series_title", "")
    if data.get("series_tagline"):
        subtitle += f" -- {data['series_tagline']}"
    add_title_banner(story, "SERMON SERIES", subtitle, meta_parts, styles)

    if data.get("scope_assessment"):
        add_section(story, "Scope Assessment", data["scope_assessment"], styles)

    if data.get("title_options"):
        section_header(story, "Series Title Options", styles)
        headers = ["Title", "Tagline"]
        rows = [[opt.get("title", ""), opt.get("tagline", "")] for opt in data["title_options"]]
        add_table(story, headers, rows, [2.0, 4.5], styles)

    if data.get("weekly_breakdown"):
        section_header(story, "Weekly Breakdown", styles)
        headers = ["Week", "Sermon Title", "Scripture", "Big Idea", "Connective Thread"]
        rows = []
        for week in data["weekly_breakdown"]:
            rows.append([
                str(week.get("week", "")),
                week.get("sermon_title", ""),
                week.get("passage", ""),
                week.get("big_idea", ""),
                week.get("connective_thread", ""),
            ])
        add_table(story, headers, rows, [0.5, 1.2, 1.0, 1.8, 2.0], styles)

    if data.get("series_arc"):
        add_section(story, "Series Arc", data["series_arc"], styles)

    if data.get("practical_notes"):
        add_practical_notes(story, data["practical_notes"], styles)

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
