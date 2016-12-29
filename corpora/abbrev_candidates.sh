#!/usr/bin/env bash

pv ./wiki_docs/*/wiki_* | tr " " "\n" | grep "[a-züóőúéáűí]\.$" | sort | uniq -c | sort -nr > abbrev_candidates.txt
