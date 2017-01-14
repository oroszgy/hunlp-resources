#! /usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class TokenizerHandler(ContentHandler):
    def __init__(self):
        self.in_word, self.isAnal = False, False
        self.in_analysis, self.in_anav, self.in_msd, self.in_lemma, self.in_tag = False, False, False, False, False

    def startElement(self, name, attrs):
        self.last_start = name

        if name == 'w':
            self.in_word = True;
            self.word = ""
            self.lemma = ""
            self.tag = ""
        elif name == 'c':
            self.in_word = True;
            self.word = "";
            self.lemma = ""
            self.tag = ""
        elif name == "s":
            self.sent_str = []
            self.sent = []
        elif name == 'ana':
            self.in_analysis = True
        elif name == 'anav':
            self.in_anav = True
        elif name == "msd":
            self.in_msd = True
        elif name == "lemma":
            self.in_lemma = True
        elif name == "mscat":
            self.in_tag = True

    def characters(self, ch):
        if self.last_start == "s":
            self.sent_str.append(ch)
        elif self.in_word and not self.in_analysis and not self.in_anav:
            self.word += ch
        elif self.in_word and self.in_analysis and self.in_msd and self.in_lemma:
            self.lemma += ch
        elif self.in_word and self.in_analysis and self.in_msd and self.in_tag:
            self.tag += ch

    def endElement(self, name):
        if name == 'w':
            self.in_word = False
            self.sent.append((self.word.strip(), self.lemma.strip(), self.tag.strip()))
        elif name == 'c':
            self.in_word = False
            self.sent.append((self.word.strip(), self.lemma.strip(), self.tag.strip()))
        elif name == 's':
            print("".join(self.sent_str).strip() + "\t" + " ".join(
                map(self.token2str, self.sent)).strip())
        elif name == 'ana':
            self.in_analysis = False
        elif name == 'anav':
            self.in_anav = False
        elif name == "msd":
            self.in_msd = False
        elif name == "lemma":
            self.in_lemma = False
        elif name == "mscat":
            self.in_tag = False

    def token2str(self, token_anal):
        # plain = "#".join(tokenTup)
        plain = token_anal[0]
        tok = plain.replace(" ", " ")
        return tok


if __name__ == "__main__":
    parser = make_parser()
    curHandler = TokenizerHandler()
    parser.setContentHandler(curHandler)
    parser.parse(codecs.open(sys.argv[1], encoding="iso-8859-2"))
