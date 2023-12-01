DIRS = {
    'R': (1, 0),
    'D': (0, -1),
    'L': (-1, 0),
    'U': (0, 1),
}


def clamp(x, min_=-1, max_=1):
    return min(max_, max(min_, x))


def part_one(lines):
    hx, hy = 0, 0
    tx, ty = 0, 0
    tv = set([(0, 0)])

    for l in lines:
        dir_, num = l.split()

        for i in range(int(num)):
            dx, dy = DIRS[dir_]
            hx += dx
            hy += dy

            if abs(hx-tx) > 1 or abs(hy-ty) > 1:
                tx += clamp(hx - tx)
                ty += clamp(hy - ty)
                tv.add((tx, ty))

    print(len(tv))


def part_two(lines):
    ts = [(0, 0)] * 10
    tv = set([(0, 0)])

    for l in lines:
        dir_, num = l.split()

        for i in range(int(num)):
            dx, dy = DIRS[dir_]
            ts[0] = (ts[0][0] + dx, ts[0][1] + dy)

            for i in range(1, len(ts)):
                prev = ts[i-1]
                t = ts[i]

                if abs(prev[0]-t[0]) > 1 or abs(prev[1]-t[1]) > 1:
                    dx = clamp(prev[0] - t[0])
                    dy = clamp(prev[1] - t[1])
                    ts[i] = (t[0] + dx, t[1] + dy)

                    if i == 9:
                        tv.add(ts[i])

    print(len(tv))


def main():
    lines = []

    with open('2022/09/input.txt', 'r') as f:
        for line in f:
            lines.append(line.strip())

    part_one(lines)
    part_two(lines)


if __name__ == '__main__':
    main()
