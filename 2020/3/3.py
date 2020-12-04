import operator
import sys
from functools import reduce


OPEN = '.'
TREE = '#'


def coords(mapp, x, y):
    w = len(mapp[0])

    return x % w, y


def part_one(mapp):
    x, y = 0, 0
    right = 3
    down = 1
    count = 0

    while y < len(mapp):
        if mapp[y][x] == TREE:
            count += 1

        x, y = coords(mapp, x+right, y+down)

    print(count)


def part_two(mapp):
    slopes = [
        (1,1),
        (3,1),
        (5,1),
        (7,1),
        (1,2),
    ]
    counts = []

    for slope in slopes:
        x, y = 0, 0
        count = 0

        while y < len(mapp):
            if mapp[y][x] == TREE:
                count += 1

            x, y = coords(mapp, x+slope[0], y+slope[1])

        counts.append(count)

    print(reduce(operator.mul, counts, 1))


def main():
    mapp = []

    for line in sys.stdin:
        mapp.append(line.strip())

    part_one(mapp)
    part_two(mapp)


if __name__ == '__main__':
    main()
