---
name: midweek-devotional
description: Use when writing a midweek devotional or a short scripture-based encouragement to send the congregation by email, app, or text between Sundays.
argument-hint: "[scripture or theme]"
---

# Midweek Devotional

A pastoral moment for the middle of the week.

> Before writing: follow the pastor-foundation skill and load the church profile from `~/.claude/pastor-profile.md`. If the profile file is missing, run the pastor-setup skill first.

---

## What You Need to Provide

**Required:**
- A verse, passage, or theme

**Optional:**
- Connection to your current sermon series
- Something happening in the community or world that's on people's minds

---

## Step 1: Write the Devotional

Use this exact structure. Every section has a purpose. Don't skip any of them.

### Opening (1-2 sentences)

Meet the reader where they are on Wednesday. Not where you wish they were.

The opening should be honest and human. Skip the greeting entirely. Drop the reader into a real moment.

What not to write: "Happy Wednesday, church family!"

What to aim for: "By Wednesday most of us have already forgotten what we committed to on Sunday. That's not failure. That's being human."

The goal is immediate recognition. The reader should think: "That's exactly where I am right now."

### Scripture (quoted in full)

Pull 1-3 verses. Not a full chapter. The whole passage should fit in a single short paragraph.

Use the pastor's preferred translation. If no preference is given, use the ESV or NIV, whichever reads more naturally for the text.

Quote it cleanly. No verse-by-verse breakdown. Let the text breathe.

### Reflection (3-5 sentences)

This is the heart of the devotional.

Write in first person. Write as a pastor who has been sitting with this text for days, not someone summarizing a commentary. What does this passage mean for THIS week, in THIS moment, for people carrying real weight?

Be specific. Vague spiritual encouragement does nothing. Anchor the reflection to something concrete: a feeling, a situation, a tension people are actually navigating.

Keep sentences short. Two to three per paragraph. Midweek readers are scanning while eating lunch or driving carpool. Make every sentence earn its place.

This section should feel like a handwritten note from someone who knows you, not a blog post from someone who needs page views.

### One Takeaway (1 sentence)

A single line the reader can carry into Thursday, Friday, and the weekend.

Practical. Memorable. Short. This is not a summary of the reflection. It is an action or a posture: something the reader can actually hold onto.

Test it: can someone repeat this sentence to a coworker without fumbling it? If not, simplify it.

### Closing (2-3 sentences)

End with a prayer or a benediction-style blessing. Not both.

A closing prayer should be direct and personal, addressed to God, written in the first person plural (we, us, our). It should feel like the pastor is praying with the reader, not at them.

A benediction should send the reader out with confidence and peace. Something they could read aloud over themselves before they close their phone.

Do not end with a sign-off like "Have a blessed week!" or "In His grace." Just let the prayer or blessing be the ending.

---

## Format Rules

- **Total length:** 200-300 words. Not a word more. Count them if needed.
- **Paragraphs:** 2-3 sentences max. No walls of text.
- **Tone:** Warm, unhurried, personal. Like a pastor texting a friend, not writing for a publication.
- **Point of view:** First person is fine. Encouraged, even. It makes the devotional feel like a real person wrote it.
- **Translation note:** If a passage reads awkwardly in the translation given, note the translation used at the bottom of the devotional in italics.

---

## Anti-Patterns

Avoid these. They will kill the devotional.

- Never exceed 300 words. Brevity is pastoral care. Long devotionals get skimmed or deleted.
- Never turn this into a sermon. One insight. One takeaway. That is enough.
- Never use the devotional to promote events, announcements, or campaigns.
- Never open with "Dear church family" or any variation of a formal greeting.
- Never close with "Have a blessed week!" It is a cliche that signals the pastor stopped thinking.
- Never write a reflection that could apply to any week of any year. Be specific to this week.
- Never quote more than 3 verses. Resist the urge to pile on more Scripture for credibility. One passage, held well, is better than five passages held loosely.

---

## Output

Deliver the devotional as a formatted PDF using `generate-pdf.py`.

No headers inside the devotional itself. No labels like "Opening:" or "Reflection:" in the final output. Those are structural guides for writing it, not formatting for the reader.

The devotional should read as one continuous piece: a short note from a pastor who cares, arriving in someone's inbox on a Wednesday morning.

If the input includes a current sermon series, weave in a single line of connection. Keep it light. Something like: "We've been talking on Sundays about..." is enough. Don't force a lecture. One thread is sufficient.

If the input includes a community event or current moment on people's minds, let it inform the opening or reflection. Ground the text in the world the reader is actually living in.

Word count check before finalizing: if it exceeds 300 words, cut from the reflection first, then the closing. The opening and takeaway are the last things to trim.

### PDF Generation

Write the devotional content to a JSON file, then run `generate-pdf.py` to produce the branded PDF.

**JSON schema:**

```json
{
  "church_name": "CHURCH_NAME from foundation",
  "date": "April 16, 2026",
  "pastor_name": "PASTOR_NAME from foundation",
  "passage_reference": "Psalm 46:10",
  "translation": "ESV",
  "scripture_text": "Be still, and know that I am God.",
  "opening": "Opening text (1-2 sentences).",
  "reflection": "Reflection text. Separate paragraphs with double newlines.",
  "takeaway": "One sentence the reader carries into the rest of the week.",
  "closing": "Prayer or benediction text."
}
```

**Field notes:**

- `church_name` and `pastor_name` come from the pastor-foundation skill.
- `reflection` uses `\n\n` to separate paragraphs.
- No section headers appear in the PDF. The layout flows as one continuous piece.
- The PDF is church-branded (no REACHRIGHT branding). Footer shows only a thin gray rule and page number.

**Usage:**

```bash
python generate-pdf.py input.json                  # output auto-named from date
python generate-pdf.py input.json devotional.pdf   # explicit output path
```
