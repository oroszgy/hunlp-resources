import sys


def is_clean(chars):
    return sum(ch.islower() for ch in chars) / len(chars) > 0.9


for line in sys.stdin:
    line = line.strip()
    if line and is_clean(line):
        print(line)

