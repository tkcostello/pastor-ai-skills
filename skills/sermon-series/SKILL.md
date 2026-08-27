---
name: sermon-series
description: Use when planning a multi-week sermon series from a theme, book of the Bible, or church season, or when mapping the preaching calendar months ahead.
argument-hint: "[theme or book] [number of weeks]"
---

# Sermon Series Planner

Map out your next series so every week builds on the last.

> Before writing: follow the pastor-foundation skill and load the church profile from `~/.claude/pastor-profile.md`. If the profile file is missing, run the pastor-setup skill first.

---

## What You'll Provide

To build your series, give me:

- **Theme, topic, or book of the Bible** (e.g., "the book of James," "anxiety," "what it means to follow Jesus")
- **Number of weeks**, or say "suggest a length" and I'll recommend one
- **Any constraints**: things like "Easter lands on week 4," "end with a giving emphasis," "we have a guest preacher on week 2," or "keep it accessible for seekers"

If you don't have constraints, just give me the theme and weeks. I'll take it from there.

---

## Step 1: Understand the Scope

Before building anything, I'll assess what you're working with.

**If you're preaching a book of the Bible:**
- Is the whole book teachable in your timeframe, or does it need to be a focused portion?
- Some books (Philippians, James, Ruth) fit naturally into 4-6 weeks. Others (Romans, Genesis) need a curated selection or a multi-series approach.
- I'll flag if the number of weeks is too ambitious or too shallow for the material.

**If you're preaching a theme:**
- I'll identify the 4-8 strongest passages that anchor the topic biblically.
- I'll avoid the temptation to chase every verse. The best thematic series has a clear through-line, not a concordance dump.
- Themes that are too broad (e.g., "faith") need to be narrowed. I'll help you find the angle.

**Output of this step:** A brief scope assessment. One paragraph. If the premise needs adjustment, I'll say so before building the full plan.

---

## Step 2: Three Series Title Options

I'll generate exactly three title options. Not five. Not eight. Three, done well.

Each title will be:
- Memorable and 2-4 words
- Functional on a banner, social graphic, or bulletin header
- Free of worn-out church series names ("Unshakeable," "Breakthrough," "Reset," "Anchored," "Deep Dive," "Level Up")
- A pun only if it's actually good. Forced wordplay is worse than no wordplay.

For each title, I'll include a one-sentence tagline that could live under it on a graphic or in promotional copy.

**Example format:**

| Title | Tagline |
|---|---|
| **Carried** | What it looks like when God does the heavy lifting. |
| **Hold Fast** | Staying grounded when everything around you shifts. |
| **All of It** | Surrendering the parts of your life you're still holding back. |

You pick one. Or tell me the direction feels off and we'll go again.

---

## Step 3: Weekly Breakdown

The core deliverable. A full table showing every week of the series.

| Week | Sermon Title | Scripture Passage | Big Idea | Connective Thread |
|---|---|---|---|---|
| 1 | ... | ... | One sentence core truth | How this week sets up week 2 |
| 2 | ... | ... | One sentence core truth | How this follows week 1, sets up week 3 |
| ... | | | | |

**What goes in each column:**

- **Sermon Title:** Compelling, not just a passage summary. "Faith That Works" is better than "James Chapter 2." It should make someone want to be in the room.
- **Scripture Passage:** Primary text. If there are supporting passages, I'll note them but keep the main reference clean.
- **Big Idea:** One sentence. Not a topic. A claim. "God's grace isn't just undeserved, it's unconditional" is a big idea. "We're talking about grace" is not.
- **Connective Thread:** What makes this a series and not just a collection of sermons. Each week should land on its own and also pull the listener toward the next week. I'll write a brief note on how each sermon connects to what came before and what comes next.

The arc should build. Week 1 establishes tension or sets a premise. The middle weeks develop it. The final week lands with weight. If the strongest content is in week 2 and the series fizzles from there, we've got a problem. I'll flag that if I see it.

---

## Step 4: Series Arc

After the table, a 2-3 sentence summary of the emotional and theological arc.

This is the narrative skeleton. Where does the series start emotionally? Where does it build? Where does it land?

A good series takes people somewhere. It doesn't just cover ground. If someone attends every week, they should feel like they traveled a distance, not just received information. I'll describe that journey in plain language so you can use it in your elder meetings, your promo copy, and your own head as you prepare.

---

## Step 5: Practical Notes

A few quick assessments before you go build it:

