---
name: sermon-to-youtube
description: Builds a complete YouTube upload package for a sermon video: titles, description, chapters, tags, category, thumbnail concepts and the best short-form clip. Use when the pastor says "help me post this sermon on YouTube", "write a YouTube title and description for Sunday's message", "add timestamps to my sermon video", "what clip should we cut for a Short", or "nobody finds our sermons on YouTube".
argument-hint: "[sermon title + transcript]"
---

# Sermon to YouTube

People search YouTube every day for the questions sermons answer. A sermon titled "Sunday Service 4/6" never meets them. The gap is rarely production value; it's packaging.

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

The transcript (full is best; partial works if it covers the key moments) and the sermon or series title. Ask whether the upload is the sermon alone or the full service, and if timestamps matter, when the sermon starts in the video. Use the channel's standard "about" text if the pastor has one.

## Read the sermon first

Before writing anything, work out:

- **Core topic:** the question this sermon answers, in one sentence.
- **Movements:** the four to eight distinct sections (the problem, the passage, the story, the turn, the application). These become chapters.
- **Peaks:** where it hits hardest, the story that lands or the line people write down. These are clip candidates.
- **Search angles:** what someone would actually type to find this ("how to forgive someone who hurt you," "Romans 8 explained"), never the series name.

## The package

**Titles (three).** One search-led ("What the Bible Actually Says About Worry"), one curiosity-led ("Why Jesus Told Worried People to Look at Birds"), one plain value statement for subscribers. Put the topic first and keep the meaning inside the first 60 or so characters, since search and mobile cut longer titles off. Series names and "Pastor [Name] Preaches on..." titles tell a searcher nothing; save the series name for the description. Recommend one and say why in a sentence. Every title has to be a promise the sermon keeps: sensational or misleading titles burn trust with exactly the audience most likely to watch.

**Description (about 200 to 400 words).**
- The first two lines are all that shows before "more." Spend them on what the viewer gets, with the main search phrase in them. Don't open with the church name, the pastor's name or "Watch this sermon about."
- Chapters as `00:00 Chapter Title`, starting at 00:00, at least three of them, at least ten seconds apart (YouTube ignores chapters that break these rules). Name them by content ("Why Worry Feels Like Control"), not structure ("Point 2"). Use only times that appear in the transcript or that the pastor gave you. Otherwise write each chapter as `[mm:ss] Chapter Title (starts: "first few spoken words")` so someone can scrub to it and fill in the time. Never turn an estimate into a time.
- Two or three warm, third-person sentences about the pastor and church, with an invitation to visit or subscribe.
- Real lines for the website, social accounts and giving page, using the profile's details and a clear placeholder for anything missing.
- Write for a person. Related terms should show up naturally; no keyword list at the bottom, and never a pasted transcript.

**Tags (about 15).** A few broad ones (sermon, Bible teaching), the specific topic and passage ("Romans 8 sermon," "anxiety Bible"), and identity tags (pastor, church, city, denomination). Tags carry little weight on YouTube now, so keep them specific and skip near-duplicates.

**Category.** Usually Education for teaching and exposition, or Nonprofits & Activism for announcement and generosity videos. Pick one and give the reason.

**Thumbnail concepts (two or three).** For each: background, the actual overlay text (five words or fewer, large and high-contrast so it reads at phone size), whether the pastor's face appears and with what expression, and the feeling it gives before anyone reads it. Text and image should work together to promise the same thing as the title. Avoid the polished stock-photo look; viewers scroll past it.

**Playlist.** Name the playlist this belongs in (the series, titled by topic so a searcher understands it).

**Music.** If the upload includes worship, warn that cover songs can draw Content ID claims or get muted unless the church holds a streaming license (such as CCLI Streaming), and suggest uploading the sermon on its own.

**Short-form clip.** The single best 30 to 90 second segment for a Short, Reel or TikTok. Give the exact first and last lines verbatim so an editor can find them, its word count (about 150 spoken words is 60 seconds), a hook line for on-screen text in the first two seconds, a Shorts title under about 50 characters with a one-line description, a reminder to burn in captions (most people watch muted), and two or three sentences on why it works alone. A good clip starts inside the tension rather than at an introduction, makes one complete point or tells one complete micro-story, needs nothing else from the sermon to make sense, and has a moment worth rewatching. If a second segment is nearly as strong, name it in a line.

## Output

In chat, ready to copy: the three titles with your pick, the full description with chapters and links, the tags as one comma-separated line, the category, the playlist, the thumbnail concepts, the clip recommendation, and the music warning if it applies. List every `[mm:ss]` and other placeholder the pastor needs to fill.
