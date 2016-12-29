import sys

from spacy.hu import Hungarian as HU

TOKENIZER = HU().tokenizer


def process_line(line):
    line = line.strip()
    if not line.startswith("<") and line:
        return " ".join(token.orth_ for token in TOKENIZER(line))


if __name__ == "__main__":
    for line in sys.stdin:
        tokens = process_line(line)
        if tokens:
            print(tokens)
