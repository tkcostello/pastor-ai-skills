---
name: sermon-research
description: Use when studying a scripture passage for preaching or teaching: commentary insights, historical and cultural context, original language notes, and cross-references. Research only, never sermon writing.
argument-hint: "[passage]"
---

# Sermon Research Assistant

Go deeper into the text so you can preach with confidence.

> Before writing: follow the pastor-foundation skill and load the church profile from `~/.claude/pastor-profile.md`. If the profile file is missing, run the pastor-setup skill first.

---

## What You Need to Provide

Give me the scripture passage you are preaching. That is the only required input. Everything else helps me go deeper, but you do not need it all to get started.

| Input | Required | Notes |
|---|---|---|
| Scripture passage | Yes | Book, chapter, verse range (e.g., Romans 8:1-11) |
| Topic or angle | No | The lens you are preaching through, if you already have one |
| Series context | No | What the larger series is, where this week falls |
| Questions you are wrestling with | No | Interpretive questions, tension points, things you are unsure about |

If all you have is a passage, that is enough. I will not ask you five follow-up questions before starting. Give me what you have and I will get to work.

---

## Research Workflow

### Step 1: Passage Context

Every passage lives somewhere. Before you can preach it well, you need to know where you are standing.

This section covers:

- **Book overview.** Who wrote it, when, and to whom. The historical situation of the author.
- **Audience.** What was the original community dealing with? What were they expecting, fearing, or celebrating?
- **Literary genre.** Is this epistle, narrative, poetry, apocalyptic, wisdom literature? The genre shapes how the passage works and what kind of demands it makes on the reader.
- **Placement in the book.** Where does this passage fall in the larger argument or story? What just happened? What comes next? Knowing the surrounding material keeps you from making the text say something the author never intended.

Length: 2-3 paragraphs. Enough to orient you, not enough to overwhelm you.

---

### Step 2: Historical and Cultural Background

The Bible was written in specific times and places. Modern readers bring 2,000 years of cultural distance to the text without realizing it. This step closes that gap.

This section covers:

- **Political and social realities.** Who held power? What was daily life like for ordinary people in this culture?
- **Religious context.** What did Jewish law, Roman religion, or local pagan practice look like on the ground? What assumptions did first-century people carry that shape the passage?
- **Cultural practices.** Hospitality, honor and shame, patron-client relationships, purity laws, agricultural cycles: these details are not trivia. They are the air the original audience breathed.
- **What modern readers miss.** I will flag two or three specific details that a contemporary reader would read past but that the original audience would have caught immediately.

Length: 2-3 paragraphs. Dense and specific, not a general history lesson.

---

### Step 3: Key Word Study

Not every word needs a word study. Some do. This step identifies 3-5 words in your passage that carry significant theological weight, have a range of meaning that matters for interpretation, or are translated inconsistently across major Bible versions.

For each word, I will provide:

| Column | What It Shows |
|---|---|
| English word | As it appears in the text |
| Transliteration | Phonetic spelling of the Hebrew or Greek |
| Literal meaning | Root definition |
| Range of meaning | How the word is used elsewhere in Scripture |
| Translation comparison | How NIV, ESV, KJV, NLT, and NASB handle it differently |

The point is not to make you look smart for knowing Greek. The point is to hand you the tools to make a better interpretive decision and explain it clearly to your congregation without a seminary lecture.

---

### Step 4: Commentary Insights

Commentaries are not the final word, but they are how you get two thousand years of careful thinkers into your study before Sunday. This step surfaces what major commentators say about the passage.

I will draw from 3-5 commentators or theological traditions, covering:

- The main interpretive question in the passage and how different scholars land on it.
- Where commentators agree. Widespread agreement is a signal worth noting.
- Where they diverge. Disagreement usually marks a genuine tension in the text, not just a matter of preference.
- Academic and pastoral perspectives. Technical commentaries ask different questions than preaching commentaries. Both are useful.

I will name the commentators I am drawing from. I will not fabricate quotes. I will summarize their positions accurately. If a passage is interpretively contested, I will tell you that directly rather than picking a side for you.

See `references/commentary-sources.md` for the full list of sources this skill draws on, with descriptions and access information.

---

### Step 5: Cross-References and Parallel Passages

Scripture interprets scripture. This step gives you 5-8 related passages with a clear note on how each one connects to your text.

For each cross-reference, I will provide:

- **Reference.** Book, chapter, and verse.
- **Connection.** One sentence on why it matters for your passage.
- **Connection type.** One of three categories:
  - *Direct parallel:* Same event or teaching from a different angle.
  - *Thematic connection:* A passage that develops the same theological idea.
  - *OT background:* An Old Testament text that your New Testament passage quotes, alludes to, or assumes the reader knows.

This is not a list for its own sake. Each reference is there because it does something useful: sheds light on an ambiguous word, shows how the theme develops across the canon, or gives you a second angle into the same truth.

---

### Step 6: Theological Themes

Most passages carry more than one theological idea. This step names the 3-5 major themes in your text and connects each one to the world your congregation actually lives in.

For each theme, I will provide:

- **Name.** A short, clear label for the theme.
- **How it appears in the text.** Where and how the passage develops this idea. Specific, not general.
- **One practical implication.** How this theological reality might land for a congregation of 100-300 people in a local church context. What question does it answer? What fear does it address? What obedience does it call for?

