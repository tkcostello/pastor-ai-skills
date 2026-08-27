#!/usr/bin/env python3
"""Sermon Brief PDF Generator"""

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
    build_styles, section_header, add_title_banner,
    add_reachright_footer, make_page_footer, create_doc,
    add_bullet_list, add_shaded_box,
)
from reportlab.platypus import Paragraph, Spacer


def add_brief_field(story, label, content, styles):
    if not content:
        return
    story.append(Paragraph(label.upper(), styles["body_label"]))
    story.append(Paragraph(content, styles["body_content"]))


def generate_pdf(json_path, output_path=None):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not output_path:
        passage = data.get("passage", "brief")
        safe_name = passage.replace(":", "-").replace(" ", "-")
        output_path = f"Sermon-Brief-{safe_name}.pdf"

    doc = create_doc(
        output_path,
        title=f"Sermon Brief: {data.get('passage', '')}",
        author=data.get("pastor_name", ""),
    )
    styles = build_styles()
    story = []

    meta_parts = []
    if data.get("series"):
        meta_parts.append(data["series"])
    if data.get("date"):
        meta_parts.append(data["date"])
    if data.get("pastor_name"):
        meta_parts.append(data["pastor_name"])
    if data.get("church_name"):
        meta_parts.append(data["church_name"])
    add_title_banner(story, "SERMON BRIEF", data.get("passage", ""), meta_parts, styles)

    add_brief_field(story, "Big Idea", data.get("big_idea"), styles)
    add_brief_field(story, "Key Tension", data.get("key_tension"), styles)
    add_brief_field(story, "Audience Need", data.get("audience_need"), styles)
    add_brief_field(story, "Desired Response", data.get("desired_response"), styles)
    add_brief_field(story, "The Turn", data.get("the_turn"), styles)

    if data.get("supporting_passages"):
        section_header(story, "Supporting Passages", styles)
        items = []
        for sp in data["supporting_passages"]:
            ref = sp.get("reference", "")
            note = sp.get("note", "")
            items.append(f"<b>{ref}</b>: {note}" if note else f"<b>{ref}</b>")
        add_bullet_list(story, items, styles)

    add_brief_field(story, "One Image or Illustration Idea", data.get("illustration_idea"), styles)

    story.append(Spacer(1, 16))
    closing = [Paragraph(
        "<i>This brief is a launchpad, not a script. Take it to prayer and make it yours.</i>",
        styles["prompt"]
    )]
    add_shaded_box(story, closing, styles)

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
