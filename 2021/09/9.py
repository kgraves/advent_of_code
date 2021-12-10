import math
import sys


def get_dirs(y, x, h, w):
    candidates = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    return [(y + dy, x + dx) for dy, dx in candidates if (0 <= (y + dy) < h) and (0 <= (x + dx) < w )]


def low_points(map_):
    h, w = len(map_), len(map_[0])
    lows = []

    for y in range(h):
        for x in range(w):
            if all(map_[y][x] < map_[d[0]][d[1]] for d in get_dirs(y, x, h, w)):
                lows.append((y, x))

    return lows


def find_basin(y, x, map_):
    h, w = len(map_), len(map_[0])
    seen = set()
    queue = [(y, x)]

    seen.add((y, x))
    while len(queue) > 0:
        cy, cx = queue.pop()
        if map_[cy][cx] < 9:
            seen.add((cy, cx))
            dirs = get_dirs(cy, cx, h , w)
            queue.extend([d for d in dirs if d not in seen])

    return seen


def part_one(lines):
    map_ = [[int(d) for d in line] for line in lines]
    risk = 0
    h, w = len(map_), len(map_[0])
    print(sum(map_[l[0]][l[1]] + 1 for l in low_points(map_)))


def part_two(lines):
    map_ = [[int(d) for d in line] for line in lines]
    basins = [find_basin(*l, map_) for l in low_points(map_)]
    largest = sorted(basins, key=len, reverse=True)
    print(math.prod([len(l) for l in largest[:3]]))


def main():
    lines = []

    with open('2021/09/input.txt', 'r') as f:
        for line in f:
            lines.append(line.strip())

    part_one(lines)
    part_two(lines)


if __name__ == '__main__':
    main()
