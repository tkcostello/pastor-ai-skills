# Sermon Series PDF

Only when the pastor asks for a PDF or a printable copy. Needs `pip install reportlab`.

Write the plan to a JSON file, then run the script in this skill's folder:

```bash
python generate-pdf.py series.json             # file named from the series title
python generate-pdf.py series.json series.pdf  # explicit output path
```

Delete the JSON afterward and tell the pastor where the PDF saved.

```json
{
  "series_title": "Hold Fast",
  "series_tagline": "Staying grounded when everything shifts",
  "date": "2026-04-08",
  "pastor_name": "From the profile",
  "church_name": "From the profile",
  "scope_assessment": "The scope paragraph.",
  "title_options": [
    { "title": "Hold Fast", "tagline": "Staying grounded when everything shifts" }
  ],
  "weekly_breakdown": [
    {
      "week": 1,
      "sermon_title": "The Confidence You Already Have",
      "passage": "Hebrews 10:19-25",
      "big_idea": "You have access to God that nothing can revoke.",
      "connective_thread": "Establishes the premise: we hold fast because of what Christ already did."
    }
  ],
  "series_arc": "The arc summary.",
  "practical_notes": {
    "duration_check": "Duration note.",
    "special_attention": "Weeks needing attention.",
    "launch_recommendation": "Launch note."
  }
}
```

`title_options` holds the 3 options. `weekly_breakdown` has one object per week. `series_title` and `series_tagline` are the option the pastor picked.
