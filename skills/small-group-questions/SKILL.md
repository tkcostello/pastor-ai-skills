---
name: small-group-questions
description: Turns Sunday's sermon into a small group discussion guide with icebreakers and 8-10 questions that move from observation to interpretation to application. Use when the pastor says "write small group questions for this week", "life group guide on Romans 8", "discussion questions from Sunday's sermon", "turn my notes into a Bible study", or "questions for our home groups".
argument-hint: "[sermon passage or summary]"
---

# Small Group Discussion Questions

Sunday's sermon becomes the week's small group conversation.

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

The passage is enough for solid questions. Sermon notes, an outline, a transcript, the big idea or an application emphasis make the guide track what was actually preached. Use the date if given.

## Find the core first

Before writing questions, pin down the sermon's big idea in one sentence (a point, not a topic: "God's faithfulness in the wilderness is the reason you can trust him in yours," not "God is faithful"), its 2-3 key themes, and the main thing it called people to do or believe. Stay in the lane the sermon opened. If it was about forgiveness and never touched justice, leave justice alone.

## The guide

Head it with the week, passage and big idea, then:

- **Icebreaker, two options** so the leader can fit the group (a 6 AM men's group and a Thursday couples' group need different doors in). One light, answerable by anyone who has never opened a Bible; one more reflective that starts toward the topic.
- **Read the passage together.** Give the reference only, not the printed text. Groups should open their Bibles; that habit matters.
- **Observation, 2 questions:** what's on the page (people, sequence, repeated words), plus one detail that's easy to miss on a first read.
- **Interpretation, 3 questions:** why the author made a specific choice; a piece of cultural or historical context that changes the meaning, kept accessible; how the passage connects to the larger biblical story.
- **Application, 3 at most:** one personal without demanding public confession ("Where do you find yourself in this story?"); one tied to work, family, money or relationships; one with some edge that presses the demand the sermon made. More than three turns the room into a confession booth, and application lands harder after the text has done its work.
- **Going deeper, 2 for groups that want more:** a cross-reference question with the reference given, and a theological question with guardrails ("What does this text tell us about how God initiates relationship with people?" rather than "Do you believe in predestination?").
- **Closing:** a prayer prompt tied to what this passage demanded, not "pray for each other's needs," and one small, concrete optional challenge someone could report back on next week.

## What makes the questions work

- Ten questions at most. Groups have 60-90 minutes, so every question earns its place.
- Keep the order: observation, interpretation, application. Starting with "what should we do?" skips the work of understanding the text.
- Open-ended only. If one word answers it, rewrite it. No leading questions with one right answer ("Don't you think God was testing Abraham here?").
- Write for the group, not a seminary class. Nothing that needs Greek or a shelf of commentaries.
- Don't lean on feelings questions. "How did this make you feel?" on repeat is therapy with a Bible on the table.
- Every question works for someone who missed Sunday. The guide stands alone with only a Bible.

## Output

Give the guide in chat, ready to paste or hand to leaders. If the pastor asks for a PDF or printable copy, follow `references/pdf.md`.
