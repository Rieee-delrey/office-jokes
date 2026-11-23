import os

LINE = "The office plant died, so we held a retrospective to find out whose action item it was."

def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and verify: the entry must be exactly one line, 1-199 chars.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry text does not match the winning line"
    assert 1 <= len(written) <= 199, "entry outside the 1-199 char gate"
    assert written.strip() and "\n" not in written, "entry must be a single non-blank line"

if __name__ == "__main__":
    main()
