---
name: church-social-post
description: Writes one church social media post, tailored separately for Facebook, Instagram and X, from an event, sermon line, verse, story or idea. Use when the pastor says "write a Facebook post about our baptisms", "Instagram caption for Easter", "turn this sermon quote into a post", "something to post on Monday about Romans 8:28", or "I need to post something this week and have no idea what".
argument-hint: "[topic or event]"
---

# Church Social Media Post

One idea, written three ways, because each platform reads differently.

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

Anything works: an event with its date and time, a verse, a sermon line, a church story or milestone, or nothing at all (then offer an engagement question or a behind-the-scenes idea). Ask which platforms only if it matters; the default is all three. For events, make sure you have the date, time, place and the one thing people should do.

## Pick the post type

Match the input: a verse becomes a quote graphic with a short reflection; an event becomes a promo with one clear call to action; a sermon line becomes a thought-provoking caption; a win or story becomes a celebration or testimony post. Use the pastor's preference if they have one. Say in a line which type you chose.

## Each platform

Write a separate post for each. The same caption pasted everywhere reads wrong on at least two of them.

- **Facebook.** The audience skews older and reads more. About 100 to 250 words: a first line that stops the scroll, a little context or story, one call to action, and a question people will actually want to answer. Never post a bare link; write the post around it.
- **Instagram.** Image first, caption second. The first line has to work on its own, since only a line or so shows before "more." Keep it to roughly 50 to 150 words with three to five specific hashtags at the end, never at the start. Suggest a carousel when the content is a list, and a Story idea (poll, question or countdown sticker) when it fits.
- **X.** Short, direct and conversational, well under the 280-character limit, with zero or one hashtag. Note when an idea is better as a short thread and what each post would cover.

Scripture never goes up alone. "Jeremiah 29:11" with nothing else is noise; give it a sentence connecting it to real life this week.

## Image direction

For each post, describe the image specifically enough to brief a volunteer or pick a photo. For quote graphics, give the exact text (15 words or fewer), the type style, a color direction that fits the church's brand if known, and the background. A good phone photo of real people from the church beats stock imagery.

## Output

In chat: the post type in one line, then the Facebook post, the Instagram caption with hashtags (plus Story or carousel idea if relevant), and the X post, each with its image suggestion. Add one quick tip on timing or reuse only if there's something worth saying.
