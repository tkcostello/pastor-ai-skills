#!/usr/bin/env python3
"""Midweek Devotional PDF Generator"""

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
    NAVY, GOLD, BODY_COLOR, SLATE, MED_GRAY,
    build_styles, make_page_footer, create_doc, add_shaded_box,
)
from reportlab.platypus import Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY


def build_devotional_styles(base_styles):
    s = dict(base_styles)
    s["devo_header"] = ParagraphStyle(
        "DevoHeader", fontName="Helvetica", fontSize=10, leading=14,
        textColor=MED_GRAY, alignment=TA_CENTER, spaceAfter=2,
    )
    s["devo_date"] = ParagraphStyle(
        "DevoDate", fontName="Helvetica", fontSize=9, leading=13,
        textColor=MED_GRAY, alignment=TA_CENTER, spaceAfter=20,
    )
    s["devo_body"] = ParagraphStyle(
        "DevoBody", fontName="Times-Roman", fontSize=11.5, leading=18,
        textColor=BODY_COLOR, spaceAfter=12, alignment=TA_JUSTIFY,
    )
    s["devo_scripture"] = ParagraphStyle(
        "DevoScripture", fontName="Times-Italic", fontSize=11, leading=17,
        textColor=BODY_COLOR, spaceAfter=4,
    )
    s["devo_reference"] = ParagraphStyle(
        "DevoReference", fontName="Helvetica-Bold", fontSize=9, leading=13,
        textColor=NAVY, spaceAfter=0,
    )
    s["devo_takeaway"] = ParagraphStyle(
        "DevoTakeaway", fontName="Helvetica-Bold", fontSize=11.5, leading=18,
        textColor=NAVY, spaceAfter=16, alignment=TA_CENTER,
    )
    s["devo_closing"] = ParagraphStyle(
        "DevoClosing", fontName="Times-Italic", fontSize=11, leading=17,
        textColor=SLATE, spaceAfter=12, alignment=TA_JUSTIFY,
    )
    s["devo_signoff"] = ParagraphStyle(
        "DevoSignoff", fontName="Helvetica", fontSize=10, leading=14,
        textColor=BODY_COLOR, spaceBefore=20,
    )
    return s


def generate_pdf(json_path, output_path=None):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not output_path:
        date = data.get("date", "devotional")
        safe_name = date.replace("/", "-").replace(" ", "-").replace(",", "")
        output_path = f"Midweek-Devotional-{safe_name}.pdf"

    doc = create_doc(
        output_path,
        title=f"Midweek Devotional: {data.get('date', '')}",
        author=data.get("pastor_name", ""),
    )
    base_styles = build_styles()
    styles = build_devotional_styles(base_styles)
    story = []

    # Header
    story.append(Paragraph(data.get("church_name", ""), styles["devo_header"]))
    story.append(Paragraph(data.get("date", ""), styles["devo_date"]))
    story.append(HRFlowable(width="30%", thickness=1.5, color=GOLD, spaceBefore=0, spaceAfter=24))

    # Opening
    if data.get("opening"):
        story.append(Paragraph(data["opening"], styles["devo_body"]))

    # Scripture callout
    if data.get("scripture_text"):
        scripture_elements = []
        scripture_elements.append(Paragraph(data["scripture_text"], styles["devo_scripture"]))
        ref_line = data.get("passage_reference", "")
        if data.get("translation"):
            ref_line += f" ({data['translation']})"
        scripture_elements.append(Paragraph(ref_line, styles["devo_reference"]))
        add_shaded_box(story, scripture_elements, styles)
        story.append(Spacer(1, 16))

    # Reflection
    if data.get("reflection"):
        for p in data["reflection"].split("\n\n"):
            p = p.strip()
            if p:
                story.append(Paragraph(p, styles["devo_body"]))

    # Takeaway
    if data.get("takeaway"):
        story.append(Spacer(1, 8))
        story.append(Paragraph(data["takeaway"], styles["devo_takeaway"]))

    # Closing
    if data.get("closing"):
        story.append(Paragraph(data["closing"], styles["devo_closing"]))

    # Pastor name
    if data.get("pastor_name"):
        story.append(Paragraph(data["pastor_name"], styles["devo_signoff"]))

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
