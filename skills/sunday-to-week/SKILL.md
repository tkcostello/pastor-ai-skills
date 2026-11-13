---
name: sunday-to-week
description: Turns one sermon transcript or set of notes into the whole week's content in a single pass (small group guide, midweek devotional, email recap, social posts, YouTube package and blog post), all built on the same core. Use when the pastor says "repurpose Sunday's sermon", "turn this transcript into everything for the week", "I need all the content from this message", "do the whole week from Sunday", or "one sermon, everything we post this week".
argument-hint: "[paste transcript or notes]"
---

# Sunday to Week

One sermon in, the week's content out, every piece drawing on the same big idea and the same words.

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

The transcript (best) or notes with the main points, scripture and stories. If the pastor didn't say which pieces they want, ask once: "All of it (small group guide, devotional, email recap, social posts, YouTube package, blog), or just some?" Default to all. If timestamps matter for YouTube, ask whether the video is the sermon alone or the full service.

## Pull the core once

Before writing any piece, work out and show:

- **Big idea:** one sentence, the transferable truth rather than the title.
- **Passage:** the one text the message hangs on, with reference.
- **Quotable lines:** three to five lines copied verbatim from the transcript, cleaned only of filler words ("um," repeated words). Never polish them into lines the pastor didn't say.
- **Best story:** the illustration that works outside the room. Flag it if it involves family, named people or a sensitive moment, and don't use it anywhere until the pastor says it's fine to share.
- **Clip candidates:** one or two, each given by its exact first and last spoken line.

Every piece below draws its quotes, story and clip from this core, so the week says one thing.

## The pieces

Produce them in this order, since earlier pieces feed later ones: small group guide, midweek devotional, email recap, social posts for the week, YouTube package, blog post.

For each piece, if the sibling skill is installed, read its SKILL.md and follow its guidance: `../small-group-questions/SKILL.md`, `../midweek-devotional/SKILL.md`, `../church-email/SKILL.md`, `../social-media-calendar/SKILL.md` and `../church-social-post/SKILL.md`, `../sermon-to-youtube/SKILL.md`, `../sermon-to-blog/SKILL.md`. Read only the ones for pieces you're producing. If a sibling isn't installed, keep that piece short and practical.

Two adjustments when they're part of one week:

- **Email recap** is one paragraph recapping Sunday's message with a link to watch, ready to drop into the church email, not the whole email.
- **Social posts** are a week's plan (Monday through Saturday) with captions written in full, using the quotable lines and the clip, not a separate topic.

Don't repeat the same quote in every piece. Spread the quotable lines across the week.

## Keeping it manageable

All six pieces are a lot to read at once. If the pastor wants everything, deliver the core and the first two or three pieces, then say what's next and continue when they're ready.

## Output

In chat, under clear headings: the core first, then each piece in the order above. List every placeholder and flagged story at the end. Offer to save the set as one file per piece (for example `sunday-to-week/small-group-guide.md`, `devotional.md`, `email-recap.md`, `social-week.md`, `youtube.md`, `blog.md`).
