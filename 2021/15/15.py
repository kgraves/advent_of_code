import collections
import heapq
import math


def get_dirs(y, x, h, w):
    candidates = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    return [(y + dy, x + dx) for dy, dx in candidates if (0 <= (y + dy) < h) and (0 <= (x + dx) < w )]


def make_map(lines):
    map_ = [[int(d) for d in line] for line in lines]
    h, w = len(map_), len(map_[0])

    return map_, h, w


def dijkstras_paged(map_, h, w, pages=1):
    weights = collections.defaultdict(int)

    weights[(0, 0)] = 0
    pq = [(0, 0, 0)]
    heapq.heapify(pq)

    while len(pq) > 0:
        weight, row, col = heapq.heappop(pq)

        if (row, col) == (h * pages - 1, w * pages - 1):
            break

        for n_row, n_col in get_dirs(row, col, h * pages, w * pages):
            adjusted_risk = (map_[n_row % h][n_col % w] + ((n_row // h) + (n_col // w)) - 1) % 9 + 1
            new_weight = weights[(row, col)] + adjusted_risk

            if new_weight < weights.get((n_row, n_col), math.inf):
                weights[(n_row, n_col)] = new_weight
                heapq.heappush(pq, (new_weight, n_row, n_col))

    return weights


def astar_paged(map_, h, w, pages=1):
    def dist(row1, col1, row2, col2):
        return math.sqrt(
            math.pow(row1 + row2, 2) +
            math.pow(col1 + col2, 2)
        )

    weights = collections.defaultdict(int)
    distances = collections.defaultdict(int)

    s = (0, 0, 0)
    weights[(0, 0)] = 0
    distances[(0, 0)] = dist(0, 0, h - 1, w - 1)
    pq = [s]
    heapq.heapify(pq)

    while len(pq) > 0:
        weight, row, col = heapq.heappop(pq)

        if (row, col) == (h * pages - 1, w * pages - 1):
            break

        for n_row, n_col in get_dirs(row, col, h * pages, w * pages):
            adjusted_risk = (map_[n_row % h][n_col % w] + ((n_row // h) + (n_col // w)) - 1) % 9 + 1
            new_weight = weights[(row, col)] + adjusted_risk

            if new_weight < weights.get((n_row, n_col), math.inf):
                weights[(n_row, n_col)] = new_weight
                distances[(n_row, n_col)] = new_weight + dist(n_row, n_col, h * pages - 1, w * pages - 1)
                heapq.heappush(pq, (distances[(n_row, n_col)], n_row, n_col))

    return weights


def part_one(lines):
    map_, h, w = make_map(lines)
    weights = dijkstras_paged(map_, h, w)
    astar_weights = astar_paged(map_, h, w)

    print(weights[(h - 1, w - 1)])
    print(astar_weights[(h - 1, w - 1)])


def part_two(lines):
    pages = 5
    map_, h, w = make_map(lines)
    weights = dijkstras_paged(map_, h, w, pages)
    astar_weights = astar_paged(map_, h, w, pages)

    print(weights[(h * pages - 1, w * pages- 1)])
    print(astar_weights[(h * pages - 1, w * pages- 1)])


def main():
    lines = []

    with open('2021/15/input.txt', 'r') as f:
        for line in f:
            lines.append(line.strip())

    part_one(lines)
    part_two(lines)


if __name__ == '__main__':
    main()
