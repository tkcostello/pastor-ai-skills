---
name: meeting-agenda
description: Use when planning or preparing any church meeting: staff meetings, elder or deacon boards, committees, volunteer huddles, or one-on-ones, or when a topic list needs to fit a time limit.
argument-hint: "[meeting type and topics]"
---

# Meeting Agenda Builder

Run meetings that end on time and actually decide things.

> Before writing: follow the pastor-foundation skill and load the church profile from `~/.claude/pastor-profile.md`. If the profile file is missing, run the pastor-setup skill first.

---

## What You Need to Provide

To build your agenda, give me the following:

- **Meeting type:** Staff meeting, elder/deacon board, volunteer huddle, committee, or one-on-one
- **Topics or items to cover:** List everything you want to address
- **Time available:** Total meeting length (example: "60 minutes")
- **Optional:** Decisions that must be made, reports expected, people attending

The more context you give, the tighter the agenda. If you're not sure what you need, list your topics and I'll help you shape it.

---

## Step 1: Assess and Prioritize

Before building the agenda, I evaluate whether your items fit your time.

**Rule of thumb:**
- Discussion or decision item: 10-15 minutes each
- Update or report: 5 minutes each
- Opening and closing: 7 minutes combined (non-negotiable)

If your list doesn't fit, I'll flag it and recommend what to cut, defer, or consolidate. The goal is a realistic agenda, not an aspirational one nobody follows.

**Common problems I'll flag:**
- More than 4-5 substantive items in a 60-minute meeting
- Decision items buried at the end where time always runs out
- Reports that could be sent via email instead of discussed live
- Items that belong in a different meeting type entirely

---

## Step 2: Build the Agenda

Every agenda follows this format:

---

```
## [Meeting Type] Agenda
**Date:** [date]
**Time:** [start] - [end] ([total] minutes)
**Location:** [if provided]

---

### Opening (5 min)
- Opening prayer / brief devotional with scripture suggestion
- Quick check-in: "What's one win from this week?"

### [Topic 1] (XX min)
**Purpose:** [Update / Discussion / Decision]
**Lead:** [who owns this, if known]
- [Key context in 1-2 sentences]
- **Discussion question:** [specific question to focus conversation]
- **Decision needed:** [Yes or No. If yes, state exactly what needs to be decided.]

### [Topic 2] (XX min)
**Purpose:** [Update / Discussion / Decision]
**Lead:** [who owns this, if known]
- [Key context in 1-2 sentences]
- **Discussion question:** [specific question to focus conversation]
- **Decision needed:** [Yes or No. If yes, state exactly what needs to be decided.]

### Action Items and Next Steps (5 min)
- Review decisions made in this meeting
- Assign action items with owners and deadlines
- Confirm next meeting date

### Closing (2 min)
- Closing prayer or brief word of encouragement

---

**Time check:** [Total allocated vs. available]
**Parking lot:** [Items deferred to a future meeting]
```

---

## Design Rules

These rules apply to every agenda I build. No exceptions.

**Tag every item.** Each agenda item gets one label: Update, Discussion, or Decision. This tells everyone what's expected of them before the item starts. Updates require listening. Discussions require input. Decisions require a clear yes or no at the end.

**Decision items get discussion questions.** Vague agenda items produce circular conversation. A specific question focuses the room. "Should we hire a part-time worship associate?" is better than "Worship staffing discussion."

**Build in a buffer.** Every agenda leaves 5-10 minutes unallocated. Real meetings drift. If everything runs perfectly, use the time for the parking lot or end early. Early endings build trust.

**Keep opening and closing brief.** Opening prayer and a check-in take 5 minutes total. Closing prayer takes 2 minutes. This is a business meeting with a spiritual foundation, not a devotional with an agenda attached.

**Time blocks must add up.** Every item gets a time allocation. Total allocated time must be equal to or less than the available meeting time. If it doesn't fit, something gets cut.

**Put decisions early, not last.** High-stakes decisions belong in the first half of the meeting when everyone's focused and energy is high. Reports and updates go at the end.

---

## Meeting Type Adjustments

### Staff Meetings
More updates, fewer decisions. The team needs to know what's happening across departments and feel connected. Include a team win near the top. Limit decisions to 1-2 items per meeting or staff starts dreading the calendar invite.

### Elder and Deacon Boards
More decisions, formal process. Include a brief financial or ministry report. Flag any items that require a formal vote and note the vote threshold (simple majority, two-thirds, etc.). Elders and deacons are giving their time as unpaid leaders. Respect that with a tight agenda.

### Volunteer Huddles
Under 30 minutes, every time. Load it with encouragement and keep logistics light. One clear ask at the end: what do you need volunteers to do or know before next week? Volunteers leave motivated or they stop showing up.

