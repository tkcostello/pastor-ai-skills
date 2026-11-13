---
name: announcement-script
description: Writes a word-for-word spoken announcement script for Sunday morning, cut to the three or four items that matter and kept under 90 seconds. Use when the pastor says "write Sunday's announcements", "turn this list into a script for our worship leader", "we have too many announcements, help me cut them", "script for our announcement video", or pastes this week's events for the stage.
argument-hint: "[announcements to include]"
---

# Sunday Announcement Script

Say what matters in 90 seconds or less.

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

The list of everything being considered; more is fine. Helpful extras: who is delivering it (lead pastor, worship leader, volunteer), the tone of the service, and anything that has to be said aloud no matter what.

## Cut first

Announcements get tuned out because they try to cover everything. If there are more than four items, rank them by urgency (a deadline this week or next, a real opportunity someone would miss) and by how much of the room it applies to. Only the top three or four make the spoken script. Everything else goes in a short "For the bulletin, slides or email" list at the end with its key logistics. Anything the pastor marked as must-say stays in regardless of rank. Be decisive: a crowded script helps no one.

## Writing for the ear

- **Open with something that earns attention,** not "We have a few announcements," which is the room's cue to check their phones. A bold line, a tie to what just happened in worship, or straight into the first item: "Three things. One minute. Here we go."
- **Give each item two or three sentences:** why it matters to the person in the seat, the logistics they need (day, time, place), and one specific action (grab a card, text a number, sign up at the table). "Check it out" isn't an action.
- **Leave the fine print for the bulletin.** Room numbers, committee chairs, parking details and form locations don't survive being heard once.
- **Bridge between items** with a natural spoken transition, not "Number two" or "Also."
- **Close by leading into what's next** in the service ("Now, let's worship."), not "That's all I've got" or "Back to you, Pastor."
- **Keep it to 150-225 words,** which is 60-90 seconds at a natural pace. If it runs long, cut an item rather than asking the announcer to talk faster. Ninety seconds feels like three minutes to a room waiting to worship.

Write every sentence so it can be read aloud as written, with no blanks to fill. Add a delivery cue in brackets only where it helps: [pause], [hold up the card], [point to the screen]. If someone other than the lead pastor is delivering, add a one- or two-line tone note at the top so the script fits their voice and energy.

## Output

Give the script in chat with its estimated length in seconds and the bumped items below it. If the pastor asks for a PDF or printable copy for the announcer, follow `references/pdf.md`.
