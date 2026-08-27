---
name: sermon-to-blog
description: Use when turning a preached sermon (transcript or notes) into a standalone blog post for the church website.
argument-hint: "[paste transcript or notes]"
---

# Sermon to Blog Post

**Preach it once, publish it forever.**

> Before writing: follow the pastor-foundation skill and load the church profile from `~/.claude/pastor-profile.md`. If the profile file is missing, run the pastor-setup skill first.

---

## What This Skill Does

You preached a sermon. Maybe it was great. Maybe it was the best thing you've said from the pulpit all year. And now it's sitting in a folder somewhere as a transcript or a set of notes, doing nothing for the people who weren't in the room.

This skill turns that sermon into a standalone, web-ready blog post that works for someone who has never heard you preach. Not a transcript dump. Not a summary. A real article, structured for reading, optimized for search, and written in your voice.

---

## Input

Provide one of the following:

- Full sermon transcript (preferred)
- Recording notes or detailed outline with key points and illustrations
- Bullet points covering the main ideas, scripture references, and any stories you told

**Optional but helpful:** A target keyword or topic angle for SEO (e.g., "how to overcome anxiety as a Christian" or "what the Bible says about forgiveness").

If you don't provide a keyword, one will be identified from the sermon content.

---

## Workflow

### Step 1: Extract the Core Message

Before writing a single word of the post, identify:

- **The big idea.** One sentence. What is this sermon actually about? Not the title, not the passage. The transferable truth.
- **The strongest illustration.** One story, analogy, or real-world example from the sermon that will translate well to reading (not all illustrations work the same way in print).
- **The 3-4 most practical takeaways.** What can someone actually do, think differently about, or believe differently because of this content?
- **The primary scripture.** The passage the whole message hangs on.

This step determines the structure. A blog post is not a transcript. It is a distilled, restructured version of the sermon's best content, rebuilt for a reader who is skimming on a phone at 7am.

---

### Step 2: Write the Blog Post

Produce all three components below. No placeholders. Complete, polished output.

---

#### Title

- SEO-friendly and compelling
- Under 60 characters
- Functions as both a search result and a social share
- Includes the primary keyword naturally
- Generate 2-3 options and recommend one

**Examples of strong titles:**
- "How to Stop Worrying When Life Falls Apart"
- "What Jesus Actually Said About Anxiety"
- "3 Things the Bible Says About Trusting God in Hard Times"

**Avoid:**
- Vague sermon titles that mean nothing outside the church walls ("The Anchor Holds," "Week 3: Going Deeper")
- Clickbait that overpromises
- Titles over 60 characters

---

#### Meta Description

- 140-160 characters
- Summarizes the value of the article for someone seeing it in a search result
- Includes the primary keyword naturally, not forced
- Reads like a human wrote it, not a checklist item

---

#### Body: 800-1200 words

Structure the article as follows:

**Opening Hook (no heading, 2-3 sentences)**

Draw in a reader who did NOT hear the sermon. Use relatable tension, a pointed question, or a surprising statement. Meet them where they actually are.

Do not open with:
- "Last Sunday I preached about..."
- "In this blog post, we will explore..."
- A block of scripture
- The sermon title

The hook earns the right to be read. It should make a reader think: "Yes. That's exactly where I am."

---

**Body Sections (3-4 sections, each with an H2 subheading)**

Each section covers one key point from the sermon. The subheadings should be scannable and meaningful, not decorators.

Guidelines for each section:
- 150-250 words
- Weave in scripture naturally. Do not block-quote every other paragraph. Reference it, quote a phrase, let it breathe.
- Use the sermon's language and illustrations, adapted for reading. A story told out loud has different pacing than one told on the page. Tighten it. Cut the setup. Lead with what matters.
- Keep paragraphs short: 2-3 sentences. White space is your friend.
- Bold only what is genuinely worth emphasizing. Not every sentence. Sparingly.
- Use bullet points only for actual lists, not to fake structure.

---

**Closing (no "In Conclusion" or "As We Wrap Up")**

- 100-150 words
- Clear single takeaway: what should the reader walk away believing or doing?
- One concrete action step. Specific. Not "spend time in prayer this week." Something they can actually do today.
- End with strength. Not a fade. Not a hedge. A statement or a question that lands.

---

## Anti-Patterns

These are hard stops. None of these belong in a published blog post:

- **"In this blog post, we'll explore..."** -- Never. Cut it.
- **Altar-call language** -- "If you're ready to give your life to Jesus tonight..." belongs in a sermon, not a blog post. Adapt it or cut it.
- **Transcript sections** -- Do not paste long chunks of what was said verbatim. Restructure for reading.
- **Keyword stuffing** -- One primary keyword. Use it 3-5 times naturally. Do not force it into every paragraph or subheading.
- **Exceeding 1200 words** -- If you are over 1200 words, cut. Tighter is better. A reader who makes it to the end is worth more than one who gets halfway.
- **Weak openings** -- If the first line would not stop a scroll, rewrite it.
- **Em dashes** -- Do not use em dashes. Use a period, comma, or colon instead.

---

## Output Format

Deliver the following, in order:

1. **Recommended title** (with 2 alternatives below it)
2. **Meta description**
3. **Full article body** (formatted with H2 subheadings, ready to paste into WordPress or any CMS)
4. **SEO notes:** primary keyword identified, estimated keyword density, any secondary keywords naturally present

---

## Quality Check

Before presenting the output, verify:

- [ ] Opening hook does not reference the sermon, the service, or the pastor's name
- [ ] Word count is between 800 and 1200
- [ ] No em dashes used anywhere
- [ ] Scripture is woven in, not block-quoted throughout
- [ ] Paragraphs are 2-3 sentences max
- [ ] Subheadings are present every 200-300 words
- [ ] Closing has a clear action step
- [ ] No altar-call language
- [ ] Title is under 60 characters
- [ ] Meta description is 140-160 characters
- [ ] No filler phrases ("In this post...", "As we wrap up...", "In conclusion...")

If the output fails any of these checks, revise before presenting.
