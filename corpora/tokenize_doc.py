import sys

from spacy.hu import Hungarian as HU
import ftfy

TOKENIZER = HU().tokenizer


def process_line(line):
    line = line.strip()
    line = ftfy.fix_text(line)
    if line:
        return " ".join(token.text for token in TOKENIZER(line))
    return None


if __name__ == "__main__":
    for line in sys.stdin:
        tokens = process_line(line)
        if tokens:
            print(tokens)
