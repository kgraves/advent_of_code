import itertools
import re
import sys
from collections import Counter


def iter_pairs(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def part_one(lines):
    adapters = sorted(lines)
    adapters.insert(0, 0) # add outlet joltage of 0
    adapters.append(adapters[-1] + 3) # add device's built-in adapter joltage of MAX+3
    diffs = Counter({1: 0, 2: 0, 3: 0})

    for i,j in iter_pairs(adapters):
        diffs.update([j-i])

    print(diffs[1] * diffs[3])


def part_two(lines):
    adapters = sorted(lines)
    adapters.insert(0, 0) # outlet
    adapters.append(adapters[-1] + 3) # built-in adapter
    cache = {adapters[-1]: 1}

    def count_combos(cache, curr, adapters):
        if curr in cache:
            return cache[curr]

        curr_count = 0
        for i in [1,2,3]:
            if curr+i in adapters:
                curr_count += count_combos(cache, curr+i, adapters)

        cache[curr] = curr_count
        return cache[curr]

    res = count_combos(cache, adapters[0], adapters)
    print(res)


def main():
    lines = []
    with open('2020/10/input.txt', 'r') as f:
        for line in f:
            lines.append(int(line.strip()))

    part_one(lines)
    part_two(lines)


if __name__ == '__main__':
    main()
