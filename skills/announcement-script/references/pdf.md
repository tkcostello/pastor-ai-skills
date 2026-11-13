# Announcement Script PDF

Only when the pastor asks for a PDF or a printable copy. Needs `pip install reportlab`.

Write the script to a JSON file, then run the script in this skill's folder:

```bash
python generate-pdf.py announcements.json                    # file named from the date
python generate-pdf.py announcements.json announcements.pdf  # explicit output path
```

Delete the JSON afterward and tell the pastor where the PDF saved.

```json
{
  "date": "April 20, 2026",
  "estimated_seconds": 75,
  "items_submitted": 7,
  "items_covered": 3,
  "deliverer": "Worship Pastor",
  "tone_notes": "High energy, celebratory. Baptism Sunday.",
  "script_body": "Full script. Use [pause] style cues. Separate paragraphs with \n\n.",
  "bumped_items": [
    {"item": "Youth group schedule change", "summary": "Friday moved to Saturday this week only."}
  ]
}
```

- Bracketed cues in `script_body` print as italic stage directions.
- `bumped_items` lists what didn't make the spoken cut, each with a one-line `summary` of its logistics.
- `deliverer` and `tone_notes` are optional; leave them out and those lines are skipped.

The page is a single sheet for the announcer with a plain page-number footer.
