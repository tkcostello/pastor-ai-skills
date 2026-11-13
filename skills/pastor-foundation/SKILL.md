---
name: pastor-foundation
description: Shared church context for pastor writing that no other pastor skill covers, and the home of the kit's tradition presets. Use when the pastor says "write something for my church", "draft a note to my staff", "how does this kit handle my theology", "make the skills fit a Pentecostal (or Reformed, or Baptist) church", or asks to change the rules every pastor skill follows.
---

# Pastor Foundation

Every task skill in this kit carries the same short context block (below), so each one works on its own. This skill holds the source of that block and the longer references behind it. Use it directly for church writing that has no dedicated skill.

## The shared block

Everything in `context.md` applies here. Read it first.

## References

- `references/traditions.md`: what Pentecostal and charismatic (including Foursquare), Reformed, Baptist and broadly evangelical churches treat as normal, plus how to handle other traditions. Read it when the profile names a tradition and the writing touches worship, baptism, the Spirit's gifts, leadership or church government.
- `references/bible-translations.md`: notes on common translations, for when a pastor asks which to use or why a verse reads differently.

## Changing the shared rules

The block is copied into every task skill between `shared-context` markers. To change it, edit `context.md` and run:

```bash
python scripts/sync-context.py
```

`--check` reports any skill whose copy is out of date without changing files.
