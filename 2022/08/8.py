import itertools


def part_one(lines):
    m, h, w = make_map(lines)
    visibles = set()

    for r in range(1, h-1):
        ltall = m[r][0]
        rtall = m[r][-1]

        for c in range(1, w-1):
            if m[r][c] > ltall:
                visibles.add((r, c))
            ltall = max(ltall, m[r][c])

        for c in range(1, len(m[0])-1):
            if m[r][-c-1] > rtall:
                visibles.add((r, len(m[r])-c-1))
            rtall = max(rtall, m[r][-c-1])

    for c in range(1, len(m[0])-1):
        ttall = m[0][c]
        btall = m[-1][c]

        for r in range(1, len(m)-1):
            if m[r][c] > ttall:
                visibles.add((r, c))
            ttall = max(ttall, m[r][c])

            if m[-r-1][c] > btall:
                visibles.add((len(m)-r-1, c))
            btall = max(btall, m[-r-1][c])

    sides = 2 * (w + h) - 4
    print(len(visibles) + sides)


def part_two(lines):
    pass


def main():
    lines = []

    with open('2022/08/input.txt', 'r') as f:
        for line in f:
            lines.append(line.strip())

    part_one(lines)
    part_two(lines)


def iter_pairs(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def iter_triple(iterable):
    a, b, c = itertools.tee(iterable, 3)
    next(b, None)
    next(c, None); next(c, None)
    return zip(a, b, c)


def get_dirs_diag(y, x, h, w):
    candidates = [(-1, 0), (-1, 1), (1, 0), (1, 1), (0, 1), (1, -1), (0, -1), (-1, -1)]
    return [(y + dy, x + dx) for dy, dx in candidates if (0 <= (y + dy) < h) and (0 <= (x + dx) < w)]


def get_dirs(y, x, h, w):
    candidates = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    return [(y + dy, x + dx) for dy, dx in candidates if (0 <= (y + dy) < h) and (0 <= (x + dx) < w)]


def make_map(lines):
    map_ = [[int(d) for d in line.strip()] for line in lines]
    h, w = len(map_), len(map_[0])

    return map_, h, w


if __name__ == '__main__':
    main()
