# Sermon Research PDF

Only when the pastor asks for a PDF or a printable copy. Needs `pip install reportlab`.

Write the research to a JSON file, then run the script in this skill's folder:

```bash
python generate-pdf.py research.json               # file named from the passage
python generate-pdf.py research.json research.pdf  # explicit output path
```

Delete the JSON afterward and tell the pastor where the PDF saved.

```json
{
  "passage": "Romans 8:1-11",
  "date": "2026-04-08",
  "pastor_name": "From the profile",
  "church_name": "From the profile",
  "passage_context": "Step 1 text. Separate paragraphs with \n\n.",
  "historical_background": "Step 2 text. Separate paragraphs with \n\n.",
  "word_studies": [
    {
      "english": "condemnation",
      "transliteration": "katakrima",
      "literal_meaning": "adverse sentence, punishment following a guilty verdict",
      "range_of_meaning": "Used 3 times in the NT, all in Romans. Refers to the sentence itself, not the act of judging.",
      "translations": {
        "NIV": "condemnation",
        "ESV": "condemnation",
        "KJV": "condemnation",
        "NLT": "condemnation",
        "NASB": "condemnation"
      }
    }
  ],
  "commentary_insights": "Step 4 text. Separate paragraphs with \n\n.",
  "cross_references": [
    {
      "reference": "Galatians 5:16-25",
      "connection": "Paul's parallel treatment of life in the Spirit versus life in the flesh.",
      "type": "Thematic connection"
    }
  ],
  "theological_themes": [
    {
      "name": "Freedom from condemnation",
      "in_text": "Opens with the declaration that there is now no condemnation for those in Christ Jesus.",
      "implication": "For people carrying guilt from past failures, this is the ground they stand on."
    }
  ],
  "thinking_prompts": [
    "What assumption might your congregation bring to this text that the original audience would not have had?"
  ]
}
```

`word_studies` holds 3-5 entries, `cross_references` 5-8 (type is "Direct parallel", "Thematic connection" or "OT background"), `theological_themes` 3-5, and `thinking_prompts` 5-7 strings.
