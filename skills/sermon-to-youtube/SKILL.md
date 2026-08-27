---
name: sermon-to-youtube
description: Use when publishing a sermon video to YouTube: titles, description, timestamps, tags, thumbnail direction, and short-form clip selection.
argument-hint: "[sermon title + transcript]"
---

# Sermon to YouTube

**Upload your sermon so people actually find it.**

> Before writing: follow the pastor-foundation skill and load the church profile from `~/.claude/pastor-profile.md`. If the profile file is missing, run the pastor-setup skill first.

---

## What This Skill Does

You uploaded your sermon to YouTube. Maybe you titled it "Sunday Service 4/6/26" and called it a day. Maybe it's been sitting at 14 views for six months, mostly from your mom and one guy from the prayer chain.

YouTube is the second-largest search engine in the world. People search it every day for answers to the exact questions your sermon addressed. The gap between "no one finds this" and "hundreds of people find this" is not production value. It is optimization.

This skill takes your sermon title and transcript and produces a complete, ready-to-upload YouTube package: titles that rank, a description that works, tags that matter, thumbnail concepts a designer can execute, and one short-form clip worth pulling immediately.

---

## Input

Provide the following:

- **Sermon title** (working title or series title is fine, it will be improved)
- **Sermon transcript** (full preferred; partial works if it covers the key moments)
- **Optional:** Approximate sermon length in minutes (used to estimate timestamps)

If you have a YouTube channel description or your church's standard "about" text, include it. It will be used in the description's about section.

---

## Workflow

### Step 1: Analyze the Sermon

Before generating anything, read the transcript and identify:

- **Core topic.** One sentence. What question does this sermon answer, or what truth does it establish?
- **Key moments.** The 4-8 most distinct movements: opening, first major point, story/illustration, scripture exposition, application, call to action, close. These become timestamps.
- **Emotional peaks.** Where does the content hit hardest? The story that lands. The turn. The line people write down. These are short-form candidates.
- **Searchable angles.** What would someone type into YouTube to find this sermon? Think: "how to trust God when life falls apart," "what does the Bible say about anxiety," "Romans 8 explained." Not "Week 4: Anchor Series."

Write out your analysis before proceeding. This shapes everything else.

---

### Step 2: Generate the YouTube Package

Produce all five components below. No placeholders. Complete, polished output ready to copy and paste.

---

#### Title Options (3)

Each title must be:

- Under 60 characters (YouTube truncates at 60 in search results)
- Built around what the sermon answers, not what it was called internally
- Free of series names as the primary identifier
- Written for the person searching, not the person who was already in the room

Generate three options, one of each type:

1. **Search-optimized.** Keyword-forward. Starts with the topic people search. Speaks directly to the question.
   - Example: "What the Bible Actually Says About Worry"
   - Example: "How to Forgive Someone Who Hurt You Deeply"

2. **Curiosity-driven.** Hooks a browser. Creates a gap. Makes someone need to know.
   - Example: "The Verse About Fear No One Talks About"
   - Example: "Why Most Christians Get Patience Wrong"

3. **Direct and clear.** Straightforward value statement. Works well for returning subscribers who trust the channel.
   - Example: "Trusting God in Uncertain Times: A Biblical Framework"
   - Example: "Finding Peace When Life Doesn't Make Sense"

After all three, recommend one and explain why in one sentence.

**What to avoid:**
- "Romans Part 3, Sunday Sermon" -- series names with no topic signal
- "Pastor [Name] Preaches on..." -- name-first titles lose to topic-first titles in search
- Titles over 60 characters
- Titles that only make sense if you already know the series

---

#### Description (200-400 words)

Structure the description in this order:

**First 2 lines (above "Show More"):**
These are the only lines visible before someone clicks. They must earn the click. Write a compelling 1-2 sentence summary of what the viewer will get. Include the primary keyword naturally. Write for the person who found this in search, not someone who already attends.

Do not open with the pastor's name, the church name, or "Watch this sermon about..." These waste the most valuable real estate in the description.

**Timestamps (4-8 chapters):**
Format: `00:00 Chapter Title`

Use approximate timestamps based on the sermon's structure and length. Chapters improve watch time, show up in search, and help viewers navigate. Label them for content, not structure ("The Problem With Worry" beats "Introduction").

If exact timestamps are not available, estimate based on total length and transcript pacing. Note that timestamps are approximate if needed.

