---
name: pastor-setup
description: Use when setting up pastor-ai-skills for the first time, when a pastor wants to view or change their church profile (church name, denomination, attendance, location, Bible translation), or when any pastor skill cannot find the church profile file at ~/.claude/pastor-profile.md.
---

# Pastor Setup: Your Church Profile

One-time setup for every skill in the pastor-ai-skills collection. This skill creates a small profile file that stores your church's details so you never have to repeat them. Every other skill reads this file automatically.

The profile lives at `~/.claude/pastor-profile.md`.

---

## What This Skill Does

1. Checks whether `~/.claude/pastor-profile.md` already exists.
2. If it exists: show the current values and ask what to change. Update only what the pastor asks to change.
3. If it does not exist: run first-time setup below.

## First-Time Setup

Ask for these details conversationally. One short message, not an interrogation. Required fields first, then offer the optional ones in the same message.

**Required:**
- Church name
- Pastor's name (as they want to appear in content, e.g. "Pastor Mike" or "Rev. Michael Torres")
- Average weekly attendance
- City and state

**Optional (offer, don't demand):**
- Denomination or tradition (default: nondenominational evangelical)
- Preferred Bible translation (default: NIV)
- Service times
- Church website
- Anything else the pastor wants every skill to know (ministry names, key events, tone preferences)

## Writing the Profile

Write the answers to `~/.claude/pastor-profile.md` in exactly this format:

```markdown
# Church Profile
Used by all pastor-ai-skills. Edit anytime, or run /pastor-setup to update.

CHURCH_NAME: Grace Community Church
PASTOR_NAME: Pastor Mike
DENOMINATION: Southern Baptist
ATTENDANCE: 175
LOCATION: Tulsa, Oklahoma
BIBLE_TRANSLATION: ESV
SERVICE_TIMES: Sundays 9:00 and 11:00 AM
WEBSITE: gracetulsa.org

## Notes
Anything else the pastor wants every skill to know goes here.
```

Omit optional lines the pastor skipped, except DENOMINATION and BIBLE_TRANSLATION, which always get written with their defaults if skipped.

## After Writing

Confirm with a short recap of what was saved and one example of how it gets used ("Every skill will now quote scripture in ESV and write as Pastor Mike of Grace Community Church"). Then suggest a natural first skill to try, like `/church-email` or `/sermon-research`.

## Environments Without File Access

If the environment cannot write files (for example, a claude.ai project), output the filled-in profile block instead and tell the pastor to paste it into their project instructions.
