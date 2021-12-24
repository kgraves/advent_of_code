import collections
import re


INPUT_RE = re.compile('^target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)$')


def trinumber(n):
    return (n * (n + 1)) // 2


def part_one(lines):
    _, _, y1, y2 = INPUT_RE.match(lines[0].strip()).groups()
    min_y = min(int(y1), int(y2))

    vyi = -min_y - 1
    print(trinumber(abs(vyi)))


def part_two(lines):
    x1, x2, y1, y2 = INPUT_RE.match(lines[0].strip()).groups()
    left, right = min(int(x1), int(x2)), max(int(x1), int(x2))
    bottom, top = min(int(y1), int(y2)), max(int(y1), int(y2))
    hits = set()

    for x in range(1, right + 1):
        for y in range(bottom, abs(bottom) + 1):
            cx, cy = 0, 0
            vx, vy = x, y

            while cy > bottom:
                cx += vx
                cy += vy
                vx = max(0, vx - 1)
                vy -= 1

                if (left <= cx <= right) and (top >= cy >= bottom):
                    hits.add((x, y))

                if cx > right or cy < bottom:
                    continue

    print(len(hits))


def main():
    lines = []

    with open('2021/17/input.txt', 'r') as f:
        for line in f:
            lines.append(line.strip())

    part_one(lines)
    part_two(lines)


if __name__ == '__main__':
    main()
