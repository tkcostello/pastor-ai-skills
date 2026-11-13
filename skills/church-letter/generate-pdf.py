#!/usr/bin/env python3
"""Church Letter PDF Generator"""

import json
import sys
import os

_here = os.path.dirname(os.path.abspath(__file__))


def _load_pdf_utils():
    """Load pdf_utils.py by file path, without touching sys.path.

    Looks next to this script first (a flat copy of one skill folder), then
    $CLAUDE_PLUGIN_ROOT/shared (plugin install), then parent folders for a
    shared/ directory (a full clone). Exits with a plain message if reportlab
    or pdf_utils.py is missing.
    """
    import importlib.util
    try:
        import reportlab  # noqa: F401
    except ImportError:
        sys.exit("PDF output needs the reportlab package. Run: pip install reportlab")
    roots = [_here, os.environ.get("CLAUDE_PLUGIN_ROOT", "")]
    d = _here
    for _ in range(4):
        d = os.path.dirname(d)
        roots.append(d)
    for root in filter(None, roots):
        for path in (os.path.join(root, "pdf_utils.py"),
                     os.path.join(root, "shared", "pdf_utils.py")):
            if os.path.isfile(path):
                spec = importlib.util.spec_from_file_location("pdf_utils", path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                sys.modules["pdf_utils"] = module
                return
    sys.exit("Could not find pdf_utils.py. Copy shared/pdf_utils.py from "
             "github.com/tkcostello/pastor-ai-skills into this skill's folder.")


_load_pdf_utils()

from pdf_utils import (
    NAVY, GOLD, BODY_COLOR,
    build_styles, make_page_footer, create_doc,
)
from reportlab.platypus import Paragraph, HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_JUSTIFY


def build_letter_styles(base_styles):
    s = dict(base_styles)
    s["letterhead"] = ParagraphStyle(
        "Letterhead", fontName="Helvetica-Bold", fontSize=18, leading=22,
        textColor=NAVY, alignment=TA_CENTER, spaceAfter=4,
    )
    s["date_line"] = ParagraphStyle(
        "DateLine", fontName="Helvetica", fontSize=10, leading=14,
        textColor=BODY_COLOR, alignment=TA_RIGHT, spaceAfter=20,
    )
    s["addressee"] = ParagraphStyle(
        "Addressee", fontName="Helvetica", fontSize=11, leading=16,
        textColor=BODY_COLOR, spaceAfter=16,
    )
    s["letter_body"] = ParagraphStyle(
        "LetterBody", fontName="Times-Roman", fontSize=11, leading=17,
        textColor=BODY_COLOR, spaceAfter=12, alignment=TA_JUSTIFY,
    )
    s["signature_name"] = ParagraphStyle(
        "SignatureName", fontName="Helvetica-Bold", fontSize=11, leading=16,
        textColor=NAVY, spaceBefore=28,
    )
    s["signature_title"] = ParagraphStyle(
        "SignatureTitle", fontName="Helvetica", fontSize=10, leading=14,
        textColor=BODY_COLOR,
    )
    return s


def generate_pdf(json_path, output_path=None):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not output_path:
        date = data.get("date", "letter")
        topic = data.get("topic", "")
        safe_date = date.replace("/", "-").replace(" ", "-").replace(",", "")
        safe_topic = topic.replace(" ", "-")[:30] if topic else "letter"
        output_path = f"Church-Letter-{safe_date}-{safe_topic}.pdf"

    doc = create_doc(
        output_path,
        title=f"Church Letter: {data.get('date', '')}",
        author=data.get("pastor_name", ""),
    )
    base_styles = build_styles()
    styles = build_letter_styles(base_styles)
    story = []

    # Letterhead
    story.append(Paragraph(data.get("church_name", ""), styles["letterhead"]))
    story.append(HRFlowable(width="40%", thickness=2, color=GOLD, spaceBefore=2, spaceAfter=20))

    # Date
    if data.get("date"):
        story.append(Paragraph(data["date"], styles["date_line"]))

    # Addressee
    if data.get("addressee"):
        story.append(Paragraph(data["addressee"], styles["addressee"]))

    # Body
    body = data.get("body", "")
    for p in body.split("\n\n"):
        p = p.strip()
        if p:
            story.append(Paragraph(p, styles["letter_body"]))

    # Signature
    if data.get("pastor_name"):
        story.append(Paragraph(data["pastor_name"], styles["signature_name"]))
    if data.get("pastor_title"):
        story.append(Paragraph(data["pastor_title"], styles["signature_title"]))
    if data.get("church_name"):
        story.append(Paragraph(data["church_name"], styles["signature_title"]))

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
