import re
import sys
from collections import Counter


def part_one(lines):
    yeses = 0
    buffer = set()

    for l in lines:
        if not l.strip():
            yeses += len(buffer)
            buffer = set()
        else:
            buffer.update(*l.strip())
    else:
        yeses += len(buffer)

    print(yeses)


def part_two(lines):
    yeses = 0
    buffer = []

    def num_unanimous(buff):
        num_peeps = len(buffer)
        return sum(int(v == num_peeps) for _,v in Counter(''.join(buffer)).items())

    for l in lines:
        if not l.strip():
            yeses += num_unanimous(buffer)
            buffer = []
        else:
            buffer.append(l.strip())
    else:
        yeses += num_unanimous(buffer)

    print(yeses)


def main():
    lines = []

    with open('2020/6/input.txt', 'r') as f:
        for line in f:
            lines.append(line)

    part_one(lines)
    part_two(lines)


if __name__ == '__main__':
    main()
