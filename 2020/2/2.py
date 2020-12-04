import re
import sys


INPUT_RE = re.compile('^(\d+)\-(\d+)\ ([a-z])\:\ ([a-z]+)$')


def part_one(lines):
    for line in lines:
        res = INPUT_RE.match(line)
        min_, max_ = int(res.group(1)), int(res.group(2))
        letter = res.group(3)
        password = res.group(4)

        count = 0
        for l in password:
            count += 1 if letter == l else 0

        if min_ <= count <= max_:
            valids += 1

    print(valids)


def part_two(lines):
    valids = 0

    for line in lines:
        res = INPUT_RE.match(line)
        min_, max_ = int(res.group(1)), int(res.group(2))
        letter = res.group(3)
        password = res.group(4)

        is_first = password[min_-1] == letter
        is_second = password[max_-1] == letter

        valids += 1 if is_first != is_second else 0

    print(valids)


def main():
    valids = 0
    lines = []

    for line in sys.stdin:
        lines.append(line)

    part_one(lines)
    part_two(lines)


if __name__ == '__main__':
    main()
