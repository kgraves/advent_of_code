import collections
import functools
import itertools
import math
import re
import sys
from dataclasses import dataclass

INPUT_RE = re.compile(r'^(\d+),(\d+)\ -\>\ (\d+),(\d+)$')


def part_one(lines):
    pass


def part_two(lines):
    pass


def main():
    lines = []

    with open('2022/XX/sample.txt', 'r') as f:
        for line in f:
            lines.append(line.strip())

    part_one(lines)
    part_two(lines)


if __name__ == '__main__':
    main()
