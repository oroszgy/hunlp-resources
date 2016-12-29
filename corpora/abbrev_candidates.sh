#!/usr/bin/env bash

pv ./wiki_docs/*/wiki_* | tr " " "\n" | grep "\.$" | sort | uniq -c | sort -nr > abbrev_candidates.txt
