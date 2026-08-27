---
name: pastor-setup
description: Use when setting up pastor-ai-skills for the first time, when a pastor wants to view or change their church profile (church name, denomination, attendance, congregation, community, Bible translation), or when any pastor skill cannot find the church profile file at ~/.claude/pastor-profile.md.
---

# Pastor Setup: Your Church Profile

One-time setup for every skill in the pastor-ai-skills collection. This skill runs a short guided interview, then saves a profile file that stores your church's context so you never have to repeat it. Every other skill reads this file automatically.

The profile lives at `~/.claude/pastor-profile.md`.

---

## What This Skill Does

1. Checks whether `~/.claude/pastor-profile.md` already exists.
2. If it exists: show the current values and ask what to change. Update only what the pastor asks to change.
3. If it does not exist: run the interview below.

## Interview Rules

These rules are non-negotiable:

- **One question per message.** Never bundle two questions together. Ask, wait for the answer, then ask the next.
- **Acknowledge each answer in a few words before the next question.** Like a person would. Not a form.
- **Show progress.** Prefix each question with where they are, like "2 of 6."
- **Any answer can be "skip."** Skipping an optional question is always fine. Move on without comment.
- **Adapt.** If an answer already covers a later question, don't ask it again. If an answer is interesting ("we're a military town"), one natural follow-up is allowed, but only one.
- **Keep it warm and fast.** The whole core round should feel like two minutes, not an intake form.

## Round 1: The Core (6 questions, required)

Open with one sentence: this takes about two minutes, sets up every skill, and only happens once.

1. **Church name.** "What's your church's name?"
2. **Their name and role.** "And your name, as you'd want it to appear in content? Plus your role, if you're not the lead pastor." (Executive pastors, worship pastors, and comms directors use these tools too. Capture the role so skills write from the right seat.)
3. **Denomination or tradition.** "What denomination or tradition are you part of? Totally fine to say nondenominational." (Default: nondenominational evangelical.)
4. **Attendance.** "About how many people attend on an average weekend?"
5. **Location.** "What city and state?" If they only give a city, that's enough.
6. **Bible translation.** "Which Bible translation do you preach from?" (Default: NIV.)

## Round 2: The Context (optional, offered as one choice)

After question 6, offer it as a single yes/no: "That's the essentials. Want to answer 5 more so the tools really know your church? Takes two more minutes and makes every output sharper. Or we can stop here and add detail later."

If yes, one at a time:

7. **Community.** "Tell me about your community. Urban, suburban, or rural, and anything that defines it: college town, military base, retirement area, tourist economy."
8. **Congregation.** "Who actually fills your seats? Age mix, young families vs. seniors, long-timers vs. new believers, anything that shapes how you communicate."
9. **Season.** "What season is the church in right now? Growing, plateaued, rebuilding, brand-new plant, fresh off a transition. Be honest, this stays on your machine."
10. **Ministries.** "Any ministries or recurring programs the tools should know by name? Youth group name, kids ministry, small group system, food pantry, whatever comes up in your communication a lot."
11. **Voice.** "Last one. When your church communicates, do you lean formal or casual? Any words or phrases you always use, or never use?"

## Writing the Profile

Write the answers to `~/.claude/pastor-profile.md` in exactly this format. Omit any line the pastor skipped, except DENOMINATION and BIBLE_TRANSLATION, which always get written with their defaults if skipped.

```markdown
# Church Profile
Used by all pastor-ai-skills. Edit anytime, or run /pastor-setup to update.

CHURCH_NAME: Grace Community Church
PASTOR_NAME: Pastor Mike
ROLE: Lead Pastor
DENOMINATION: Southern Baptist
ATTENDANCE: 175
LOCATION: Tulsa, Oklahoma
BIBLE_TRANSLATION: ESV
COMMUNITY: Suburban, growing area on the north side of Tulsa, lots of young families moving in
CONGREGATION: Mix of young families and empty nesters, about a third are new to church in the last 3 years
CHURCH_SEASON: Growing, added a second service in January
MINISTRIES: Ignite Youth, Grace Kids, community groups (our small group system), Tulsa food pantry partnership
VOICE: Casual but reverent. We say "community groups" never "cell groups." Avoid churchy insider language.
SERVICE_TIMES: Sundays 9:00 and 11:00 AM
WEBSITE: gracetulsa.org

## Notes
Anything else the pastor wants every skill to know goes here.
```

SERVICE_TIMES and WEBSITE were not interview questions. If they came up naturally, save them. Otherwise leave them out.

## After Writing

Confirm with a short recap of what was saved and one example of how it gets used ("Every skill now writes as Pastor Mike of Grace Community Church, quotes the ESV, and knows your community groups by name"). Then suggest a natural first skill to try, like `/church-email` or `/sermon-research`.

## Environments Without File Access

If the environment cannot write files (for example, a claude.ai project), run the same interview, then output the filled-in profile block and tell the pastor to paste it into their project instructions.
