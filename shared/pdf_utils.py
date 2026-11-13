#!/usr/bin/env python3
"""
Shared PDF Utility Library for Pastor AI Skills
Reusable components for generating branded PDF documents.

Required: pip install reportlab
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable
)


# --- Color Palette ---
# Editorial study-bible aesthetic: deep navy + warm gold accent

NAVY = HexColor("#1B2A4A")
GOLD = HexColor("#B8860B")
GOLD_LIGHT = HexColor("#D4A843")
BODY_COLOR = HexColor("#2D3436")
SLATE = HexColor("#4A5568")
MED_GRAY = HexColor("#A0AEC0")
LIGHT_BG = HexColor("#F8F6F1")
RULE_GRAY = HexColor("#D1CDC4")
WHITE = HexColor("#FFFFFF")

# Content width: letter (8.5") minus 1" margins each side = 6.5"
CONTENT_WIDTH = 6.5 * inch


# --- Styles ---

def build_styles():
    """Create custom paragraph styles for the document."""
    s = {}

    # --- Title banner styles (white on navy) ---
    s["title"] = ParagraphStyle(
        "Title", fontName="Helvetica-Bold", fontSize=28, leading=34,
        textColor=WHITE, spaceAfter=2,
    )
    s["passage"] = ParagraphStyle(
        "Passage", fontName="Helvetica", fontSize=16, leading=22,
        textColor=HexColor("#C8D6E5"), spaceAfter=6,
    )
    s["meta"] = ParagraphStyle(
        "Meta", fontName="Helvetica", fontSize=9, leading=13,
        textColor=HexColor("#8899AA"),
    )

    # --- Section headers ---
    s["section_header"] = ParagraphStyle(
        "SectionHeader", fontName="Helvetica-Bold", fontSize=14, leading=18,
        textColor=NAVY, spaceBefore=24, spaceAfter=2,
    )

    # --- Body ---
    s["body"] = ParagraphStyle(
        "Body", fontName="Times-Roman", fontSize=11, leading=16,
        textColor=BODY_COLOR, spaceAfter=10, alignment=TA_JUSTIFY,
    )
    s["body_bold"] = ParagraphStyle(
        "BodyBold", fontName="Helvetica-Bold", fontSize=11, leading=16,
        textColor=NAVY, spaceAfter=4,
    )
    s["body_label"] = ParagraphStyle(
        "BodyLabel", fontName="Helvetica-Bold", fontSize=9.5, leading=14,
        textColor=GOLD, spaceAfter=2,
    )
    s["body_content"] = ParagraphStyle(
        "BodyContent", fontName="Times-Roman", fontSize=11, leading=16,
        textColor=BODY_COLOR, spaceAfter=8, leftIndent=0,
        alignment=TA_JUSTIFY,
    )

    # --- Bullets ---
    s["bullet"] = ParagraphStyle(
        "Bullet", fontName="Times-Roman", fontSize=11, leading=16,
        textColor=BODY_COLOR, leftIndent=18, spaceAfter=8,
        bulletIndent=4, bulletFontName="Helvetica-Bold",
        bulletFontSize=9, bulletColor=GOLD,
    )

    # --- Thinking prompts (inside shaded box) ---
    s["prompt"] = ParagraphStyle(
        "Prompt", fontName="Times-Italic", fontSize=10.5, leading=15,
        textColor=SLATE, spaceAfter=6, leftIndent=0,
    )

    # --- Table styles ---
    s["table_header"] = ParagraphStyle(
        "TableHeader", fontName="Helvetica-Bold", fontSize=8.5,
        leading=11, textColor=WHITE,
    )
    s["table_cell"] = ParagraphStyle(
        "TableCell", fontName="Helvetica", fontSize=8.5,
        leading=12, textColor=BODY_COLOR,
    )
    s["table_cell_bold"] = ParagraphStyle(
        "TableCellBold", fontName="Helvetica-Bold", fontSize=8.5,
        leading=12, textColor=NAVY,
    )

    return s


# --- Helper: Section header with gold accent ---

def section_header(story, title, styles):
    """Add a section header with gold accent underline."""
    story.append(Paragraph(title, styles["section_header"]))
    story.append(HRFlowable(
        width="100%", thickness=2, color=GOLD,
        spaceBefore=2, spaceAfter=14
    ))


# --- Text Section ---

def add_section(story, title, content, styles):
    """Add a text section with header and body paragraphs."""
    section_header(story, title, styles)

    if isinstance(content, str):
        for p in content.split("\n\n"):
            p = p.strip()
            if p:
                story.append(Paragraph(p, styles["body"]))
    elif isinstance(content, list):
        for item in content:
            story.append(Paragraph(item, styles["body"]))


# --- Bullet List ---

def add_bullet_list(story, items, styles):
    """Add a list of strings as gold-bulleted paragraphs."""
    for item in items:
        story.append(Paragraph(item, styles["bullet"], bulletText="\u2022"))


# --- Generic Table ---

def add_table(story, headers, rows, col_widths, styles):
    """Add a styled table with navy header, gold accent, and alternating rows.

    Args:
        story: The PDF story list to append to.
        headers: List of header strings.
        rows: List of lists of strings.
        col_widths: List of floats in inches (converted to points inside).
        styles: Dict of ParagraphStyles from build_styles().
    """
    col_widths_pts = [w * inch for w in col_widths]

    header_row = [Paragraph(h, styles["table_header"]) for h in headers]
    table_data = [header_row]

    for row in rows:
        table_data.append([Paragraph(cell, styles["table_cell"]) for cell in row])

    table = Table(table_data, colWidths=col_widths_pts, repeatRows=1)

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


# --- Shaded Box (gold left border + cream background) ---

def add_shaded_box(story, elements, styles):
    """Add content inside a gold-left-border + cream background container.

    Args:
        story: The PDF story list to append to.
        elements: List of Paragraph/Spacer flowables to place inside the box.
        styles: Dict of ParagraphStyles from build_styles().
    """
    gold_bar_width = 4
    content_col_width = CONTENT_WIDTH - gold_bar_width - 2

    box = Table(
        [[None, elements]],
        colWidths=[gold_bar_width, content_col_width],
    )
    box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), GOLD),
        ("BACKGROUND", (1, 0), (1, -1), LIGHT_BG),
        ("LEFTPADDING", (0, 0), (0, -1), 0),
        ("RIGHTPADDING", (0, 0), (0, -1), 0),
        ("TOPPADDING", (0, 0), (0, -1), 0),
        ("BOTTOMPADDING", (0, 0), (0, -1), 0),
        ("LEFTPADDING", (1, 0), (1, -1), 16),
        ("RIGHTPADDING", (1, 0), (1, -1), 16),
        ("TOPPADDING", (1, 0), (1, -1), 14),
        ("BOTTOMPADDING", (1, 0), (1, -1), 14),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(box)


# --- Title Banner (generalized) ---

def add_title_banner(story, title_text, subtitle_text, meta_parts, styles):
    """Add a full-width navy banner with title, subtitle, and meta line.

    Args:
        story: The PDF story list to append to.
        title_text: Main title, e.g. "SERMON RESEARCH".
        subtitle_text: Subtitle line, e.g. "Romans 8:1-11".
        meta_parts: List of strings joined with " | ", e.g. ["Apr 8, 2026", "Pastor Name"].
        styles: Dict of ParagraphStyles from build_styles().
    """
    banner_content = []
    banner_content.append(Paragraph(title_text, styles["title"]))
    if subtitle_text:
        banner_content.append(Paragraph(subtitle_text, styles["passage"]))
    if meta_parts:
        banner_content.append(Spacer(1, 4))
        banner_content.append(
            Paragraph("  |  ".join(meta_parts), styles["meta"])
        )

    # Wrap in a table cell for navy background
    banner = Table(
        [[banner_content]],
        colWidths=[CONTENT_WIDTH],
    )
    banner.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("LEFTPADDING", (0, 0), (-1, -1), 24),
        ("RIGHTPADDING", (0, 0), (-1, -1), 24),
        ("TOPPADDING", (0, 0), (-1, -1), 24),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 20),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    story.append(banner)

    # Gold accent line below banner
    story.append(HRFlowable(
        width="100%", thickness=3, color=GOLD,
        spaceBefore=0, spaceAfter=24
    ))


# --- Page Footer (canvas callback factory) ---

def make_page_footer(label=""):
    """Return a canvas callback that draws a thin rule, an optional label
    (usually the church name) on the left, and the page number on the right."""
    def _footer(canvas_obj, doc):
        canvas_obj.saveState()
        page_width = letter[0]
        margin = 1.0 * inch
        canvas_obj.setStrokeColor(RULE_GRAY)
        canvas_obj.setLineWidth(0.5)
        canvas_obj.line(margin, 0.6 * inch, page_width - margin, 0.6 * inch)
        canvas_obj.setFont("Helvetica", 7)
        canvas_obj.setFillColor(MED_GRAY)
        if label:
            canvas_obj.drawString(margin, 0.42 * inch, label)
        canvas_obj.drawRightString(
            page_width - margin, 0.42 * inch, f"Page {canvas_obj.getPageNumber()}"
        )
        canvas_obj.restoreState()

    return _footer


# --- Document Creation ---

def create_doc(output_path, title="", author=""):
    """Create and return a SimpleDocTemplate with standard layout.

    Letter size, 1" side margins, 0.85" top/bottom margins.

    Args:
        output_path: File path for the PDF.
        title: PDF metadata title.
        author: PDF metadata author.

    Returns:
        A SimpleDocTemplate instance.
    """
    return SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=1.0 * inch,
        rightMargin=1.0 * inch,
        topMargin=0.85 * inch,
        bottomMargin=0.85 * inch,
        title=title,
        author=author,
    )
