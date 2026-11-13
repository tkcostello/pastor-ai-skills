---
name: midweek-devotional
description: Writes a short midweek devotional (about 200-300 words) for the congregation's email, app or text. Use when the pastor says "write this week's devotional", "midweek devo on Psalm 46", "something encouraging to send Wednesday", "a short devotional tied to Sunday's sermon", or gives a verse or theme for a between-Sundays note.
argument-hint: "[verse, passage or theme]"
---

# Midweek Devotional

A short note from the pastor that lands on Wednesday: one passage, one honest thought, something to carry into the rest of the week.

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

A verse, passage or theme is enough. Use anything else the pastor offers: the current sermon series, something the church or town is going through this week.

## The voice

Write it the way a pastor texts a friend who's having a hard week. First person is good. Skip the greeting ("Happy Wednesday, church family!") and start inside a real moment the reader will recognize, like how Sunday's resolve tends to fade by midweek. Quote one to three verses in full and let them stand without a verse-by-verse breakdown. Then stay with one idea, tied to something concrete people are carrying this week rather than a thought that fits any week of any year. Give them one line they could repeat to a coworker. End with a short prayer (we, us, our) or a blessing, not both, and with no sign-off after it.

Keep it to roughly 200-300 words, short paragraphs, no section labels in the finished piece. If the pastor mentioned the sermon series, one light line of connection is plenty ("We've been in Philippians on Sundays..."). It's a devotional, not a sermon or an announcement: leave events and promotions for the church email.

If the passage reads awkwardly in the profile's translation, note the translation used in italics at the end.

## Output

Give the devotional in chat, ready to paste. If the pastor asks for a PDF or printable copy, follow `references/pdf.md`.
