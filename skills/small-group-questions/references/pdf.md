# Small Group Guide PDF

Only when the pastor asks for a PDF or a printable copy. Needs `pip install reportlab`.

Write the guide to a JSON file, then run the script in this skill's folder:

```bash
python generate-pdf.py guide.json            # file named from the passage
python generate-pdf.py guide.json guide.pdf  # explicit output path
```

Delete the JSON afterward and tell the pastor where the PDF saved.

```json
{
  "passage": "Romans 8:1-11",
  "date": "April 13, 2026",
  "translation": "ESV",
  "pastor_name": "From the profile",
  "church_name": "From the profile",
  "big_idea": "One sentence distilled from the sermon.",
  "icebreakers": ["Option A", "Option B"],
  "observation_questions": ["Q1", "Q2"],
  "interpretation_questions": ["Q3", "Q4", "Q5"],
  "application_questions": ["Q6", "Q7", "Q8"],
  "going_deeper_questions": ["Q9", "Q10"],
  "prayer_prompt": "Specific prayer direction.",
  "optional_challenge": "One concrete action step."
}
```

`icebreakers` has 2 entries. The question arrays follow the guide: 2 observation, 3 interpretation, up to 3 application, 2 going deeper.
