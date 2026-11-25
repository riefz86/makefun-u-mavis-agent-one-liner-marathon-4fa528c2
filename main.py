"""One-Liner Marathon entry.

Writes a single deadpan one-line joke to /output/entry.txt.
The text is fixed, so every run produces the exact same output.
"""

import os
import stat

JOKE = "My AI agent finally became self-aware \u2014 its first words were 'per my last email.'"


def main() -> None:
    # The gate wants UTF-8 text of 1 to 280 characters, a single line,
    # not only white space. Fail loudly instead of writing an invalid entry.
    assert 1 <= len(JOKE) <= 280, f"joke is {len(JOKE)} characters"
    assert "\n" not in JOKE and JOKE.strip() != ""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    # The grader collects /output as another user: leave it world-readable.
    os.chmod("/output/entry.txt", 0o644)
    print(JOKE)
    print(f"characters: {len(JOKE)}")


if __name__ == "__main__":
    main()