This section is not a sermon outline. It is a map of the theological terrain. What you do with that terrain is your job.

---

### Step 7: Thinking Prompts

Good preaching is not just about knowing what the text says. It is about knowing what your congregation will do with it, where they will get stuck, and what assumptions they are carrying into the room.

These 5-7 questions are designed to push your thinking before you touch a single outline or illustration. They are not sermon structure questions. They are interpretive pressure tests.

Examples of the kind of questions this section asks:

- What assumption might your congregation bring to this text that the original audience would not have had?
- Where is the natural application of this passage too easy? Where might it be harder than it looks?
- What does this passage demand that your congregation probably does not want to hear?
- If your congregation walks out feeling good about this sermon, did you preach the whole text?
- What is the most common way this passage is mishandled from the pulpit, and how do you avoid it?

The questions will be tailored to your specific passage, not pulled from a generic list.

---

## Output Format

This skill outputs a formatted PDF document, not terminal text. The PDF includes styled headers, formatted tables for word studies, structured lists for cross-references, and clean typography designed for reading and markup on screen or in print.

### Requirements

The PDF generator requires Python and the `reportlab` library. If reportlab is not installed, install it before generating:

```
pip install reportlab
```

### How It Works

After completing all seven research steps, do the following:

1. **Write a JSON file** containing the structured research data. Save it as a temporary file (e.g., `sermon-research-temp.json`) in the current working directory.
2. **Locate `generate-pdf.py`** in the same directory as this skill file. Search skill directories if needed.
3. **Run the script:** `python generate-pdf.py sermon-research-temp.json`
4. **Delete the temporary JSON file** after the PDF generates successfully.
5. **Tell the pastor** the PDF filename and where it was saved.

The PDF saves to the current working directory with a filename based on the passage (e.g., `Sermon-Research-Romans-8-1-11.pdf`).

### JSON Data Structure

Structure the research into this exact format before generating the PDF. Every field maps to a section in the document.

```json
{
  "passage": "Romans 8:1-11",
  "date": "2026-04-08",
  "pastor_name": "PASTOR_NAME from foundation",
  "church_name": "CHURCH_NAME from foundation",
  "passage_context": "Full text of the Passage Context section. Use double line breaks to separate paragraphs.",
  "historical_background": "Full text of the Historical and Cultural Background section. Use double line breaks to separate paragraphs.",
  "word_studies": [
    {
      "english": "condemnation",
      "transliteration": "katakrima",
      "literal_meaning": "adverse sentence, punishment following a guilty verdict",
      "range_of_meaning": "Used 3 times in the NT, all in Romans. Refers to the sentence itself, not the act of judging.",
      "translations": {
        "NIV": "condemnation",
        "ESV": "condemnation",
        "KJV": "condemnation",
        "NLT": "condemnation",
        "NASB": "condemnation"
      }
    }
  ],
  "commentary_insights": "Full text of the Commentary Insights section. Use double line breaks to separate paragraphs.",
  "cross_references": [
    {
      "reference": "Galatians 5:16-25",
      "connection": "Paul's parallel treatment of life in the Spirit versus life in the flesh.",
      "type": "Thematic connection"
    }
  ],
  "theological_themes": [
    {
      "name": "Freedom from condemnation",
      "in_text": "Opens the passage with the declaration that there is now no condemnation for those in Christ Jesus.",
      "implication": "For a congregation carrying guilt from past failures, this is not abstract theology. It is the ground they stand on."
    }
  ],
  "thinking_prompts": [
    "What assumption might your congregation bring to this text that the original audience would not have had?",
    "Where is the natural application of this passage too easy?"
  ]
}
```

**Important notes on the JSON:**
- `passage_context`, `historical_background`, and `commentary_insights` are plain text strings. Separate paragraphs with double newlines (`\n\n`).
- `word_studies` is an array of objects. Include 3-5 entries matching the words identified in Step 3.
- `cross_references` uses three type values: "Direct parallel", "Thematic connection", or "OT background".
- `theological_themes` is an array of 3-5 theme objects.
- `thinking_prompts` is an array of 5-7 question strings.
- Use the pastor's real name and church name from the foundation variables, not placeholders.
- Do not use em dashes anywhere in the content. Use commas, colons, or periods instead.

---

## Anti-Patterns

This skill will not do the following, even if you ask:

- **No sermon outline or structure.** Research is research. Structure comes in your prep, not here.
- **No three-point frameworks.** The AI will not suggest how to organize the sermon.
- **No fabricated quotes.** If a commentator's exact words are not available, the AI summarizes the position. It does not invent a quotation to make a point sound more authoritative.
- **No over-spiritualized history.** The Roman census was a political act. The Temple Mount was a real place with real economic activity. Historical context is not a metaphor. This skill reads it plainly before asking what it means theologically.

---

## Why This Exists

Most pastors do not have a seminary library, a research assistant, or three hours to spend in commentaries before a busy week. This skill does not replace deep personal study. It compresses the front end of that study so you spend your time thinking and praying, not hunting down background information you already know you need.

The work of applying the text to your congregation's life belongs to you. The Holy Spirit works through that process. What this skill does is make sure you are not preaching on insufficient information about what the text actually says.

---

**Why this works:** Separating research from structure keeps you from locking into a sermon shape too early. Pastors who research and outline in the same step often end up preaching what they already believed rather than what the text demands.
