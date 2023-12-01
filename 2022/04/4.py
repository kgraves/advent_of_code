import re


INPUT_RE = re.compile(r'^(\d+)-(\d+),(\d+)-(\d+)$')


def part_one(lines):
    c = 0
    for line in lines:
        fb, fe, sb, se = [int(i) for i in INPUT_RE.match(line).groups()]
        f = set(range(fb, fe+1))
        s = set(range(sb, se+1))
        if f <= s or s <= f:
            c += 1

    print(c)


def part_two(lines):
    c = 0
    for line in lines:
        fb, fe, sb, se = [int(i) for i in INPUT_RE.match(line).groups()]
        f = set(range(fb, fe+1))
        s = set(range(sb, se+1))
        if f & s:
            c += 1

    print(c)


def main():
    lines = []

    with open('2022/04/input.txt', 'r') as f:
        for line in f:
            lines.append(line.strip())

    part_one(lines)
    part_two(lines)


if __name__ == '__main__':
    main()
