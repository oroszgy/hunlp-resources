import sys

from spacy.hu import Hungarian

if __name__ == "__main__":
    HU = Hungarian()
    tokenizer = HU.tokenizer
    text = sys.stdin.read()
    tokens = tokenizer(text)
    token_list = [token.orth_ for token in tokens if not token.is_space]
    print("\n".join(token_list))
