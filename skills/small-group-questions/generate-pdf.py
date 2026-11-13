#!/usr/bin/env python3
"""Small Group Discussion Guide PDF Generator"""

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
    build_styles, section_header, add_title_banner,
    make_page_footer, create_doc,
    add_shaded_box, add_bullet_list,
)
from reportlab.platypus import Paragraph, Spacer


def add_numbered_questions(story, questions, styles, start_num=1):
    for i, q in enumerate(questions, start_num):
        story.append(Paragraph(f"<b>{i}.</b>  {q}", styles["body"]))
    return start_num + len(questions)


def generate_pdf(json_path, output_path=None):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not output_path:
        passage = data.get("passage", "guide")
        safe_name = passage.replace(":", "-").replace(" ", "-")
        output_path = f"Small-Group-Guide-{safe_name}.pdf"

    doc = create_doc(
        output_path,
        title=f"Small Group Guide: {data.get('passage', '')}",
        author=data.get("pastor_name", ""),
    )
    styles = build_styles()
    story = []

    meta_parts = [p for p in [data.get("date"), data.get("pastor_name"), data.get("church_name")] if p]
    add_title_banner(story, "SMALL GROUP DISCUSSION GUIDE", data.get("passage", ""), meta_parts, styles)

    if data.get("big_idea"):
        section_header(story, "Big Idea", styles)
        big_idea_elements = [Paragraph(f"<b>{data['big_idea']}</b>", styles["body_content"])]
        add_shaded_box(story, big_idea_elements, styles)
        story.append(Spacer(1, 12))

    if data.get("icebreakers"):
        section_header(story, "Icebreaker (leader picks one)", styles)
        add_bullet_list(story, data["icebreakers"], styles)

    translation = data.get("translation", "NIV")
    section_header(story, "Read the Passage Together", styles)
    story.append(Paragraph(f"{data.get('passage', '')} ({translation})", styles["body"]))

    num = 1
    if data.get("observation_questions"):
        section_header(story, "Observation Questions", styles)
        num = add_numbered_questions(story, data["observation_questions"], styles, num)

    if data.get("interpretation_questions"):
        section_header(story, "Interpretation Questions", styles)
        num = add_numbered_questions(story, data["interpretation_questions"], styles, num)

    if data.get("application_questions"):
        section_header(story, "Application Questions", styles)
        num = add_numbered_questions(story, data["application_questions"], styles, num)

    if data.get("going_deeper_questions"):
        section_header(story, "Going Deeper", styles)
        num = add_numbered_questions(story, data["going_deeper_questions"], styles, num)

    section_header(story, "Closing", styles)
    if data.get("prayer_prompt"):
        story.append(Paragraph("PRAYER PROMPT", styles["body_label"]))
        prayer_elements = [Paragraph(data["prayer_prompt"], styles["prompt"])]
        add_shaded_box(story, prayer_elements, styles)
        story.append(Spacer(1, 8))

    if data.get("optional_challenge"):
        story.append(Paragraph("OPTIONAL CHALLENGE", styles["body_label"]))
        story.append(Paragraph(data["optional_challenge"], styles["body_content"]))

    page_footer = make_page_footer(data.get("church_name", ""))
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
