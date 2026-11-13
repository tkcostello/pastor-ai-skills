---
name: sermon-to-youtube
description: Builds a complete YouTube upload package for a sermon video: titles, description, chapters, tags, category, thumbnail concepts and the best short-form clip. Use when the pastor says "help me post this sermon on YouTube", "write a YouTube title and description for Sunday's message", "add timestamps to my sermon video", "what clip should we cut for a Short", or "nobody finds our sermons on YouTube".
argument-hint: "[sermon title + transcript]"
---

# Sermon to YouTube

People search YouTube every day for the questions sermons answer. A sermon titled "Sunday Service 4/6" never meets them. The gap is rarely production value; it's packaging.

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

The transcript (full is best; partial works if it covers the key moments) and the sermon or series title. Ask for the video length if timestamps matter, and use the channel's standard "about" text if the pastor has one.

## Read the sermon first

Before writing anything, work out:

- **Core topic:** the question this sermon answers, in one sentence.
- **Movements:** the four to eight distinct sections (the problem, the passage, the story, the turn, the application). These become chapters.
- **Peaks:** where it hits hardest, the story that lands or the line people write down. These are clip candidates.
- **Search angles:** what someone would actually type to find this ("how to forgive someone who hurt you," "Romans 8 explained"), never the series name.

## The package

**Titles (three).** One search-led ("What the Bible Actually Says About Worry"), one curiosity-led ("The Verse About Fear No One Talks About"), one plain value statement for subscribers. Put the topic first and keep the meaning inside the first 60 or so characters, since search and mobile cut longer titles off. Series names and "Pastor [Name] Preaches on..." titles tell a searcher nothing; save the series name for the description. Recommend one and say why in a sentence. Every title has to be a promise the sermon keeps: sensational or misleading titles burn trust with exactly the audience most likely to watch.

**Description (about 200 to 400 words).**
- The first two lines are all that shows before "more." Spend them on what the viewer gets, with the main search phrase in them. Don't open with the church name, the pastor's name or "Watch this sermon about."
- Chapters as `00:00 Chapter Title`, starting at 00:00, at least three of them, at least ten seconds apart (YouTube ignores chapters that break these rules). Name them by content ("Why Worry Feels Like Control"), not structure ("Point 2"). If you're estimating from transcript pacing, say so and tell the pastor to check them against the video before publishing.
- Two or three warm, third-person sentences about the pastor and church, with an invitation to visit or subscribe.
- Real lines for the website, social accounts and giving page, using the profile's details and a clear placeholder for anything missing.
- Write for a person. Related terms should show up naturally; no keyword list at the bottom, and never a pasted transcript.

**Tags (about 15).** A few broad ones (sermon, Bible teaching), the specific topic and passage ("Romans 8 sermon," "anxiety Bible"), and identity tags (pastor, church, city, denomination). Tags carry little weight on YouTube now, so keep them specific and skip near-duplicates.

**Category.** Usually Education for teaching and exposition, or Nonprofits & Activism for announcement and generosity videos. Pick one and give the reason.

**Thumbnail concepts (two or three).** For each: background, the actual overlay text (five words or fewer, large and high-contrast so it reads at phone size), whether the pastor's face appears and with what expression, and the feeling it gives before anyone reads it. Text and image should work together to promise the same thing as the title. Avoid the polished stock-photo look; viewers scroll past it.

**Short-form clip.** The single best 30 to 60 second segment for a Short, Reel or TikTok. Give approximate start and end times, the transcript excerpt, a title under about 50 characters, and two or three sentences on why it works alone. A good clip starts inside the tension rather than at an introduction, makes one complete point or tells one complete micro-story, needs nothing else from the sermon to make sense, and has a moment worth rewatching. If a second segment is nearly as strong, name it in a line.

## Output

In chat, ready to copy: the three titles with your pick, the full description with chapters and links, the tags as one comma-separated line, the category, the thumbnail concepts, and the clip recommendation. Flag any estimated timestamps and any placeholders the pastor needs to fill.
