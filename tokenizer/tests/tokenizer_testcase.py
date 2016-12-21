import os
import re

import sys


class TokenizerTestCase(object):
    INPUT_PREFIX = "IN :"
    OUTPUT_PREFIX = "OUT:"
    WORD_PATTERN = re.compile(r"<([wc])>([^<>]+)</\1>")

    def __init__(self, input_str, expected_words):
        self.input = input_str
        self.expected_tokens = expected_words

    def __repr__(self):
        return "TokenizerTestCase<input={}, words={}>".format(repr(self.input), self.expected_tokens)

    def to_tuple(self):
        return (self.input, self.expected_tokens)

    @classmethod
    def _parse_output_line(cls, line):
        for match in cls.WORD_PATTERN.finditer(line):
            yield match.group(2)

    @classmethod
    def read_from_file(cls, path):
        with open(path) as f:
            input_lines = []
            output_words = []
            last_type = None
            for line in f:
                if line.startswith(cls.INPUT_PREFIX):
                    if last_type == TokenizerTestCase.OUTPUT_PREFIX and input_lines:
                        yield TokenizerTestCase("\n".join(input_lines), output_words)
                        input_lines = []
                        output_words = []
                    input_lines.append(line[len(cls.INPUT_PREFIX):].strip())
                    last_type = TokenizerTestCase.INPUT_PREFIX
                elif line.startswith(cls.OUTPUT_PREFIX):
                    output_words.extend(list(cls._parse_output_line(line.strip())))
                    last_type = TokenizerTestCase.OUTPUT_PREFIX
                else:
                    # Comments separate test cases
                    if input_lines:
                        yield TokenizerTestCase("\n".join(input_lines), output_words)
                        input_lines = []
                        output_words = []
                    last_type = None


_MODULE_PATH = os.path.dirname(__file__) or "."

_DOTS_CASES = list(TokenizerTestCase.read_from_file(_MODULE_PATH + "/test_default_token_dots.txt"))
_HYPHEN_CASES = list(TokenizerTestCase.read_from_file(_MODULE_PATH + "/test_default_token_hyphen.txt"))
_QUOTE_CASES = list(TokenizerTestCase.read_from_file(_MODULE_PATH + "/test_default_token_quote.txt"))
_NUMBER_CASES = list(TokenizerTestCase.read_from_file(_MODULE_PATH + "/test_default_token_numbers.txt"))
_MISC_CASES = list(TokenizerTestCase.read_from_file(_MODULE_PATH + "/test_default_token_misc.txt"))
_IT_CASES = list(TokenizerTestCase.read_from_file(_MODULE_PATH + "/test_default_token_it.txt"))

# TODO: Until this get fixed we cannot really test the urls: https://github.com/explosion/spaCy/issues/344

ALL_TESTCASES = _DOTS_CASES + _HYPHEN_CASES + _QUOTE_CASES + _NUMBER_CASES + _MISC_CASES  # + _IT_CASES

if __name__ == "__main__":
    test_cases = TokenizerTestCase.read_from_file(sys.argv[1])
    print("[" + ",\n".join(["({}, {})".format(repr(tc.input), repr(tc.expected_tokens)) for tc in test_cases]) + "]")
