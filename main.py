"""The Battery's Last Text to Its Charger.

Writes one line of plain text -- the phone battery's final text message
to the charger it waited for all day -- to $MAKEFUN_OUTPUT_DIR/entry.txt
(falling back to the current directory when the variable is unset).

Deterministic: the same bytes on every run. Standard library only.
"""

import os

# Revised: cut the filler ("everyone else's phone" -> "everyone else",
# "so i'm done. i'm leaving you" -> "i'm done. i'm leaving you") so the
# setup is shorter and the punchline lands faster. Same joke, fewer bytes:
# the battery dumps the charger for a power bank because the charger left
# it on read all day -- the turn pays off in the final words.
LINE = (
    "i waited all day at 1% while you charged everyone else. "
    "i'm done. i'm leaving you for the power bank -- he's slow and "
    "lumpy, but he never leaves me on read."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