### One-on-Ones
Skip the rigid format. Use 3-4 open-ended check-in questions and leave space for the conversation to go where it needs to go. Suggested questions: How are you doing, really? What's been the hardest part of your role this month? Where do you need support? What's coming up that you're nervous about?

---

## Anti-Patterns I Will Never Build

**Fifteen items for a 60-minute meeting.** This is not an agenda, it is a wish list. Items will get cut on the fly, nothing will get proper time, and the meeting will run long anyway. Pick the top 5 and defer the rest.

**No time allocations.** An agenda without time blocks is a list. Time blocks communicate priority, keep the facilitator accountable, and give attendees a clear read on whether a discussion is going long.

**Important decision saved for last.** When the budget vote or staffing decision lands at the end of a meeting, it gets 4 minutes of distracted attention from people who are mentally already out the door. Put the most important thing first.

**Opening devotional that runs 15 minutes.** A 15-minute devotional before a 60-minute meeting means you are having a 75-minute meeting. Brief prayer and a scripture verse honors everyone's time and still centers the meeting spiritually. Long devotionals before long meetings are a form of avoidance.

---

## Example Output

Here is a sample agenda for a 60-minute staff meeting with four items:

---

```
## Staff Meeting Agenda
**Date:** April 14, 2026
**Time:** 9:00 AM - 10:00 AM (60 minutes)
**Location:** Conference Room B

---

### Opening (5 min)
- Opening prayer (brief, 1-2 minutes)
- Check-in: "What's one win from the past week?"

### Easter Weekend Debrief (15 min)
**Purpose:** Discussion
**Lead:** Lead Pastor
- We had 47 first-time guests and four salvations. How did the team feel it went?
- **Discussion question:** What worked better than expected, and what would we do differently next year?
- **Decision needed:** No.

### Summer Series Planning (15 min)
**Purpose:** Decision
**Lead:** Teaching Pastor
- We need to lock in the summer series topic and dates before we can brief the design team.
- **Discussion question:** Between the two proposed series concepts, which one better fits where our congregation is right now?
- **Decision needed:** Yes. Choose series topic and confirm start date.

### Children's Ministry Volunteer Gap (10 min)
**Purpose:** Discussion
**Lead:** Children's Director
- We're 6 volunteers short for the summer. Current recruiting efforts have stalled.
- **Discussion question:** What are two or three recruitment channels we haven't tried yet?
- **Decision needed:** No. Decision will come in next week's meeting after options are explored.

### Budget Update (5 min)
**Purpose:** Update
**Lead:** Executive Pastor
- Q1 came in 3% under budget. Brief overview of what's ahead in Q2.
- **Decision needed:** No.

### Action Items and Next Steps (8 min)
- Review: Series topic and start date agreed on
- Assign: Children's Director to return next week with 3 recruitment ideas
- Assign: Executive Pastor to send Q1 budget summary by Friday
- Confirm: Next staff meeting April 21

### Closing (2 min)
- Closing prayer

---

**Time check:** 60 minutes allocated / 60 minutes available
**Parking lot:** Building project update (deferred to April 21 meeting)
```

---

## How to Use This Skill

Paste or describe your meeting details and I will build a complete, ready-to-run agenda. Include your meeting type, time available, and topics to cover. If you have specific decisions that must land in this meeting, name them. The more specific you are, the more useful the agenda.

If you are not sure what belongs on the agenda, list everything on your mind and I will help you prioritize, cut, and sequence it.

---

## Output Format

After building the agenda, generate a JSON file matching this schema and pass it to `generate-pdf.py` to produce a REACHRIGHT-branded PDF.

```json
{
  "meeting_type": "Staff Meeting",
  "date": "April 14, 2026",
  "start_time": "9:00 AM",
  "end_time": "10:00 AM",
  "total_minutes": 60,
  "location": "Conference Room B",
  "pastor_name": "PASTOR_NAME from foundation",
  "church_name": "CHURCH_NAME from foundation",
  "time_check": {"allocated": 60, "available": 60},
  "opening": {"minutes": 5, "prayer_note": "Opening prayer", "checkin_question": "One win from this week?"},
  "agenda_items": [
    {"title": "Easter Debrief", "minutes": 15, "purpose": "Discussion", "lead": "Lead Pastor", "context": "47 guests, four salvations.", "discussion_question": "What worked better than expected?", "decision_needed": "No", "decision_detail": ""}
  ],
  "action_items": [{"action": "Send budget summary", "owner": "Executive Pastor", "deadline": "Friday"}],
  "closing": {"minutes": 2, "note": "Closing prayer"},
  "parking_lot": ["Building project update (deferred to April 21)"]
}
```

**Field notes:**

- **purpose** must be one of: "Update", "Discussion", or "Decision"
- **decision_needed** must be "Yes" or "No"
- **decision_detail** is only used when decision_needed is "Yes"
- Do not use em dashes in any field values
