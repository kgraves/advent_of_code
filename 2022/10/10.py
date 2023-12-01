def part_one(lines):
    c = 1
    X = 1
    ss = []
    sig_str = [20, 60, 100, 140, 180, 220]

    for l in lines:
        if c in sig_str:
            ss.append(c * X)
        c += 1

        if l.startswith('addx'):
            if c in sig_str:
                ss.append(c * X)
            c += 1

            X += int(l.split(' ')[1])

    print(sum(ss))


def part_two(lines):
    c = 1
    X = 1
    row = ''

    for i, l in enumerate(lines):
        row += '#' if ((c-1) % 40) in range(X-1, X+2) else '.'
        c += 1
        if (c-1) % 40 == 0:
            print(row)
            row = ''

        if l.startswith('addx'):
            row += '#' if ((c-1) % 40) in range(X-1, X+2) else '.'
            c += 1
            if (c-1) % 40 == 0:
                print(row)
                row = ''

            X += int(l.split(' ')[1])


def main():
    lines = []

    with open('2022/10/input.txt', 'r') as f:
        for line in f:
            lines.append(line.strip())

    part_one(lines)
    part_two(lines)


if __name__ == '__main__':
    main()
