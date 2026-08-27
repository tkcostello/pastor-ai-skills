#!/usr/bin/env python3
"""
Sermon Research PDF Generator
Converts structured sermon research JSON into a formatted PDF document.

Usage: python generate-pdf.py <input.json> [output.pdf]

Required: pip install reportlab
"""

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
    NAVY, GOLD, SLATE, LIGHT_BG, RULE_GRAY, WHITE,
    build_styles, section_header, add_section, add_title_banner,
    add_reachright_footer, make_page_footer, create_doc, add_shaded_box,
)
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle
from reportlab.lib.units import inch


# --- Sermon-specific layout functions ---


def add_word_studies(story, word_studies, styles):
    """Add the word study table with refined styling."""
    section_header(story, "Key Word Study", styles)

    if not word_studies:
        story.append(Paragraph("No word studies provided.", styles["body"]))
        return

    headers = [
        "English", "Transliteration",
        "Literal Meaning", "Range of Meaning", "Translations"
    ]

    header_row = [Paragraph(h, styles["table_header"]) for h in headers]
    table_data = [header_row]

    for ws in word_studies:
        translations = ws.get("translations", {})
        trans_parts = []
        for k, v in translations.items():
            trans_parts.append(f"<b>{k}</b>: {v}")
        trans_text = ", ".join(trans_parts) if trans_parts else ""

        row = [
            Paragraph(ws.get("english", ""), styles["table_cell_bold"]),
            Paragraph(ws.get("transliteration", ""), styles["table_cell"]),
            Paragraph(ws.get("literal_meaning", ""), styles["table_cell"]),
            Paragraph(ws.get("range_of_meaning", ""), styles["table_cell"]),
            Paragraph(trans_text, styles["table_cell"]),
        ]
        table_data.append(row)

    col_widths = [0.9 * inch, 0.95 * inch, 1.0 * inch, 1.8 * inch, 1.85 * inch]

    table = Table(table_data, colWidths=col_widths, repeatRows=1)

    style_commands = [
        # Header row
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("TOPPADDING", (0, 0), (-1, 0), 10),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
        # Gold line below header
        ("LINEBELOW", (0, 0), (-1, 0), 2, GOLD),
        # All cells
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 1), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 8),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        # Subtle grid
        ("GRID", (0, 0), (-1, 0), 0, WHITE),
        ("LINEBELOW", (0, 1), (-1, -1), 0.5, RULE_GRAY),
        ("LINEBEFORE", (1, 1), (-1, -1), 0.5, RULE_GRAY),
    ]

    # Alternating row backgrounds
    for i in range(1, len(table_data)):
        if i % 2 == 0:
            style_commands.append(("BACKGROUND", (0, i), (-1, i), LIGHT_BG))

    table.setStyle(TableStyle(style_commands))
    story.append(table)
    story.append(Spacer(1, 16))


def add_cross_references(story, cross_refs, styles):
    """Add cross-references as a formatted bullet list."""
    section_header(story, "Cross-References and Parallel Passages", styles)

    if not cross_refs:
        story.append(Paragraph("No cross-references provided.", styles["body"]))
        return

    for ref in cross_refs:
        reference = ref.get("reference", "")
        connection = ref.get("connection", "")
        conn_type = ref.get("type", "")

        type_label = f'  <font color="#{SLATE.hexval()[2:]}">[{conn_type}]</font>' if conn_type else ""
        text = f"<b>{reference}</b>{type_label}:  {connection}"
        story.append(Paragraph(text, styles["bullet"], bulletText="\u2022"))


def add_theological_themes(story, themes, styles):
    """Add theological themes with structured sub-sections."""
    section_header(story, "Theological Themes", styles)

    if not themes:
        story.append(Paragraph("No themes provided.", styles["body"]))
        return

    from reportlab.platypus import HRFlowable

    for theme in themes:
        name = theme.get("name", "")
        in_text = theme.get("in_text", "")
        implication = theme.get("implication", "")

        # Theme name with gold underline
        story.append(Paragraph(name, styles["body_bold"]))
        story.append(HRFlowable(
            width="30%", thickness=1.5, color=GOLD,
            spaceBefore=0, spaceAfter=8
        ))

        if in_text:
            story.append(Paragraph("IN THE TEXT", styles["body_label"]))
            story.append(Paragraph(in_text, styles["body_content"]))

        if implication:
            story.append(Paragraph("FOR YOUR CONGREGATION", styles["body_label"]))
            story.append(Paragraph(implication, styles["body_content"]))

        story.append(Spacer(1, 8))


def add_thinking_prompts(story, prompts, styles):
    """Add thinking prompts inside a shaded container with gold left border."""
    section_header(story, "Thinking Prompts", styles)

    if not prompts:
        story.append(Paragraph("No prompts provided.", styles["body"]))
        return

    # Build prompt paragraphs
    prompt_elements = []
    for i, prompt in enumerate(prompts, 1):
        prompt_elements.append(
            Paragraph(f"<b>{i}.</b>  {prompt}", styles["prompt"])
        )

    add_shaded_box(story, prompt_elements, styles)


# --- Main Generator ---

def generate_pdf(json_path, output_path=None):
    """Generate a formatted PDF from sermon research JSON data."""

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not output_path:
        passage = data.get("passage", "research")
        safe_name = passage.replace(":", "-").replace(" ", "-")
        output_path = f"Sermon-Research-{safe_name}.pdf"

    doc = create_doc(
        output_path,
        title=f"Sermon Research: {data.get('passage', '')}",
        author=data.get("pastor_name", ""),
    )

    styles = build_styles()
    story = []

    # Title banner
    meta_parts = []
    if data.get("date"):
        meta_parts.append(data["date"])
    if data.get("pastor_name"):
        meta_parts.append(data["pastor_name"])
    if data.get("church_name"):
        meta_parts.append(data["church_name"])

    add_title_banner(story, "SERMON RESEARCH", data.get("passage", ""), meta_parts, styles)

    # Sections
    if data.get("passage_context"):
        add_section(story, "Passage Context", data["passage_context"], styles)

    if data.get("historical_background"):
        add_section(
            story, "Historical and Cultural Background",
            data["historical_background"], styles
        )

    if data.get("word_studies"):
        add_word_studies(story, data["word_studies"], styles)

    if data.get("commentary_insights"):
        add_section(
            story, "Commentary Insights",
            data["commentary_insights"], styles
        )

    if data.get("cross_references"):
        add_cross_references(story, data["cross_references"], styles)

    if data.get("theological_themes"):
        add_theological_themes(story, data["theological_themes"], styles)

    if data.get("thinking_prompts"):
        add_thinking_prompts(story, data["thinking_prompts"], styles)

    # REACHRIGHT branding
    add_reachright_footer(story, styles)

    page_footer = make_page_footer("reachright")
    doc.build(story, onFirstPage=page_footer, onLaterPages=page_footer)

    return os.path.abspath(output_path)


# --- CLI Entry ---

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate-pdf.py <input.json> [output.pdf]")
        sys.exit(1)

    json_input = sys.argv[1]
    pdf_output = sys.argv[2] if len(sys.argv) > 2 else None

    result_path = generate_pdf(json_input, pdf_output)
    print(f"PDF generated: {result_path}")
