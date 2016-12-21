import os

import pytest
from spacy.hu import Hungarian

from tokenizer.tests.tokenizer_testcase import ALL_TESTCASES


@pytest.fixture(scope="session")
def HU():
    return Hungarian()


@pytest.fixture(scope="module")
def hu_tokenizer(HU):
    return HU.tokenizer


@pytest.mark.parametrize(("test_case"), ALL_TESTCASES)
def test_testcases(hu_tokenizer, test_case):
    tokens = hu_tokenizer(test_case.input)
    token_list = [token.orth_ for token in tokens if not token.is_space]
    assert test_case.expected_tokens == token_list  # , "{} was erronously tokenized as {}".format(test_case, token_list)
