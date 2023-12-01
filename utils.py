import itertools


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
    map_ = [[int(d) for d in line] for line in lines]
    h, w = len(map_), len(map_[0])

    return map_, h, w
