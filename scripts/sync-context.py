#!/usr/bin/env python3
"""Copy the shared church-context block into every task skill.

The block lives in skills/pastor-foundation/context.md. Each task skill carries
its own copy between these markers, so the skill works even when installed on
its own:

    <!-- shared-context:start -->
    ...
    <!-- shared-context:end -->

Usage:
    python scripts/sync-context.py          # rewrite the blocks
    python scripts/sync-context.py --check  # exit 1 if any block is stale
"""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCE = ROOT / "skills" / "pastor-foundation" / "context.md"
SKIP = {"pastor-foundation", "pastor-setup"}
START = "<!-- shared-context:start: edit skills/pastor-foundation/context.md, then run scripts/sync-context.py -->"
END = "<!-- shared-context:end -->"
PATTERN = re.compile(r"<!-- shared-context:start.*?-->.*?<!-- shared-context:end -->", re.S)


def main() -> int:
    check = "--check" in sys.argv
    block = f"{START}\n{SOURCE.read_text(encoding='utf-8').strip()}\n{END}"
    stale = []
    for skill in sorted((ROOT / "skills").glob("*/SKILL.md")):
        if skill.parent.name in SKIP:
            continue
        text = skill.read_text(encoding="utf-8")
        if not PATTERN.search(text):
            print(f"missing markers: {skill.relative_to(ROOT)}")
            stale.append(skill)
            continue
        updated = PATTERN.sub(lambda _: block, text)
        if updated != text:
            stale.append(skill)
            if not check:
                skill.write_text(updated, encoding="utf-8", newline="\n")
                print(f"synced: {skill.relative_to(ROOT)}")
    if check and stale:
        print(f"{len(stale)} skill(s) out of date. Run: python scripts/sync-context.py")
        return 1
    if not stale:
        print("all skills up to date")
    return 0


if __name__ == "__main__":
    sys.exit(main())
