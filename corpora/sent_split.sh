#!/usr/bin/env bash

sed 's/\([\.\?\!] *\)/\1\'$'\n/g'
