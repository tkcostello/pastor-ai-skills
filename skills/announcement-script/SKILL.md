---
name: announcement-script
description: Use when preparing Sunday morning announcements: a spoken script for the stage, worship host, or announcement video.
argument-hint: "[announcements to include]"
---

# Sunday Announcement Script

**Say what matters in 90 seconds or less.**

> Before writing: follow the pastor-foundation skill and load the church profile from `~/.claude/pastor-profile.md`. If the profile file is missing, run the pastor-setup skill first.

---

## What This Skill Does

Most Sunday announcements are boring because they try to cover everything. This skill does the opposite. It forces ruthless prioritization, then writes a word-for-word spoken script that opens with energy, moves fast, and lands every item with a clear call to action.

The result: people actually listen, and you're done in under 90 seconds.

---

## Input

Provide a list of announcements to work from. Include anything you're considering mentioning. More is fine. This skill will sort it out.

**Required:**
- A list of announcements (events, deadlines, updates, volunteer needs, giving moments, anything)

**Optional:**
- Who is delivering the announcements (pastor, worship leader, volunteer, etc.)
- The overall tone of the service (celebratory, reflective, high energy, quiet)
- Any announcement that is non-negotiable and must be spoken

**Example input:**
```
- Women's Bible study starts Thursday, 7pm, room 214
- Volunteer signup for summer VBS
- Baptism Sunday is April 20th, sign up at the welcome table
- Offering moment
- New sermon series starts next week
- Youth group rescheduled from Friday to Saturday this week
- Food pantry needs canned goods
```

---

## Workflow

### Step 1: Triage

If more than 4 items are submitted, force-rank them by two criteria:

1. **Urgency:** Is there a deadline this week or next? Would missing this cost someone a real opportunity?
2. **Relevance to the whole room:** Does this apply to most of the congregation, or just a small segment?

Only the top 3-4 items make the spoken script. Everything else gets bumped to the bulletin, slides, or email section at the bottom of the output. Be decisive. Crowding the script helps no one.

If an item was marked non-negotiable by the submitter, it stays in the spoken script regardless of rank.

---

### Step 2: Write the Script

Write a complete, word-for-word spoken script. No fill-in-the-blank. No placeholders. Every sentence should be deliverable as written.

**Rules:**

**Opening hook.** Do not open with "We have a few announcements" or any variation of it. Open with something that earns attention. A question, a bold statement, a brief moment of connection to what just happened in worship, or a direct lead into the first announcement. Examples:
- "Before we go any further, I need 60 seconds of your attention because what I'm about to tell you matters."
- "A few things that can genuinely change your week."
- "Three things. One minute. Here we go."

**Each announcement: 2-3 sentences max.** Structure every item the same way:
1. Why it matters to the person in the seat (the benefit, the transformation, the need being met)
2. The logistics (date, time, location, what to do)
3. One clear single action (sign up, talk to someone, grab a card, text a number)

Do not include room numbers, committee chair names, or other fine print in the spoken script. That belongs in the bulletin.

**Transitions.** Write brief natural bridges between items. Not "Number two." Not "Also." Something that moves the energy forward without sounding like a list.

**Close.** End with a warm, forward-facing transition into the next part of the service. Not "That's all!" or "Back to you, pastor." Something that lands and leads. Examples:
- "Alright. Now let's do what we came here to do."
- "That's what's ahead. Right now, let's turn our attention to giving."
- "Now, let's worship."

**Length:** 60-90 seconds spoken at a natural pace. That is 150-225 words for the script body. Stay in that range.

**Delivery notes.** Add brief parenthetical cues where helpful: (pause), (smile), (hold up the card), (point to the screen). Keep them minimal. Only where it genuinely helps the delivery.

---

## Output Format

Output is a **branded single-page PDF** designed to be printed and handed to the announcer. The PDF generator lives at `generate-pdf.py` in this skill folder.

### PDF Layout

1. **Header:** "Sunday Announcements" in navy, centered, bold
2. **Meta line:** date | estimated seconds | items covered out of submitted (centered, gray)
3. **Gold accent rule**
4. **Deliverer/tone notes** in italic slate (if provided)
5. **Script body** in readable serif type. Delivery cues written as `[pause]` in the JSON render as *(pause)* in italic slate color inline.
6. **Divider** (thin gray rule)
7. **Bumped items section:** "For the Bulletin / Slides / Email" header with bullet list of items that did not make the spoken cut
8. **Footer:** thin gray rule with page number only (no REACHRIGHT branding)

### JSON Schema

Save the structured output as JSON matching this schema, then run `python generate-pdf.py input.json` to produce the PDF.

```json
{
  "date": "April 20, 2026",
  "estimated_seconds": 75,
  "items_submitted": 7,
  "items_covered": 3,
  "deliverer": "Worship Pastor",
  "tone_notes": "High energy, celebratory. Baptism Sunday.",
  "script_body": "Full script text. Use [cue] for delivery cues. Separate paragraphs with double newlines.",
  "bumped_items": [
    {"item": "Youth group schedule change", "summary": "Friday moved to Saturday this week only."}
  ]
}
```

**Field notes:**

- `script_body` -- Use `[brackets]` for delivery cues (e.g., `[pause]`, `[smile]`, `[point to screen]`). They render as italic colored text in the PDF. Separate paragraphs with double newlines (`\n\n`).
- `bumped_items` -- Announcements that did not make the spoken script. Each has an `item` name and a one-line `summary` with key logistics.
- `deliverer` and `tone_notes` are optional. If omitted, those lines are skipped in the PDF.
- The PDF is church-branded (no REACHRIGHT footer).

---

## Anti-Patterns

Never do any of these:

- **Exceed 90 seconds.** If the script runs long, cut an item. Do not compress by talking faster.
- **Open with "We have a few announcements."** Or any version of it. This is the universal signal for people to check their phones.
- **Include fine print in the spoken script.** Room numbers, committee chairs, budget lines, parking instructions. All of that belongs in the bulletin. The spoken script carries the headline and the action only.
- **Use vague CTAs.** "Check it out!" or "Learn more!" are not actions. Every item ends with one specific thing a person can do right now or this week.
- **End with dead phrases.** "That's all I got!" "That's it for announcements!" "Back to you, pastor!" None of these. The close should land the script and lead forward.
- **Write for the announcer, not the listener.** Every sentence should answer the question: why does this matter to the person sitting in that seat right now?

---

## Examples

### Example: Strong Opening (Good)

"Before we get to worship, three things you actually want to know about."

### Example: Weak Opening (Bad)

"Okay, so we have a couple of announcements real quick."

---

### Example: Strong Announcement Item (Good)

"If you've been thinking about getting baptized, this is your moment. Baptism Sunday is April 20th. Grab a card from the welcome table on your way out and hand it to anyone on our team."

### Example: Weak Announcement Item (Bad)

"We're having Baptism Sunday on April 20th, coordinated by the pastoral care team. If you're interested, you can find more information on the back table or talk to someone from the committee, and there are forms available in room 214."

---

### Example: Strong Close (Good)

"Alright. That's what's coming. Right now, let's give our attention to what matters most."

### Example: Weak Close (Bad)

"Okay, that's all I've got! Back to you, Pastor Dave."

---

## Notes for the Deliverer

If the person making announcements is not the lead pastor, include a brief note at the top of the output with one or two tone reminders specific to whoever is delivering. A worship leader carries different energy than a volunteer coordinator. The script should feel natural in their voice, not borrowed from someone else.

When in doubt, write shorter. Ninety seconds feels like three minutes when the congregation is waiting to worship. Respect their attention. Earn it fast. Get out clean.
