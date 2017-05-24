#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cat $1 | iconv -f latin2 -t utf8 | awk '/^<s>/{print substr($0,4)}' | python $DIR/tokenize_doc.py > $2
