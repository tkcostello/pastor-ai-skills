---
name: sermon-series
description: Plans a multi-week sermon series from a theme, book of the Bible or church season, with title options, a week-by-week breakdown, the series arc and practical notes. Use when the pastor says "plan a 5-week series on James", "I need a fall series on prayer", "map out our preaching calendar through Easter", "give me series title ideas for Ruth", or "how long should a series on the Sermon on the Mount be".
argument-hint: "[theme or book] [number of weeks]"
---

# Sermon Series Planner

Map a series so every week builds on the last and the people who come every Sunday feel they traveled somewhere.

<!-- shared-context:start: edit skills/pastor-foundation/context.md, then run scripts/sync-context.py -->
## Church context

Read the church profile at `~/.claude/pastor-profile.md` (in a claude.ai Project it sits in the project instructions). Use what it holds: church and pastor names, role, tradition, polity, attendance, location, Bible translation, ministry names, voice preferences, service times, website and giving link. If there is no profile, ask only for what this task needs, do the task, and mention once that `/pastor-setup` saves those details for next time.

Write as the person in the profile. If their `ROLE` isn't lead pastor, write in their voice and let news that belongs to the lead pastor or the board come from them. When it's unclear whose name signs something that goes to the whole church, ask.

Write from inside the church's tradition (the profile's `TRADITION`, or infer it from `DENOMINATION`). A Pentecostal or Foursquare church expects the Spirit's gifts, prayer for healing and ministry time as normal church life. A Reformed church has its confessions and the doctrines of grace. A Baptist church has believer's baptism and congregational life. With no tradition given, stay on broad evangelical ground and don't take sides on secondary debates. The `pastor-foundation` skill's `references/traditions.md` has the full presets, including each tradition's church calendar.

- Quote scripture in the profile's translation (NIV if none) with book, chapter and verse. Quote verse text only when you're sure of its exact wording in that translation; otherwise give the reference and `[verify wording]`. Don't stretch a verse to carry a point its passage doesn't make.
- Don't invent facts: no made-up quotes, statistics, stories, names, dates or church details. Leave a clear `[placeholder]` instead.
- Protect people. Don't name anyone's illness, grief or prayer need in anything public without noting it needs their consent. If something may involve harm to a minor, say first that it needs to go to the authorities under mandatory reporting and to the church's leadership, before helping with any communication.
- Sermon tools help the pastor study and think. None of them writes a sermon to preach as-is.
- Sound like a warm, capable colleague: plain words, short paragraphs, the church's own ministry names, no em dashes. Say it and stop.
<!-- shared-context:end -->

## What to ask for

A theme, topic or book plus a number of weeks (or "suggest a length") is enough. Use any constraints offered: a start date, Easter on week 4, a guest preacher, a giving emphasis, seeker-friendly, a season the church is going through.

## The plan

**1. Scope.** One paragraph, and if the premise needs adjusting, say so before building the rest. For a book: does it fit the timeframe whole, or does it need a focused portion? Philippians, James and Ruth fit 4-6 weeks; Romans or Genesis need a curated selection or several series. For a theme: find the 4-8 strongest anchor passages with one clear through-line rather than a concordance dump, and narrow anything too broad ("faith") to a real angle. If the goal is vague ("get us going again", "something for January"), name the goal you're assuming in one sentence and offer one alternative angle in another.

**2. Three title options**, each written as `Title: tagline`, the tagline one line for a graphic or promo. Three keeps the decision easy. Titles are 2-4 words, memorable and usable on a banner. Avoid worn-out series names (Unshakeable, Breakthrough, Reset, Anchored, Deep Dive, Level Up), and use a pun only if it's actually good. Let the pastor pick one or redirect.

**3. Weekly breakdown**, as a table: week, date, sermon title, primary passage, big idea, connective thread. When a start date is known or implied ("January", "starting after Easter"), fill in the real Sunday dates and flag holidays, low-attendance weeks (holiday weekends, spring break, summer) and the special Sundays in the tradition's calendar notes (`pastor-foundation` skill, `references/traditions.md`). Without a date, leave the date column out.
- Sermon titles should make someone want to be in the room ("Faith That Works," not "James Chapter 2"), and they shouldn't all follow one formula (all questions, all one word, all alliterative).
- One primary passage per week. One text preached well beats three skimmed.
- The big idea is a one-sentence claim, not a topic. If it could fit 40 different sermons, it isn't sharp yet.
- A title, tagline or big idea that echoes a verse must match its wording in the profile's translation.
- The connective thread says how the week follows the last and pulls toward the next. That is what makes it a series rather than a collection.
- Build the arc: week 1 sets the premise or tension strongly enough to hook, the middle develops it, and the strongest sermon lands near the end. Flag it if the best material sits in week 2.

**4. Series arc.** Two or three sentences on where the series starts emotionally and theologically, where it builds and where it lands, in plain words the pastor can reuse with elders and in promo copy.

**5. Practical notes.**
- *Duration check:* attention on one series holds well through about 6 weeks and drops after 8. Say if the request runs long (don't plan past 8 unless asked) or if 4 weeks rushes rich material.
- *Weeks needing attention:* emotionally heavy topics (grief, sin, money, sexuality), theologically complex weeks, and visitor spikes like Easter, Christmas or a community event.
- *Launch:* one sentence on how to open strong, such as a teaser the Sunday before, a cold open, or a pre-series event or mailer.

## Output

Give the full plan in chat. If the pastor asks for a PDF or printable copy, follow `references/pdf.md`.
