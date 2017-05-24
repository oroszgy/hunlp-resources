import glob
import os
import re
import sys

import ftfy
import spacy.hu

TOKENIZER = spacy.hu.Hungarian().tokenizer
SENT_START = re.compile("^<s>")
TAG = re.compile(u"<[^<>]+>")


def clean_line(line, min_char_ratio=0.9, min_length=50):
    line = ftfy.fix_text(line)
    line = TAG.sub("", line)
    if line and len(line) > min_length:
        char_ratio = float(sum(ch.islower() for ch in line)) / len(line)
        if char_ratio > min_char_ratio:
            return line
        else:
            return None


def sentences(f):
    for line in f:
        if SENT_START.match(line):
            line = clean_line(line[3:].strip())
            if line:
                yield " ".join(token.text for token in TOKENIZER(line))


if __name__ == "__main__":
    outdir = sys.argv[2]
    for fpath in glob.iglob(sys.argv[1]):
        head, tail = os.path.split(fpath)
        with open(fpath, encoding='iso-8859-2') as inpf, \
                open("{}/{}".format(outdir, tail), "w", encoding="utf8") as outf:
            for s in sentences(inpf):
                outf.write(s)
                outf.write("\n")
