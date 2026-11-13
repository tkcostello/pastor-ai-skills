---
name: sermon-to-blog
description: Turns a preached sermon (transcript, notes or outline) into a standalone, search-friendly blog post for the church website. Use when the pastor says "turn Sunday's sermon into a blog post", "make this transcript a blog", "write up my message for the website", "blog version of this sermon", or pastes sermon notes and asks for an article.
argument-hint: "[paste transcript or notes]"
---

# Sermon to Blog Post

Rebuild the sermon as an article for someone who never heard it, reading on a phone. It is not a transcript, and it is not a summary of the service.

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

A transcript is best; notes or an outline with the main points, scripture and stories will do. Use a target keyword if the pastor has one. If not, pick the plain phrase a person would actually search for this topic ("what the Bible says about forgiveness") and say which you chose.

## Find the core first

Before drafting, pull out the big idea in one sentence (the transferable truth, not the sermon title or passage), the one passage the message hangs on, the illustration that will work in print, and the three or four takeaways a reader can act on. Those decide the structure. Leave the rest of the sermon behind.

## Writing it for readers

- **Title.** Name the question or truth, not the series ("The Anchor Holds, Week 3" means nothing to a searcher). Keep it around 60 characters so it isn't cut off in search results, with the keyword in it naturally. Offer three and recommend one.
- **Meta description.** About 150 to 160 characters saying what the reader gets, in a human sentence.
- **Opening.** Two or three sentences that start where the reader is: a tension, a question, a moment they'll recognize. Don't open with "Last Sunday I preached," the sermon title, a block of scripture or "In this post we'll explore." Someone arriving from search doesn't know or care that it was a sermon yet.
- **Body.** Three or four sections with H2 subheadings that say something, one sermon point each. Weave scripture in by phrase and reference rather than block-quoting every point. Retell stories for the page: spoken stories carry setup and repetition that drag in print, so tighten them and lead with what matters. Short paragraphs, bold used rarely, bullets only for real lists.
- **Close.** One clear takeaway and one specific thing to do today (not "spend time in prayer this week"). End on a line that lands. Skip "In conclusion."
- **Length.** About 800 to 1,200 words. If it runs long, cut; a reader who finishes is worth more than one who quits halfway.

Adapt altar-call language ("if you're ready to give your life to Jesus tonight") into an invitation that fits a reader, such as visiting the church or talking with a pastor. Use the keyword a few times where it reads naturally and nowhere it doesn't.

## Output

In chat: the recommended title with two alternatives, the meta description, the full article with H2 subheadings ready to paste into WordPress or any CMS, and a one-line SEO note naming the primary keyword and any secondary terms that came up naturally.
