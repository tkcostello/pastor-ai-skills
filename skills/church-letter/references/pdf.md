# Letter PDF

Only when the pastor asks for a PDF or a printed letterhead copy. Needs `pip install reportlab`.

Write the letter to a JSON file, then run the script in this skill's folder:

```bash
python generate-pdf.py letter.json             # file named from the date and topic
python generate-pdf.py letter.json letter.pdf  # explicit output path
```

Delete the JSON afterward and tell the pastor where the PDF saved.

```json
{
  "church_name": "From the profile",
  "date": "April 14, 2026",
  "topic": "Leadership Transition",
  "addressee": "Dear New Hope Family,",
  "body": "Full letter text. Separate paragraphs with \n\n.",
  "pastor_name": "From the profile",
  "pastor_title": "From the profile",
  "framing_note": "One sentence on what the letter communicates.",
  "flags": ["Anything needing legal review or pastoral follow-up."]
}
```

- `framing_note` and `flags` stay out of the PDF; they're for the pastor.
- The PDF has the church name as a centered letterhead, the dated and addressed body, and a signature block with the pastor's name, title and church.