**About section (2-3 sentences):**
Brief, warm, third-person. Who is this pastor. What church. Where. One sentence invitation to subscribe or explore more.

**Links:**
Include placeholder lines for:
- Church website
- Social media (Facebook, Instagram)
- Giving link
- Subscribe prompt

Write these as real lines, not labels. Example: "Visit us online at [church website]" not "[INSERT WEBSITE HERE]."

**Keywords woven in:**
The description body should naturally include the primary keyword and 2-3 related terms. Do not add a keyword dump at the bottom. YouTube reads the whole description. Write for a human, not a crawler.

---

#### Tags (15-20)

Mix three types:

1. **Broad and high-volume:** "sermon," "church," "Bible study," "Christian message," "Sunday sermon," "church online"
2. **Topic-specific:** Use the actual topic, scripture passage, book of the Bible, and related search terms. Examples: "Romans 8 sermon," "suffering and faith," "trusting God," "anxiety Bible"
3. **Identity tags:** Pastor name, church name, city and state, denomination if applicable

Keep total tags between 15 and 20. YouTube's tag limit matters less than it used to, but specificity still helps in related video placement.

---

#### YouTube Category

Name the recommended category and why. Most sermons fit one of two:

- **Education:** Best for exposition-heavy sermons, Bible teaching, topical messages with practical application
- **Nonprofits and Activism:** Best for church announcement videos, generosity campaigns, community-facing content

Pick one and state the reason in one sentence.

---

#### Thumbnail Concepts (2-3 ideas)

For each concept, specify:

- **Background:** Solid color, gradient, or image (if image, describe what kind: close-up face, environmental shot, texture)
- **Text overlay:** 3-5 words. Large. High contrast. Readable on a phone screen at thumbnail size. Write the actual text, not a description of it.
- **Pastor photo:** Yes or no. If yes, placement: left side, right side, centered. Expression direction: confident, concerned, hopeful, surprised.
- **Emotional tone:** What does this thumbnail communicate before anyone reads it?

**Hard rules:**
- Maximum 5 words of text on the thumbnail. Fewer is better.
- Text must contrast with the background. Dark text on dark background is invisible at small size.
- No stock photo vibe. Thumbnails that look polished but generic get ignored.
- The text and image should work together to create curiosity or confirm relevance.

---

#### Short-Form Clip Recommendation

Identify the single best 30-60 second segment from the transcript to pull as a YouTube Short, Instagram Reel, or TikTok.

Provide:

- **Start and end timestamps** (approximate, based on transcript position)
- **Transcript excerpt:** Paste the actual words from that segment
- **Why this segment works:** 2-3 sentences. What makes it land as a standalone clip? Does it have a hook in the first 3 seconds? Does it resolve tension? Does it leave someone wanting more?
- **Suggested short-form title:** Under 50 characters. Written for short-form discovery, not the full sermon title.

A good short-form clip:
- Starts in the middle of tension, not at an introduction
- Makes a complete point or tells a complete micro-story
- Does not require the rest of the sermon to make sense
- Has a moment worth pausing on or rewatching

---

## Anti-Patterns

These are hard stops. None of these belong in the output:

- **Clickbait that misrepresents the content.** If the sermon does not answer the promise in the title, change the title.
- **"YOU WON'T BELIEVE" energy.** This is a sermon. Sensationalism kills trust with the exact audience most likely to watch.
- **More than 20 tags.** Tag bloat signals spam. Quality over quantity.
- **Transcript-dump descriptions.** The description is not the transcript. It is a sales page for the video. Write it like one.
- **Thumbnails with more than 5 words.** If you need 8 words to explain the thumbnail, the concept is not strong enough.
- **Series-name-only titles.** "Anchored: Part 5" tells a search engine nothing and convinces no one to click.
- **Em dashes.** Do not use them. Use a period, comma, or colon instead.

---

## Quality Check

Before presenting the output, verify:

- [ ] All three title options are under 60 characters
- [ ] The first 2 lines of the description stand alone without "Show More"
- [ ] Timestamps are present and labeled by content, not structure
- [ ] Tags total between 15 and 20
- [ ] No tag appears twice in different forms
- [ ] Each thumbnail concept includes background, text, photo placement, and tone
- [ ] Thumbnail text is 5 words or fewer
- [ ] Short-form clip is 30-60 seconds, has a transcript excerpt, and has a suggested title
- [ ] No em dashes used anywhere in the output
- [ ] No placeholders. All content is complete and ready to use.
