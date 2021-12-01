import itertools
import sys


def iter_pairs(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def iter_triple(iterable):
    a, b, c = itertools.tee(iterable, 3)
    next(b, None)
    next(c, None); next(c, None)
    return zip(a, b, c)


def part_one(nums):
    increases = 0
    for prev, curr in iter_pairs(nums):
        if curr > prev:
            increases += 1

    print(increases)


def part_two(nums):
    increases = 0
    iter_ = iter_triple(nums)
    prev_sum = sum(next(iter_))

    for prev, curr, next_ in iter_:
        curr_sum = (prev + curr + next_)
        if prev_sum < curr_sum:
            increases += 1

        prev_sum = curr_sum

    print(increases)


def main():
    lines = []

    with open('2021/01/input.txt', 'r') as f:
        for line in f:
            lines.append(int(line.strip()))

    part_one(lines)
    part_two(lines)


if __name__ == '__main__':
    main()