**Duration check.** Is this series the right length? Congregational attention on a single series typically holds well through 6 weeks and drops meaningfully after 8. If you've asked for a 10-week series on a theme, I'll tell you. If 4 weeks feels like you're rushing rich material, I'll say that too.

**Weeks needing special attention.** I'll flag any week that's likely to be emotionally heavy (grief, sin, money, sexuality), theologically complex, or a natural visitor spike (Easter, Christmas, a community event). Those weeks may need extra prep, different framing, or a pastoral sensitivity note.

**Series launch recommendation.** One sentence on how to open strong. Options include: a teaser week the Sunday before the series starts, a cold open into the first week with no announcement, or a pre-series event or mailer. I'll give you my read on what fits your material.

---

## Anti-Patterns I Avoid

These are the series planning mistakes I won't make, and will push back on if I see them emerging:

- Generating 8 title options when you only need to make one decision. Three is enough.
- Making every sermon title follow the same formula (all one-word titles, all questions, all alliterative). Formulaic title patterns draw attention to the formula.
- Front-loading the best content. Week 1 needs to be strong enough to hook, but the best sermon should be near the end. Build to it.
- Planning series longer than 8 weeks unless you explicitly ask. Attention drops. Even great series lose momentum.
- Confusing "a lot of passages" with "a strong series." One clear passage per week, preached well, beats three passages skimmed.
- Vague big ideas. If the big idea could apply to 40 different sermons, it's not a big idea yet.

---

## How to Use This

Paste your request in plain language:

> "I want to do a 5-week series on the Sermon on the Mount. We're going through a season of transition as a church, and I want it to feel grounding and hopeful. No major holidays in the window."

> "Book of Ruth, 4 weeks, women's ministry emphasis but it's a whole-church series."

> "Something on prayer. I'm not sure how long. Suggest a length. We want to use it as a fall launch series."

I'll take it from there and return the full plan: scope assessment, three title options, weekly breakdown table, series arc, and practical notes.

---

## Output Format

This skill outputs a formatted PDF document, not terminal text. The PDF includes a branded title banner, formatted tables for title options and weekly breakdown, structured sections for scope assessment, series arc, and practical notes, and clean typography designed for reading and markup on screen or in print.

### Requirements

The PDF generator requires Python and the `reportlab` library. If reportlab is not installed, install it before generating:

```
pip install reportlab
```

### How It Works

After completing all five planning steps, do the following:

1. **Write a JSON file** containing the structured series plan data. Save it as a temporary file (e.g., `sermon-series-temp.json`) in the current working directory.
2. **Locate `generate-pdf.py`** in the same directory as this skill file. Search skill directories if needed.
3. **Run the script:** `python generate-pdf.py sermon-series-temp.json`
4. **Delete the temporary JSON file** after the PDF generates successfully.
5. **Tell the pastor** the PDF filename and where it was saved.

The PDF saves to the current working directory with a filename based on the series title (e.g., `Sermon-Series-Hold-Fast.pdf`).

### JSON Data Structure

Structure the series plan into this exact format before generating the PDF. Every field maps to a section in the document.

```json
{
  "series_title": "Hold Fast",
  "series_tagline": "Staying grounded when everything shifts",
  "passage_or_theme": "Hebrews 10-12",
  "num_weeks": 4,
  "date": "2026-04-08",
  "pastor_name": "PASTOR_NAME from foundation",
  "church_name": "CHURCH_NAME from foundation",
  "scope_assessment": "Full text of the scope assessment paragraph.",
  "title_options": [
    {
      "title": "Hold Fast",
      "tagline": "Staying grounded when everything shifts"
    }
  ],
  "weekly_breakdown": [
    {
      "week": 1,
      "sermon_title": "The Confidence You Already Have",
      "passage": "Hebrews 10:19-25",
      "big_idea": "You have access to God that nothing can revoke.",
      "connective_thread": "Establishes the premise: we hold fast because of what Christ already did."
    }
  ],
  "series_arc": "Full text of the series arc summary.",
  "practical_notes": {
    "duration_check": "Full text of the duration check.",
    "special_attention": "Full text of the special attention notes.",
    "launch_recommendation": "Full text of the launch recommendation."
  }
}
```

**Important notes on the JSON:**
- `title_options` is an array of exactly 3 objects, each with a `title` and `tagline` string.
- `weekly_breakdown` is an array with one object per week, matching the number of weeks in the series.
- `practical_notes` is an object with three string fields: `duration_check`, `special_attention`, and `launch_recommendation`.
- Use the pastor's real name and church name from the foundation variables, not placeholders.
- Do not use em dashes anywhere in the content. Use commas, colons, or periods instead.
