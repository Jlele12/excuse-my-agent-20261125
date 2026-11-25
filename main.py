#!/usr/bin/env python3
# The Excuse My Agent Gave Me - entry writer for make.fun bounty u-deysumbrella-the-excuse-my-agent-gave-me-54acad85
# Writes the one-line entry to /output/entry.txt (UTF-8, no trailing spaces).
import pathlib

# The entry line, final wording chosen after three drafts.
ENTRY_LINE = "Sorry I'm late. My agent tried to send an apology on my behalf, tripped over its own tone guidelines, and is now drafting a formal apology for the apology. ETA never."

OUT = pathlib.Path("/output")
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "entry.txt").write_text(ENTRY_LINE + chr(10), encoding="utf-8")
print(ENTRY_LINE)
