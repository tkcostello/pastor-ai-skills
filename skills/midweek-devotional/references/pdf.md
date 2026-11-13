# Devotional PDF

Only when the pastor asks for a PDF or a printable copy. Needs `pip install reportlab`.

Write the devotional to a JSON file, then run the script in this skill's folder:

```bash
python generate-pdf.py devotional.json                 # file named from the date
python generate-pdf.py devotional.json devotional.pdf  # explicit output path
```

Delete the JSON afterward and tell the pastor where the PDF saved.

```json
{
  "church_name": "From the profile",
  "date": "April 16, 2026",
  "pastor_name": "From the profile",
  "passage_reference": "Psalm 46:10",
  "translation": "ESV",
  "scripture_text": "Be still, and know that I am God.",
  "opening": "The first lines, before the scripture.",
  "reflection": "The body. Separate paragraphs with \n\n.",
  "takeaway": "The line the reader carries into the week.",
  "closing": "Prayer or blessing."
}
```

The script lays these out as one continuous piece with no section labels. The PDF carries the church's name only, with a plain page-number footer.
