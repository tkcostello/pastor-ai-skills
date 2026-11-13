---
name: church-letter
description: Writes formal letters from the pastor to the congregation or a group, from welcome letters and building updates to leadership transitions, staff departures and hard news. Use when the pastor says "I need to tell the church our worship pastor is leaving", "write a letter about the building closing for repairs", "welcome letter for new members", "help me explain the new childcare policy", or "a letter to the church about our finances".
argument-hint: "[occasion]"
---

# Church Letter

The right words for the hard letters and the good ones.

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

The occasion, the key facts (what happened, what's changing, what readers need to know) and the audience: the whole church, a group like volunteers or small group leaders, or one person. Useful extras: tone guidance, anything that should stay off the page, and whether it will be printed, emailed or both.

## Match the letter to the occasion

| Letter | Tone | Length |
|---|---|---|
| Welcome or celebration | Warm, upbeat | 200-300 words |
| Facility or logistics update | Clear, positive | 150-250 words |
| Leadership transition | Honest, hopeful, pastoral | 300-500 words |
| Staff departure | Careful, gracious, brief | 200-300 words |
| Policy change | Clear, empathetic, firm | 250-400 words |
| Financial update or need | Transparent, specific, hopeful | 300-400 words |
| Crisis or difficult news | Pastoral, steady | 300-500 words |

If it's a blend, say which blend you're using.

## What a good letter does

People save a pastor's letters, reread them and quote them months later, so write it to be received clearly and trusted.

- **Open with the relationship, not the news.** The congregation isn't a memo list. "Before Sunday, I wanted you to hear this from me." Skip "I am writing to inform you" and "It is with a heavy heart," which reads as theater.
- **State the facts plainly.** What is happening, when, who's affected, what you're doing about it. If someone is leaving, say they're leaving; "some adjustments to our leadership structure" tells no one anything. People fill vague gaps with their worst assumptions.
- **Name what readers will feel,** in a sentence or two, because people feel news before they process it. "I know this raises questions. Here is what I can tell you right now."
- **Give a clear next step:** the timeline, who to contact, when the next update or gathering is, where to give. If there's nothing to do, say so: "You don't need to do anything. I just wanted you to hear this from me."
- **Close with pastoral warmth** they'll remember: a real prayer, a blessing, confidence in the church. Not a throwaway "God bless," and not a reflective question; a letter isn't a small group.

Date it, address it the way the church does ("Dear Grace Family,"), and sign with the pastor's name and title. In churches led by elders or a session, letters about discipline, staff or major decisions often come from the board: ask, and if so sign it from the board (for example, "The Session of Grace Church"), with the pastor as moderator if that's their practice.

## Hard letters

For staff departures, leadership transitions, crises and personnel-related policy changes:

- Assign no blame, in the lines or between them. If a departure wasn't mutual, that still stays out of writing.
- State the decision, give enough context to understand it, and stop. Paragraphs defending the choice read as defensive and usually backfire.
- Answer the most important question, acknowledge others exist, and point people to where they can ask. Pre-answering every objection bloats the letter.
- Leave out specific complaints, incidents, violations and terms of separation.
- For a confessed moral failure, name the category plainly ("an inappropriate relationship with another adult") and give no details. Silence about why fuels the rumors; details wound the people involved. Don't name anyone else involved.
- If the situation carries legal exposure (a termination, an accusation, liability), flag it and recommend counsel before anything goes out in writing.

## Output

Give the letter in chat. Under it, add one sentence on what the letter communicates (for the pastor, not to send) and any flags: legal review, or a conversation that should happen in person before or after it goes out. For sensitive letters, offer an alternate closing paragraph in a second tone.

If the pastor asks for a PDF or printed letterhead copy, follow `references/pdf.md`.
