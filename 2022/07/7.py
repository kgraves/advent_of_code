import re
from collections import defaultdict

INPUT_RE = re.compile(r'^\d+\ ')
MAX_SIZE = 100_000
DISC_SIZE = 70_000_000
UNUSED_NEEDED = 30_000_000


def dir_struct(lines):
    struct = {}
    cwd = []

    for line in lines:
        if line.startswith('$ cd'):
            if '/' in line:
                continue
            if '..' in line:
                cwd.pop()
            else:
                cwd.append(line[5:])
        if line.startswith('dir'):
            _, name = line.split(' ')

            temp = struct
            for d in cwd:
                temp = temp[d]

            temp[name] = {}
        if INPUT_RE.match(line):
            size, name = line.split(' ')

            temp = struct
            for d in cwd:
                temp = temp[d]

            temp[name] = size

    return struct


def walk_dir(struct, candidates):
    size = 0
    for k, v in struct.items():
        if isinstance(v, dict):
            d_size = walk_dir(v, candidates)
            candidates.append(d_size)
            size += d_size
        else:
            assert isinstance(v, str)
            size += int(v)

    return size


def part_one(lines):
    struct = dir_struct(lines)
    cs = []
    total_size = walk_dir(struct, cs)
    cs.append(total_size)

    print(sum(c for c in cs if c <= MAX_SIZE))


def part_two(lines):
    struct = dir_struct(lines)
    cs = []
    total_size = walk_dir(struct, cs)
    cs.append(total_size)

    free_size = DISC_SIZE - total_size
    needed_size = UNUSED_NEEDED - free_size

    for c in sorted(cs):
        if c > needed_size:
            print(c)
            return


def part_one_take_two(lines):
    cwd = ['/']
    sizes = defaultdict(int)

    for line in lines[1:]:
        if line.startswith('$ cd'):
            if '..' in line:
                cwd.pop()
            else:
                cwd.append(line[5:])
        if INPUT_RE.match(line):
            size, name = line.split(' ')

            for i in range(len(cwd)):
                sizes['.'.join(cwd[:len(cwd)-i])] += int(size)

    print(sum(s for d, s in sizes.items() if s <= MAX_SIZE))


def part_two_take_two(lines):
    cwd = ['/']
    sizes = defaultdict(int)

    for line in lines[1:]:
        if line.startswith('$ cd'):
            if '..' in line:
                cwd.pop()
            else:
                cwd.append(line[5:])
        elif INPUT_RE.match(line):
            size, name = line.split(' ')
            for i in range(len(cwd)):
                sizes['.'.join(cwd[:len(cwd)-i])] += int(size)

    needed_size = UNUSED_NEEDED - (DISC_SIZE - sizes['/'])
    for k, v in sorted(sizes.items(), key=lambda s: s[1]):
        if v > needed_size:
            print(v)
            return


def main():
    lines = []

    with open('2022/07/input.txt', 'r') as f:
        lines = f.readlines()

    part_one(lines)
    part_one_take_two(lines)
    part_two(lines)
    part_two_take_two(lines)


if __name__ == '__main__':
    main()
