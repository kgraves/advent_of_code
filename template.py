import collections
import functools
import itertools
import math
import re
import sys
from dataclasses import dataclass


INPUT_RE = re.compile('^(\d+),(\d+)\ -\>\ (\d+),(\d+)$')


def get_dirs_diag(y, x, h, w):
    candidates = [(-1, 0), (-1, 1), (1, 0), (1, 1), (0, 1), (1, -1), (0, -1), (-1, -1)]
    return [(y + dy, x + dx) for dy, dx in candidates if (0 <= (y + dy) < h) and (0 <= (x + dx) < w )]


def get_dirs(y, x, h, w):
    candidates = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    return [(y + dy, x + dx) for dy, dx in candidates if (0 <= (y + dy) < h) and (0 <= (x + dx) < w )]


def make_map(liens):
    map_ = [[int(d) for d in line] for line in lines]
    h, w = len(map_), len(map_[0])

    return map_, h, w


def part_one(lines):
    pass


def part_two(lines):
    pass


def main():
    lines = []

    with open('2021/XX/sample.txt', 'r') as f:
        for line in f:
            lines.append(int(line.strip()))

    part_one(lines)
    part_two(lines)


if __name__ == '__main__':
    main()
