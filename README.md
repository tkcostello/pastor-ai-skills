# Pastor AI Skills

14 AI-powered workflow tools built for pastors. Not prompts. Real multi-step skills that handle the weekly grind so you can focus on ministry.

Built for [Claude Code](https://claude.ai/code). Also works in Claude.ai Projects.

---

## About

I'm Thomas Costello. I've been in pastoral ministry for 20+ years and I run [REACHRIGHT](https://reachrightstudios.com), a church marketing agency. I built these skills for myself because I got tired of writing the same types of content every week from scratch. These are the tools I actually use.

I'm sharing them because pastors deserve better than generic AI prompts. These are workflow tools with pastoral sensitivity built in, not templates you have to heavily rewrite.

---

## Install (One Command)

Open Claude Code and run:

```
/plugin marketplace add tkcostello/pastor-ai-skills
```

Then:

```
/plugin install pastor-skills@pastor-ai-skills
```

That's it. All 14 skills, the shared foundation, and the optional PDF templates install together, and you get updates whenever this repo improves.

Then run your first skill:

```
/pastor-setup
```

It asks for your church's details once (name, your name, attendance, location, denomination, Bible translation) and saves them. Every skill uses them from then on. You never repeat yourself.

Your denomination also sets your tradition. Pentecostal and charismatic churches (Foursquare, Assemblies of God and others), Reformed churches and Baptist churches each get a preset, so the skills write from inside your tradition instead of around it. Nondenominational churches stay on broad evangelical ground unless you say otherwise.

---

## The Skills

| Skill | What it does | How often |
|---|---|---|
| **Setup** | | |
| `/pastor-setup` | One-time church profile setup. Run this first. | Once |
| **Sermon Prep** | | |
| `/sermon-research` | Deep research on a passage: commentaries, historical context, word studies, thinking prompts | Weekly |
| `/sermon-brainstorm` | Interactive brainstorm session that produces a clear sermon brief | Weekly |
| `/sermon-series` | Plan a multi-week series with titles, passages, and big ideas | Monthly |
| **Written Communication** | | |
| `/church-email` | Write the weekly church email: subject line, preview text, body | Weekly |
| `/announcement-script` | 60-90 second spoken announcement script for Sunday morning | Weekly |
| `/church-letter` | Letters for any occasion: transitions, updates, celebrations, hard news | As needed |
| **Sermon Repurposing** | | |
| `/small-group-questions` | Discussion questions from Sunday's sermon: observation, interpretation, application | Weekly |
| `/sermon-to-blog` | Turn a sermon into an 800-1200 word blog post (not a transcript) | Weekly |
| `/sermon-to-youtube` | YouTube title, description, tags, thumbnail concept, short-form clip recommendation | Weekly |
| **Social Media** | | |
| `/church-social-post` | Platform-specific posts for Facebook, Instagram, and Twitter | 3-5x/week |
| `/social-media-calendar` | A week or month of content mapped to dates and platforms | Weekly |
| **Pastoral Rhythm** | | |
| `/midweek-devotional` | 200-300 word devotional for email or app: pastoral, personal, brief | Weekly |
| `/meeting-agenda` | Structured agenda with time blocks and discussion questions | Weekly |

You don't have to remember the slash commands. Once installed, just ask in plain English ("help me research Philippians 2 for Sunday") and Claude picks the right skill.

One note on the commands: when installed as a plugin, Claude Code may show the skills with a prefix, like `/pastor-skills:church-email`. Type `/` and start typing the skill name and it will come up either way.

---

## Other Ways to Install

### Manual copy (Claude Code)

```bash
git clone https://github.com/tkcostello/pastor-ai-skills.git

# Setup saves your church profile. Foundation holds the tradition presets.
cp -r pastor-ai-skills/skills/pastor-setup ~/.claude/skills/
cp -r pastor-ai-skills/skills/pastor-foundation ~/.claude/skills/

# Copy any skills you want
cp -r pastor-ai-skills/skills/sermon-research ~/.claude/skills/
cp -r pastor-ai-skills/skills/church-email ~/.claude/skills/

# Want PDFs from a skill that makes them? Put the PDF library in its folder
cp pastor-ai-skills/shared/pdf_utils.py ~/.claude/skills/sermon-research/
```

Every skill carries the shared church context itself, so each one works on its own. You can copy just the ones you want.

The plugin install above is easier and keeps itself updated. Use manual copy only if you have a reason.

### Claude.ai Projects

1. Create a new Project in Claude.ai
2. Paste a filled-out church profile block into your Project's custom instructions (`skills/pastor-setup/SKILL.md` shows the format)
3. Add the `SKILL.md` contents for whichever skills you want below it. Each one already includes the shared church context.

You lose the PDF output in this mode, but every writing skill works.

---

## PDF Output (Optional)

Every skill answers right in the chat. Eight of them can also hand you a formatted, print-ready PDF when you ask for one ("make that a PDF"): sermon research briefs, meeting agendas, small group guides, letters on your letterhead, and more. PDFs need one Python package:

```bash
pip install reportlab
```

Claude Code can install it the first time you ask for a PDF. The skills that offer PDFs: `sermon-research`, `sermon-brainstorm`, `sermon-series`, `meeting-agenda`, `small-group-questions`, `midweek-devotional`, `announcement-script`, `church-letter`. Everything else has zero dependencies.

---

## Philosophy

**These are workflow tools, not prompt templates.** Each skill carries the know-how a pastor would otherwise have to look up: the questions that sharpen a sermon brief, how to break hard news in a letter, what makes a YouTube title work. You don't need to know email marketing or YouTube SEO. The skill knows.

**Your church and your tradition carry across every skill.** Every skill reads the same church profile and follows the same short set of guardrails, so tone, theology, and your church's details stay consistent without you repeating them.

**Sermon prep tools help you research and think. They never write the sermon.** That's between you and the Holy Spirit. The research skill digs into commentaries and context. The brainstorm skill asks you questions. Neither one hands you a manuscript.

**Every output is designed to be ready to use.** Not a rough draft you have to rewrite. Copy, paste, send. If you're rewriting more than 20% of what you get, the skill didn't do its job.

## What's New

See [CHANGELOG.md](CHANGELOG.md).

---

## About the Author

**Thomas Costello** is the founder and CEO of [REACHRIGHT](https://reachrightstudios.com) and Executive Pastor at New Hope Hawaii Kai. He's been in ministry for 20+ years, planted a church, led a church through a merger, grew a church from 30 to 150, and built a marketing agency that serves churches across the country.

- [LinkedIn](https://www.linkedin.com/in/tkcostello/)
- [Twitter/X](https://x.com/tkcostello)
- [REACHRIGHT](https://reachrightstudios.com)

---

## License

MIT. Use these however you want.
