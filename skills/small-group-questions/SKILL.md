---
name: small-group-questions
description: Use when creating discussion questions or a study guide from Sunday's sermon for small groups, life groups, or Bible studies.
argument-hint: "[sermon passage or summary]"
---

# Small Group Discussion Questions

Sunday's sermon becomes Monday's small group conversation.

> Before writing: follow the pastor-foundation skill and load the church profile from `~/.claude/pastor-profile.md`. If the profile file is missing, run the pastor-setup skill first.

---

## What You Need to Provide

**Required:**
- Sermon passage (book, chapter, verses)

**Helpful (any level of detail works):**
- Key points from the sermon
- The big idea or main takeaway
- A transcript, outline, or rough notes

**Optional:**
- A specific application emphasis you want reinforced
- The date of the sermon
- Your preferred Bible translation

The more context you provide, the tighter the questions will track the actual sermon. A passage alone is enough to generate solid questions, but sermon notes produce a guide that feels like a direct extension of Sunday.

---

## Step 1: Extract the Core

Before writing a single question, identify:

1. **The Big Idea.** One sentence. What was the sermon ultimately about? Not the topic, the point. "God is faithful" is a topic. "God's faithfulness in the wilderness is the reason you can trust him in yours" is a big idea.
2. **2-3 Key Themes.** The threads the pastor kept returning to. These anchor the interpretation questions.
3. **The Primary Application.** What did the pastor call people to do, believe, or change?

Questions reinforce the sermon. They do not go on interesting tangents the passage could support. If the pastor preached on forgiveness and didn't touch on justice, don't write a question about justice. Stay in the lane the sermon opened.

---

## Step 2: Generate the Discussion Guide

Produce the complete guide in this format:

---

## Small Group Discussion Guide

**Week of:** [date if provided, otherwise leave blank]
**Passage:** [passage reference]
**Big Idea:** [one sentence distilled from the sermon]

---

**Icebreaker** (leader picks one)

- [Option A: lighter or fun. Something anyone can answer without knowing the Bible or having attended the service. Draws people in before the conversation gets serious.]
- [Option B: slightly more reflective. Still accessible, but begins to open the emotional or experiential door toward the sermon topic.]

---

**Read the Passage Together**

