import functools
import operator


LETTER_MAP = {}
for i, index in enumerate(range(ord('a'), ord('z')+1)):
    LETTER_MAP[chr(index)] = i + 1
for i, index in enumerate(range(ord('A'), ord('Z')+1)):
    LETTER_MAP[chr(index)] = i + 26 + 1


def part_one(lines):
    p = 0
    for line in lines:
        c = set(line[:len(line)//2]) & set(line[len(line)//2:])
        p += LETTER_MAP[c.pop()]

    print(p)


def part_two(lines):
    p = 0
    for st in range(0, len(lines), 3):
        c = functools.reduce(operator.and_, [set(l) for l in lines[st:st+3]])
        p += LETTER_MAP[c.pop()]

    print(p)


def main():
    lines = []

    with open('2022/03/input.txt', 'r') as f:
        for line in f:
            lines.append(line.strip())

    part_one(lines)
    part_two(lines)


if __name__ == '__main__':
    main()
