#!/usr/bin/env bash

cat ./abbreviations_*.txt | egrep -v '^#' | egrep -v '^\s*$'| egrep -v ' ' | sort -u > abbreviations.txt
