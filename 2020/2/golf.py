import re
import sys
from collections import Counter


INPUT_RE = re.compile('^(\d+)\-(\d+)\ ([a-z])\:\ ([a-z]+)$')


def part_one(lines):
    v = 0
    for line in lines:
        mn, mx, lt, ps = INPUT_RE.match(line).groups()
        p = Counter(ps)
        v += 1 if (int(mn) <= p[lt] <= int(mx)) else 0

    print(v)


def part_two(lines):
    v = 0
    for line in lines:
        mn, mx, lt, ps = INPUT_RE.match(line).groups()
        v += 1 if (ps[int(mn)-1]==lt) ^ (ps[int(mx)-1]==lt) else 0

    print(v)


def main():
    valids = 0
    lines = []

    with open('2020/2/input.txt', 'r') as f:
        for line in f:
            lines.append(line)

    part_one(lines)
    part_two(lines)


if __name__ == '__main__':
    main()
