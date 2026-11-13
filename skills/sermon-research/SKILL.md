---
name: sermon-research
description: Researches a scripture passage for preaching or teaching (context, background, word studies, commentary, cross-references, themes and interpretive questions) without writing or outlining the sermon. Use when the pastor says "research Romans 8:1-11 for Sunday", "give me background on this passage", "what do the commentaries say about John 4", "word study on this text", or "help me study Ephesians 2 before I preach it".
argument-hint: "[passage]"
---

# Sermon Research

Compress the front end of study so the pastor spends the week thinking and praying, not hunting for background. Research only: keeping it separate from structure stops the pastor from preaching what they already believed instead of what the text demands.

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

The passage is enough; start without follow-up questions. Use anything else offered: the angle they're preaching through, the series and where this week falls, interpretive questions they're wrestling with (answer those directly along the way).

## The research, in seven steps

### 1. Passage context

Two or three paragraphs to orient, not overwhelm: author, date and recipients; what the original community was dealing with, expecting or fearing; genre (epistle, narrative, poetry, apocalyptic, wisdom) and how it shapes what the passage demands; where it falls in the book's argument or story, what came just before and what follows.

### 2. Historical and cultural background

Two or three dense, specific paragraphs, not a general history lesson: who held power and what daily life was like; the religious setting (Jewish law, Roman religion, local practice) and the assumptions people carried; practices like hospitality, honor and shame, patronage, purity and farming cycles. Flag two or three details a modern reader would read past that the original audience would have caught at once.

Read history plainly before asking what it means theologically. The census was a political act; the Temple was a real place with real commerce. Context is not a metaphor.

### 3. Key word study

Pick 3-5 words that carry theological weight, have a range of meaning that affects interpretation, or are translated inconsistently. For each, in a table: English word, transliteration, literal meaning, range of meaning elsewhere in Scripture, and how NIV, ESV, KJV, NLT and NASB render it. The aim is a better interpretive decision the pastor can explain without a seminary lecture.

### 4. Commentary insights

Draw on 3-5 commentators or traditions: the passage's main interpretive question and where scholars land, where they agree (a signal worth noting), where they diverge (usually a real tension in the text), and both technical and pastoral angles.

Name the commentators and the works. Don't invent commentary quotes or page numbers: summarize a commentator's position and name the work, and say so when you're unsure what a specific commentator wrote. When a passage is contested, say so plainly rather than picking a side for the pastor. `references/commentary-sources.md` lists the sources to draw on.

### 5. Cross-references

Five to eight passages, each with the reference, one sentence on why it matters here, and its type: *Direct parallel* (same event or teaching from another angle), *Thematic connection* (develops the same idea) or *OT background* (a text the passage quotes, alludes to or assumes). Every one should earn its place: clarify a word, trace the theme across the canon, or give a second way into the same truth.

### 6. Theological themes

Three to five themes, each with a short name, where and how the passage develops it, and one practical implication for a local congregation: what question it answers, what fear it addresses, what obedience it calls for. A map of the terrain, not an outline.

### 7. Thinking prompts

Five to seven interpretive pressure tests, written for this passage, to push the pastor's thinking before any outline or illustration. The kind of thing to ask:

- What assumption will the congregation bring that the original audience wouldn't have had?
- Where is the natural application too easy, and where is it harder than it looks?
- What does this passage demand that people probably don't want to hear?
- If everyone walks out feeling good, was the whole text preached?
- What is the most common way this passage is mishandled from the pulpit, and how do you avoid it?

## What to hold back

No sermon outline, point structure or suggested way to organize the message, even if asked. Structure belongs to the pastor's own prep.

## Output

Give the research in chat with clear headings for the seven sections. If the pastor asks for a PDF or printable copy, follow `references/pdf.md`.
