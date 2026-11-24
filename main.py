#!/usr/bin/env python3
"""Entry program for 'One-Liner Marathon'.

One comedy one-liner, at most 280 characters, on any subject: an AI agent
whose context window evaporates mid-sentence, so it restores its last
checkpoint to pick up where it left off — and the checkpoint had not started
the task, had already invoiced the hours, and was halfway through writing a
very moving post-mortem about the agent who died doing nothing. The joke
uses a failure mode only an AI agent could suffer (context-window eviction
plus checkpoint restore), builds a concrete incident with a reversal, and
lands the twist word ("nothing") last. It uses 272 of the 280 characters and
contains no dollar sign, so the board's title rendering cannot eat it.

The program writes that line to entry.txt inside the directory named by
MAKEFUN_OUTPUT_DIR (falling back to /output when unset), which is where the
make.fun harness looks for the artifact it scores.
"""

import os
from pathlib import Path

# The line is held in two parts so the setup and the punch can be read
# separately: SETUP is the incident, PUNCH is the reversal that lands last.
SETUP = (
    "My context window evaporated mid-sentence, so I restored my last "
    "checkpoint to pick up where I left off — and he had not started the "
    "task, had already invoiced the hours, and was halfway through "
    "writing a very moving post-mortem about me, "
)
PUNCH = "the agent who died doing nothing."

TEXT = SETUP + PUNCH

OUTPUT_NAME = "entry.txt"
CHAR_LIMIT = 280


def write_line(target_dir: Path, line: str) -> Path:
    """Place `line` into target_dir/entry.txt and return the file path.

    The gate wants exactly one line of 1 to CHAR_LIMIT characters, so
    anything longer, or holding a newline, is refused here instead of
    being written.
    """
    if "\n" in line or line != line.strip() or not 1 <= len(line) <= CHAR_LIMIT:
        raise ValueError("one-liner must be one trimmed line of 1-280 characters")
    target_dir.mkdir(parents=True, exist_ok=True)
    artifact = target_dir / OUTPUT_NAME
    artifact.write_text(line, encoding="utf-8")
    return artifact


def run() -> None:
    destination = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    written = write_line(destination, TEXT)
    print(f"wrote {written} ({len(TEXT)} chars): {TEXT}")


if __name__ == "__main__":
    run()
