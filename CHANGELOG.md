# Changelog

## 2.1.0 (November 2026)

Rebuilt for current Claude models. Newer models already know how to write a clear email or a tight social post. They need your church's context, your tradition, and a few guardrails. The skills now carry that and very little else. Then every skill was test-driven against real requests from three kinds of churches, and the weak spots were fixed.

### Four new skills

- **`/sunday-to-week`**: paste one sermon transcript and get the whole week back (small group guide, midweek devotional, email recap, social posts, YouTube package, blog post). It pulls the big idea, the quotable lines and the clip once, so every piece says the same thing.
- **`/sermon-feedback`**: an honest read of your own manuscript, outline or transcript. It says back the big idea it heard, checks it against the text, finds where attention drops, and ranks the three changes that would help most. It coaches; it never rewrites.
- **`/funeral-prep`**: family meeting questions, an order of service for your tradition, readings, a life sketch built only from what the family told you, a message brief, a logistics checklist and a follow-up care plan. Ask for one piece when it's short notice.
- **`/wedding-prep`**: questions for the couple, ceremony order, vow options, readings, a message brief, a rehearsal run sheet and officiant notes.

### Fixes from the test drive

- **Your role and your polity.** Executive and associate pastors now write in their own voice, with the lead pastor's news coming from the lead pastor. Setup asks who makes the big decisions (elders, deacons, a congregational vote) and for your website and giving link. Letters about staffing or discipline can come from the board.
- **Scripture wording.** Skills quote verse text only when they're sure of its exact wording in your translation, and mark the rest `[verify wording]`. Word studies no longer list five translations from memory.
- **Protecting people.** Nothing names someone's illness or grief publicly without noting it needs their consent. Anything that may involve harm to a minor points to mandatory reporting first.
- **Church calendar.** Each tradition preset now knows its calendar (Pentecost Sunday, Reformation Sunday, Sanctity of Human Life Sunday, Lottie Moon, and more), plus the Sundays when guests come and attendance dips. Sermon series plans now use real dates.
- **Sermon prep.** The brainstorm now asks what the author is actually claiming before it settles on a big idea, and offers options when you're stuck. Research answers your specific question first, ends with a short "verify before Sunday" list, and on contested passages lays out the views and then says where your tradition usually lands. Small group guides add leader notes and care for hard passages.
- **Communication.** Emails keep extra items in an "Also this week" list instead of dropping them. Announcement scripts give a death or birth in the church family a line from the stage. Letters handle a moral failure plainly without details. Board agendas get a consent agenda, safety items first, and confidential items in an elders-only executive session. Devotionals know how to speak after a local tragedy.
- **Video and social.** YouTube chapters never print a guessed timestamp. Clips come with exact first and last lines, a hook and captions, and a warning about worship songs and streaming licenses. Social posts default to Facebook and Instagram, cover an event with a run of three posts, and include alt text and image sizes. The calendar adds a weekly vertical video, a Sunday shot list and an owner for each post. Blog posts are written in the pastor's first person, with a slug and an image idea.
- **No more REACHRIGHT branding on PDFs.** The footer now shows your church's name and the page number.

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
