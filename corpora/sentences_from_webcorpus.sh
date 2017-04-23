#!/bin/bash

cat $1 | iconv -f latin2 -t utf8 | awk '/^<s>/{print substr($0,4)}' > $2
