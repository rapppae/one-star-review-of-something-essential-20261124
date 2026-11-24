"""Write the one-star-review entry to /output/entry.txt.

One single-line deadpan one-star review, at most 160 characters,
of an everyday essential everyone relies on.
"""

from pathlib import Path

ENTRY = "One star. The sun has no off switch, no dimmer, and wakes me up every single morning without asking. Would not recommend."
# One line, 121 characters (limit 160).

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