[Passage reference. Use the pastor's preferred translation if known. Default to NIV.]

---

**Observation Questions** (what does the text say?)

1. [A question grounded in what's literally on the page. Characters, sequence, key words, repeated phrases. Anyone who just read the passage can answer this.]
2. [Something easy to miss on a first read. A detail, a phrase, a shift in tone that most people skip over. Builds careful reading habits without requiring commentary.]

---

**Interpretation Questions** (what does the text mean?)

3. [Why the author made a specific choice: word selection, structure, who he addressed. Moves from observation into meaning.]
4. [Cultural, historical, or linguistic context that changes or deepens the meaning. Keep it accessible, not academic. "In that culture, this meant..." style.]
5. [How this passage connects to the larger biblical story. A thread to another text, a theme that runs through Scripture, or how this moment fits the redemption arc.]

---

**Application Questions** (what do we do about it?)

6. [Personal without being invasive. Invites honest reflection without requiring public confession. "Where do you find yourself in this story?" style.]
7. [Connects the passage to daily life: work, family, relationships, finances, parenting. Makes the Bible feel relevant to Tuesday morning, not just Sunday.]
8. [Challenges comfort or issues a call to action. This one should have some edge. Not harsh, but not soft either. The sermon made a demand. This question reinforces it.]

---

**Going Deeper** (for groups that want more)

9. [A cross-reference question that connects this passage to another text. "How does [X passage] add to or challenge what we read here?" Give the reference. Don't make them hunt for it.]
10. [A theological question with guardrails. Opens a real doctrinal or philosophical question the passage raises, but frames it in a way that keeps the conversation grounded. Not "do you believe in predestination?" but "what does this text tell us about how God initiates relationship with people?"]

---

**Closing**

- **Prayer prompt:** [Specific direction based on the sermon theme. Not "pray for each other." Something like: "Spend a few minutes praying specifically about the area where this week's passage challenged you most. Ask God for the courage to act on what you heard, not just to think about it."]
- **Optional challenge:** [One small, concrete action step for the week. Specific enough to be doable. Vague enough that it applies to different life situations. Something a group member could report back on next week.]

---

## Design Rules

**Volume:** 8-10 questions total, never more. Groups have 60-90 minutes. Every question should earn its place or get cut.

**Flow:** Observation to Interpretation to Application. This is the inductive Bible study method. It works because it follows how understanding actually develops: see it, understand it, apply it. Never start with application. Groups that start with "what should we do?" skip the work of actually understanding what the text says.

**Question type:** Open-ended only. Never yes/no. If the question can be answered with one word, rewrite it.

**Application:** Specific to real life situations. Not theological abstraction. "How does this passage inform how you respond to a difficult coworker?" beats "How should Christians handle conflict?" every time.

**Icebreakers:** Always provide two options. Different groups have different cultures. A men's group at 6 AM and a couples' group on Thursday night need different entry points.

**Translation note:** Include the passage reference in the guide. Do not print out the full text. Groups should open their Bibles. That habit matters.

---

## Anti-Patterns

These are the ways small group guides go wrong. Avoid all of them.

**Writing for seminary students.** If a question requires knowing Greek, having read multiple commentaries, or understanding 2nd Temple Judaism to engage meaningfully, cut it or rewrite it. Questions serve the group, not the pastor's library.

**Leading questions with one right answer.** "Don't you think God was testing Abraham's faith here?" is not a discussion question. It's a quiz with pressure attached. Write questions that genuinely invite different responses.

**Feelings-only questions.** "How did this passage make you feel?" on repeat is not Bible study. It's group therapy with a Bible on the table. Feelings are one lane. The observation and interpretation questions keep the group in the text.

**Assuming everyone heard the sermon.** Some group members skip Sunday. Others zone out. Others attend a different service and haven't seen the notes. Every question should work on its own. The guide should function as a standalone document even if someone walks in cold with only their Bible.

**Generic closing prayers.** "Pray for each other's needs" is what groups do when the guide ran out of ideas. The prayer prompt should connect directly to what the passage demanded. If the sermon was about surrender, the closing prayer should be about surrender. Specific. Not generic.

**Too many application questions.** Application is the goal, but three application questions is the limit. More than that and the group starts feeling like a confession booth. Let the text do the work in the observation and interpretation phases. The application questions land harder when they're earned.

---

## Output Quality Check

Before delivering the guide, verify:

- The Big Idea is one sentence and comes from the sermon, not from a general theme the passage could support
- All 10 questions are open-ended: no question can be answered yes or no
- The three sections flow in order: observation, interpretation, application
- At least one application question connects to daily work, family, or relationships (not just spiritual life)
- The prayer prompt is specific to the sermon theme, not generic
- The optional challenge is a concrete action step, not a vague encouragement
- No em dashes anywhere in the document
- Total question count is 10 or fewer

---

## PDF Output

The final output is a formatted, REACHRIGHT-branded PDF, not terminal text. Requires `reportlab` (`pip install reportlab`).

### Process

1. Generate the discussion guide using the steps above.
2. Assemble the structured data into the JSON schema below.
3. Write a temporary JSON file matching the schema.
4. Run `generate-pdf.py` with the JSON file to produce the PDF.
5. Return the PDF path to the pastor.

### JSON Schema

```json
{
  "passage": "Romans 8:1-11",
  "date": "April 13, 2026",
  "translation": "ESV",
  "pastor_name": "PASTOR_NAME from foundation",
  "church_name": "CHURCH_NAME from foundation",
  "big_idea": "One sentence distilled from the sermon.",
  "icebreakers": ["Option A", "Option B"],
  "observation_questions": ["Q1", "Q2"],
  "interpretation_questions": ["Q3", "Q4", "Q5"],
  "application_questions": ["Q6", "Q7", "Q8"],
  "going_deeper_questions": ["Q9", "Q10"],
  "prayer_prompt": "Specific prayer direction.",
  "optional_challenge": "One concrete action step."
}
```

**Notes:** `icebreakers` always has exactly 2 entries. Question counts follow the guide structure: 2 observation + 3 interpretation + 3 application + 2 going deeper = 10 total. `pastor_name` and `church_name` come from the pastor-foundation skill. No em dashes anywhere in the content.
