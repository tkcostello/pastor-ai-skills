---
name: social-media-calendar
description: Plans a week or month of church social media posts by date and platform, built around the sermon series and church calendar. Use when the pastor says "plan our social posts for next week", "build April's social media calendar", "what should we post this month", "map out posts around Easter and baptism Sunday", or "give our volunteer a posting schedule".
argument-hint: "[week or month + what's coming up]"
---

# Social Media Content Calendar

A posting plan a small church team can actually keep, built around Sunday.

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

The date range, the sermon series or topics, and anything on the church calendar (baptisms, outreach, guest speakers, a giving or missions emphasis, holidays). Default to four or five posts a week unless the pastor says otherwise. Work with whatever they give; a single sentence is enough to start.

## Building the plan

Place things in this order: major events first (Easter, launch Sunday, baptisms) since everything around them should build toward them; then the sermon, so Sunday gets a quote or recap and the week echoes its theme; then a steady thread of engagement posts; then testimonies, behind-the-scenes and practical posts as fill.

A rhythm that works for most churches, to adapt freely:

- **Sunday:** sermon quote or recap
- **Monday:** behind the scenes or a team or volunteer highlight
- **Tuesday:** a question or poll
- **Wednesday:** midweek encouragement from scripture
- **Thursday:** event promo or a practical help
- **Friday:** something light, or a testimony
- **Saturday:** Sunday preview and invitation

Not every day needs a post. Four or five a week that people stop for beats seven they scroll past, and a volunteer can sustain it. Keep to one feed post per platform per day; Stories don't count. Include one short vertical video a week (the sermon clip from `sermon-to-youtube`, or a 15-second phone video) as a Reel. Every idea should be doable with a phone photo or a simple text graphic; a plan that waits on a designer for every post doesn't get executed. If an idea is weak, leave the day empty.

## Output

In chat:

1. A short overview of the period: the themes and the anchor moments you built around.
2. A table with date, day, platform (Facebook, Instagram or both), post type, a specific content idea someone could write from or hand to a volunteer, the call to action, who supplies the photo, video or words, and the date it needs to be ready.
3. A Sunday shot list: the four to six photos and short clips someone needs to capture on Sunday for the week's posts.
4. Graphics needed: which posts need a designed asset, what it is, and when it needs to be ready.
5. One or two evergreen posts that can be made ahead and held as backups for a week that falls apart.
6. Platform notes: which posts can be shared to both with small changes and which need a different hook, format or caption length.

Offer to write the whole first week's captions in one pass, following the `church-social-post` skill.
