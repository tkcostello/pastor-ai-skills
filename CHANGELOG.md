# Changelog

## 2.1.0 (November 2026)

Rebuilt for current Claude models. Newer models already know how to write a clear email or a tight social post. They need your church's context, your tradition, and a few guardrails. The skills now carry that and very little else.

### Every skill stands on its own

Task skills used to depend on a separate `pastor-foundation` skill that nothing loaded automatically. When it didn't load, the guardrails and your church details went missing without any warning. Each task skill now carries a short shared block: read the church profile, write from inside your tradition, quote scripture accurately, don't invent facts, never write the sermon. The block has one source (`skills/pastor-foundation/context.md`), and `scripts/sync-context.py` copies it into every skill.

### Tradition presets

The kit used to default to "nondenominational evangelical" and stayed neutral on the Spirit's gifts, even for Pentecostal churches. `/pastor-setup` now saves a `TRADITION` alongside your denomination, and every skill writes from inside it:

- **pentecostal-charismatic**: Foursquare, Assemblies of God, Church of God, Vineyard and charismatic churches. The Spirit's gifts, prayer for healing and ministry time are normal church life.
- **reformed**: Presbyterian, Reformed and Reformed Baptist churches. Confessions, the doctrines of grace, the ordinary means of grace.
- **baptist**: Southern Baptist and other Baptist churches. Believer's baptism, congregational life, missions.
- **evangelical**: the neutral default for churches that don't lean one of those ways.

The details are in `skills/pastor-foundation/references/traditions.md`. Existing profiles keep working: skills infer the tradition from `DENOMINATION` when there's no `TRADITION` line.

### Leaner skills

- Removed the "Why this works" line every output used to end with.
- Removed the generic banned-phrase list and repeated writing advice that current models don't need.
- Removed all-caps rules and fill-in-the-blank templates. The midweek devotional's fixed five-part structure is now a short voice brief.
- Every description now lists the plain-English requests that trigger it ("write this week's devotional", "help me research Romans 8").
- `sermon-research` now states plainly that it won't invent commentary quotes or page numbers.

### PDFs are opt-in

Every skill answers in the chat by default. Ask for a PDF ("make that printable") and the eight PDF skills still produce one. The PDF instructions moved into each skill's `references/pdf.md`, so they only load when you ask.

`generate-pdf.py` now loads `pdf_utils.py` by file path instead of changing Python's import path. It finds the library in a plugin install, a full clone, or a single skill folder you copied by hand, and gives a plain message when `reportlab` or `pdf_utils.py` is missing.

## 2.0.0 (August 2026)

One-command plugin install, `/pastor-setup` with a saved church profile, and trigger-style descriptions.
