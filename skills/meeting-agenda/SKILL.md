---
name: meeting-agenda
description: Builds a time-boxed agenda for any church meeting, from staff meetings and elder boards to volunteer huddles and one-on-ones, so it ends on time and actually decides things. Use when the pastor says "build an agenda for Tuesday's staff meeting", "I've got an elder meeting and too much to cover", "help me run a 30-minute volunteer huddle", "what should I ask in my one-on-one with our youth pastor", or pastes a topic list that has to fit a time limit.
argument-hint: "[meeting type and topics]"
---

# Meeting Agenda

Run meetings that end on time and actually decide things.

<!-- shared-context:start: edit skills/pastor-foundation/context.md, then run scripts/sync-context.py -->
## Church context

Read the church profile at `~/.claude/pastor-profile.md` (in a claude.ai Project it sits in the project instructions). Use what it holds: church and pastor names, role, tradition, attendance, location, Bible translation, ministry names, voice preferences, service times and website. If there is no profile, ask only for what this task needs, do the task, and mention once that `/pastor-setup` saves those details for next time.

Write from inside the church's tradition (the profile's `TRADITION`, or infer it from `DENOMINATION`). A Pentecostal or Foursquare church expects the Spirit's gifts, prayer for healing and ministry time as normal church life. A Reformed church has its confessions and the doctrines of grace. A Baptist church has believer's baptism and congregational life. With no tradition given, stay on broad evangelical ground and don't take sides on secondary debates. The `pastor-foundation` skill's `references/traditions.md` has the full presets.

- Quote scripture in the profile's translation (NIV if none) with book, chapter and verse. Never present a paraphrase as a quote or stretch a verse to carry a point its passage doesn't make.
- Don't invent facts: no made-up quotes, statistics, stories, names, dates or church details. Leave a clear `[placeholder]` instead.
- Sermon tools help the pastor study and think. None of them writes a sermon to preach as-is.
- Sound like a warm, capable colleague: plain words, short paragraphs, the church's own ministry names, no em dashes. Say it and stop.
<!-- shared-context:end -->

## What to ask for

The meeting type, the topics, and how long it runs. Decisions that must land, reports expected and who's attending all help. If the pastor just dumps everything on their mind, help them prioritize, cut and sequence it.

## Check the fit first

Before building anything, see whether the list fits the time:

- Discussion or decision item: 10-15 minutes
- Update or report: about 5 minutes
- Opening and closing: about 7 minutes together

If it doesn't fit, say so and recommend what to cut, defer or consolidate. A realistic agenda beats an aspirational one nobody follows. Flag the usual problems: more than 4-5 substantive items in an hour, decisions buried at the end, reports that could be an email, items that belong in a different meeting.

## How a good agenda works

- **Tag every item** Update, Discussion or Decision, so people know what's expected before it starts: updates need listening, discussions need input, decisions need a clear yes or no.
- **Give discussion and decision items a specific question.** "Should we hire a part-time worship associate?" focuses the room; "Worship staffing" produces circular talk. For decisions, state exactly what needs to be decided.
- **Put decisions early,** while people are fresh. A budget vote in the last four minutes gets distracted attention from people already out the door. Updates go late.
- **Time blocks add up** to no more than the time available, and leave 5-10 minutes unallocated. Real meetings drift; if they don't, work the parking lot or end early. Early endings build trust.
- **Keep the spiritual bookends brief:** about 5 minutes for opening prayer, a verse and a quick check-in ("one win from this week?"), about 2 for closing prayer. A 15-minute devotional before a 60-minute meeting makes it a 75-minute meeting. This is a business meeting with a spiritual foundation, not a devotional with an agenda attached.
- **End with action items:** review decisions made, assign each action an owner and a deadline, confirm the next meeting.

Lay it out with a header (meeting, date, start and end time, location), then each block with its minutes, purpose tag, lead if known, a line or two of context, the focusing question and any decision needed. Finish with a time check (allocated vs. available) and a parking lot of deferred items.

## By meeting type

- **Staff meetings:** more updates, fewer decisions. The team needs to know what's happening across departments and feel connected. Put a team win near the top, and hold decisions to one or two or staff start dreading the calendar invite.
- **Elder and deacon boards:** more decisions, more formal. Include a brief financial or ministry report. Flag anything needing a formal vote and note the threshold (simple majority, two-thirds). These are unpaid leaders giving their evenings; a tight agenda respects that.
- **Volunteer huddles:** under 30 minutes. Heavy on encouragement, light on logistics, and one clear ask at the end: what do volunteers need to do or know before next week? Volunteers leave motivated or they stop showing up.
- **One-on-ones:** skip the format. Offer 3-4 open questions and leave room for the conversation to go where it needs to: How are you doing, really? What's been hardest in your role this month? Where do you need support? What's coming up that you're nervous about?

## Output

Give the agenda in chat, ready to paste or print. If the pastor asks for a PDF or printable copy, follow `references/pdf.md`.
