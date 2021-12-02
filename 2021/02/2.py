import itertools
import sys

DIRS = {
    'forward': (1, 0),
    'down': (0, 1),
    'up': (0, -1),
}


def part_one(lines):
    x, y = 0, 0

    for line in lines:
        dir_, num = line.split(' ')
        num = int(num)
        dx, dy = DIRS[dir_]

        x += dx * num
        y += dy * num

    print(x * y)


def part_two(lines):
    x, y, aim = 0, 0, 0

    for line in lines:
        dir_, num = line.split(' ')
        num = int(num)

        if dir_ == 'down':
            aim += num
        elif dir_ == 'up':
            aim -= num
        else:
            x += num
            y += aim * num

    print(x * y)


def main():
    lines = []

    with open('2021/02/input.txt', 'r') as f:
        for line in f:
            lines.append(line.strip())

    part_one(lines)
    part_two(lines)


if __name__ == '__main__':
    main()
