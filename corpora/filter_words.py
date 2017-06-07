import sys

import plac
import regex

# LOWER_WORD_RE = regex.compile("^\p{Ll}+$")
WORD_RE = regex.compile("^\p{L}\p{Ll}+$")
TOO_MANY_PUNCT = regex.compile("\p{P}{4,}")
NUMBERS = regex.compile("[0-9,.+-]+")

DROP_THRESHOLD = 5
FREQUENT_WORD_THRESHOLD = 10


def keep_token(word, freq):
    if freq < DROP_THRESHOLD:
        return False
    elif freq <= FREQUENT_WORD_THRESHOLD:
        return WORD_RE.match(word) is not None
    else:
        if TOO_MANY_PUNCT.search(word) or NUMBERS.match(word):
            return False
        else:
            return True


def parse_brown(line):
    path, word, freq = line.split("\t")
    return word, int(freq)


def parse_freq(line):
    tf, df, word = line.split("\t")
    return eval(word), int(tf)


def parse_w2v(line):
    word_w_vector = line.split(" ")
    return word_w_vector[0], DROP_THRESHOLD + 1


def main(format):
    for line in sys.stdin:
        if format == "brown":
            word, freq = parse_brown(line)
        elif format == "freq":
            word, freq = parse_freq(line)
        elif format == "w2v":
            word, freq = parse_w2v(line)
        else:
            print("Not correct format, it should be either 'brown', 'freq', or 'w2v'")
        if keep_token(word, freq):
            sys.stdout.write(line)


if __name__ == "__main__":
    plac.call(main)
