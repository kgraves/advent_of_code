import math
import re


MOVE_RE = re.compile(r'^move (\d+) from (\d+) to (\d+)$')


def parse_input(lines):
    stacks = [[] for _ in range(math.ceil(len(lines[0]) / 4))]
    moves = []
    it = iter(lines)

    ids = list(range(1, len(lines[0]), 4))
    while (l := next(it, None)) and not l.startswith(' 1'):
        for i, p in enumerate(l[id] for id in ids):
            if p.strip():
                stacks[i].insert(0, p)

    next(it)

    while (l := next(it, None)):
        num, src, dest = [int(i) for i in MOVE_RE.match(l.strip()).groups()]
        moves.append((num, src, dest))

    return stacks, moves


def part_one(lines):
    stacks, moves = parse_input(lines)

    for num, src, dest in moves:
        for i in range(num):
            stacks[dest-1].append(stacks[src-1].pop())

    print(''.join([s[-1] for s in stacks if s]))


def part_two(lines):
    stacks, moves = parse_input(lines)

    for num, src, dest in moves:
        stacks[dest-1].extend(stacks[src-1][-num:])
        stacks[src-1] = stacks[src-1][:-num]

    print(''.join([s[-1] for s in stacks if s]))


def main():
    lines = []

    with open('2022/05/sample.txt', 'r') as f:
        for line in f:
            lines.append(line)

    part_one(lines)
    part_two(lines)


if __name__ == '__main__':
    main()


def part_one_backup(lines):
    stacks = [[], [], [], [], [], [], [], [], [], []]

    for line in lines:
        if '[' in line:
            for i, p in enumerate(range(0, len(line), 4)):
                if line[p:p+4].strip().replace('[', '').replace(']', '') == '':
                    continue
                stacks[i].insert(0, line[p:p+4].strip().replace('[', '').replace(']', ''))
        if line.startswith(' 1') or line.strip() == '':
            continue
        if line.startswith('move'):
            num, src, dest = [int(i) for i in MOVE_RE.match(line.strip()).groups()]

            for i in range(num):
                stacks[dest-1].append(stacks[src-1].pop())

    print(''.join([s[-1] for s in stacks if s]))


def part_two_newest_backup(lines):
    stacks, moves = parse_input(lines)

    for num, src, dest in moves:
        temp = [stacks[src-1].pop() for _ in range(num)]
        for i in range(num):
            stacks[dest-1].append(temp.pop())

    print(''.join([s[-1] for s in stacks if s]))


def part_two_backup(lines):
    stacks = [[], [], [], [], [], [], [], [], [], []]

    for line in lines:
        if '[' in line:
            for i, p in enumerate(range(0, len(line), 4)):
                if line[p:p+4].strip().replace('[', '').replace(']', '') == '':
                    continue
                stacks[i].insert(0, line[p:p+4].strip().replace('[', '').replace(']', ''))
        if line.startswith(' 1') or line.strip() == '':
            continue
        if line.startswith('move'):
            num, src, dest = [int(i) for i in MOVE_RE.match(line.strip()).groups()]

            temp = []
            for i in range(num):
                temp.append(stacks[src-1].pop())
            for i in range(num):
                stacks[dest-1].append(temp.pop())

    print(''.join([s[-1] for s in stacks if s]))
