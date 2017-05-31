import sys

import regex

LOWER_WORD_RE = regex.compile("^\p{Ll}+$")
WORD_RE = regex.compile("^\p{L}\p{Ll}+$")
TOO_MANY_PUNCT = regex.compile("\p{P}{4,}")


def keep_token(word, freq):
    if freq < 3:
        if LOWER_WORD_RE.match(word):
            return True
        else:
            return False
    elif freq <= 5:
        if WORD_RE.match(word):
            return True
        else:
            return False
    else:
        if TOO_MANY_PUNCT.search(word):
            return False
        else:
            return True


if __name__ == "__main__":
    for line in sys.stdin:
        path, word, freq = line.split("\t")
        if keep_token(word, int(freq)):
            sys.stdout.write(line)
