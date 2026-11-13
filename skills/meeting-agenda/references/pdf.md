# Agenda PDF

Only when the pastor asks for a PDF or a printable copy. Needs `pip install reportlab`.

Write the agenda to a JSON file, then run the script in this skill's folder:

```bash
python generate-pdf.py agenda.json             # file named from the date
python generate-pdf.py agenda.json agenda.pdf  # explicit output path
```

Delete the JSON afterward and tell the pastor where the PDF saved.

```json
{
  "meeting_type": "Staff Meeting",
  "date": "April 14, 2026",
  "start_time": "9:00 AM",
  "end_time": "10:00 AM",
  "total_minutes": 60,
  "location": "Conference Room B",
  "pastor_name": "From the profile",
  "church_name": "From the profile",
  "time_check": {"allocated": 55, "available": 60},
  "opening": {"minutes": 5, "prayer_note": "Opening prayer", "checkin_question": "One win from this week?"},
  "agenda_items": [
    {"title": "Summer Series", "minutes": 15, "purpose": "Decision", "lead": "Teaching Pastor", "context": "We need the topic and dates before briefing design.", "discussion_question": "Which of the two concepts fits where our people are right now?", "decision_needed": "Yes", "decision_detail": "Choose the series topic and confirm the start date."}
  ],
  "action_items": [{"action": "Send budget summary", "owner": "Executive Pastor", "deadline": "Friday"}],
  "closing": {"minutes": 2, "note": "Closing prayer"},
  "parking_lot": ["Building project update (deferred to April 21)"]
}
```

- `purpose` is "Update", "Discussion" or "Decision".
- `decision_needed` is "Yes" or "No"; `decision_detail` prints only when it's "Yes".
- Optional fields can be left out and their lines are skipped.
