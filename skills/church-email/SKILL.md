---
name: church-email
description: Turns a week's announcements, events and pastoral notes into the all-church email or newsletter, with subject lines and preview text built to get it opened. Use when the pastor says "write this week's church email", "turn these announcements into our newsletter", "here's everything happening this week, make it an email", "I need a subject line for Sunday's email", or pastes a messy list of events to send to the church.
argument-hint: "[announcements and events]"
---

# Weekly Church Email

Turn the week's announcements into an email people actually open.

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

Whatever the pastor has, in any shape: bullet points, a voice dump, a sermon recap. Useful extras: a personal note, a prayer need to highlight, the current series, service times if the profile doesn't have them.

## Decide what matters first

Before drafting, pick the lead item: the one thing the congregation most needs to know or do this week. It goes first and gets two or three sentences. Keep up to four more as supporting items at a sentence or two each, and cut or defer the rest to another channel. Tell the pastor what you cut and why. Every item feels important to whoever submitted it, but an email that treats eight things equally communicates none of them.

## Subject line and preview text

These two lines decide whether anything else gets read, so build them first.

- **Subject:** under 50 characters, specific, led by the most compelling item rather than the most official one. "3 spots left for Family Camp" gets opened; "This Week at Grace Community" gets skipped. Vary the shape week to week (a number, a name, a date, a question, a teaser), because the same formula every week trains people to ignore it. Give two options, A and B, from different angles.
- **Preview text:** 40-90 characters that add a second hook instead of repeating the subject. Subject "3 spots left for Family Camp," preview "Register by Wednesday or you'll miss it."

## The email

- **Greeting:** one or two sentences of the pastor actually showing up, tied to something real this week. "Sunday was one of those mornings I'll be thinking about for a while." Not "Greetings, church family!" or "Happy Monday!"
- **Items:** what it is, the details that matter, and one clear next step (register, sign up, show up, reply, bring a friend). Bold dates, times, places and deadlines, and nothing else, so bold always means "you need this to act." A minor event gets one sentence and a link, not a paragraph.
- **Quick links:** a short "This week:" list of 3-5 actions with their links, for the reader who skimmed. Leave off anything without a link.
- **Closing:** one warm sentence, varied week to week ("See you Sunday" is fine), then the pastor's name and church. Skip "Be blessed" and skip a reflective question meant to prompt replies.

Keep it to 200-400 words; shorter wins. Paragraphs of one to three sentences with generous line breaks, since most people read it on a phone between other things.

## Output

Give it in chat ready to paste into the email tool: Subject A, Subject B and preview text on top, then the email, then a short note of what was cut. Use `[link]` placeholders where the pastor hasn't supplied URLs.
