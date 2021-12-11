def get_dirs(y, x, h, w):
    candidates = [(-1, 0), (-1, 1), (1, 0), (1, 1), (0, 1), (1, -1), (0, -1), (-1, -1)]
    return [(y + dy, x + dx) for dy, dx in candidates if (0 <= (y + dy) < h) and (0 <= (x + dx) < w )]


def flash(map_, flashers):
    h, w = len(map_), len(map_[0])
    queue = flashers
    flashed = set(flashers)
    count = len(flashers)

    while len(queue) > 0:
        r, c = queue.pop()

        for dr, dc in get_dirs(r, c, h , w):
            map_[dr][dc] += 1

            if map_[dr][dc] > 9 and (dr, dc) not in flashed:
                queue.append((dr, dc))
                flashed.add((dr, dc))
                count += 1

    return count


def part_one(lines):
    map_ = [[int(d) for d in line] for line in lines]
    h, w = len(map_), len(map_[0])
    count = 0

    for i in range(100):
        flashers = []
        for r in range(h):
            for c in range(w):
                map_[r][c] += 1
                if map_[r][c] > 9:
                    flashers.append((r, c))

        count += flash(map_, flashers)

        for r in range(h):
            for c in range(w):
                if map_[r][c] > 9:
                    map_[r][c] = 0

    print(count)


def part_two(lines):
    map_ = [[int(d) for d in line] for line in lines]
    h, w = len(map_), len(map_[0])

    day = 1
    while True:
        flashers = []
        for r in range(h):
            for c in range(w):
                map_[r][c] += 1
                if map_[r][c] > 9:
                    flashers.append((r, c))

        flash(map_, flashers)

        for r in range(h):
            for c in range(w):
                if map_[r][c] > 9:
                    map_[r][c] = 0

        if sum(sum(r) for r in map_) == 0:
            print(day)
            break

        day += 1


def main():
    lines = []

    with open('2021/11/input.txt', 'r') as f:
        for line in f:
            lines.append(line.strip())

    part_one(lines)
    part_two(lines)


if __name__ == '__main__':
    main()
