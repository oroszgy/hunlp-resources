import sys
from collections import Counter
from collections import defaultdict

from spacy.hu import Hungarian

tokenizer = Hungarian().tokenizer


def tokenize(text):
    return [t.orth_ for t in tokenizer(text)]


def extract_docs(wiki_docsfile):
    inside_doc = False
    doc_words = []
    for line in wiki_docsfile:
        line = line.strip()
        if line.startswith("<doc"):
            inside_doc = True
            doc_words = []
        elif line.startswith("</doc"):
            inside_doc = False
            yield doc_words
        else:
            if inside_doc:
                doc_words.extend(tokenize(line))


def calculate_stats(docs):
    word_df = defaultdict(int)
    word_freq = defaultdict(int)
    for doc in docs:
        wordcounts = Counter(doc)
        for word, freq in wordcounts.items():
            word_df[word] += 1
            word_freq[word] += freq
    return dict(word_freq), dict(word_df)


if __name__ == "__main__":
    docs = extract_docs(sys.stdin)
    word_freq, word_df = calculate_stats(docs)
    words = sorted(word_freq.keys())

    for w in words:
        print("{}\t{}\t{}".format(w, word_freq[w], word_df[w]))
