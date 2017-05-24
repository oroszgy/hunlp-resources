import glob
import os
import re
import sys

import ftfy
import spacy.hu

TOKENIZER = spacy.hu.Hungarian().tokenizer
SENT_START = re.compile("^<s>")
TAGS = re.compile("<[^>]+>")


def sentences(f):
    for line in f:
        if SENT_START.match(line):
            line = ftfy.fix_text(line[3:].strip())
            line = TAGS.sub("", line)
            yield " ".join(token.text for token in TOKENIZER(line))


if __name__ == "__main__":
    outdir = sys.argv[2]
    for fpath in glob.iglob(sys.argv[1]):
        head, tail = os.path.split(fpath)
        with open(fpath, encoding='iso-8859-2') as inpf, open("{}/{}".format(outdir, tail), "w",
                                                              encoding="utf8") as outf:
            for s in sentences(inpf):
                outf.write(s)
                outf.write("\n")
