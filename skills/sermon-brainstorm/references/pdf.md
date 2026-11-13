# Sermon Brief PDF

Only when the pastor asks for a PDF or a printable copy, after the brief is done. Needs `pip install reportlab`.

Write the brief to a JSON file, then run the script in this skill's folder:

```bash
python generate-pdf.py brief.json            # file named from the passage
python generate-pdf.py brief.json brief.pdf  # explicit output path
```

Delete the JSON afterward and tell the pastor where the PDF saved.

```json
{
  "passage": "John 11:1-44",
  "series": "Life and Death",
  "date": "2026-04-13",
  "pastor_name": "From the profile",
  "church_name": "From the profile",
  "big_idea": "Jesus delays not because he is indifferent, but because he is after something bigger than comfort.",
  "key_tension": "The God who could have prevented suffering chose not to, and that choice was love.",
  "audience_need": "People in the room are carrying grief and wondering where God is in it.",
  "desired_response": "Trust that God is present in the delay, not absent from it.",
  "the_turn": "The moment shifts from Mary and Martha questioning Jesus to Jesus weeping with them.",
  "supporting_passages": [
    { "reference": "Psalm 13:1-2", "note": "The cry of how long, a parallel to Martha and Mary." }
  ],
  "illustration_idea": "A surgeon who makes you wait because timing matters more than speed."
}
```

`series` and `date` are optional. `supporting_passages` holds 2-3 objects.
