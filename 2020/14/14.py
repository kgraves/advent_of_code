import re
import sys


MASK_RE = re.compile('mask = (.+)')
PROG_RE = re.compile('mem\[(\d+)\] = (\d+)')


def part_one(mask, prog):
    mem = {}

    for addr, val in prog:
        mem[addr] = '0' * 36
        # TODO never completed


def part_two(_, ids):
    print()


def main():
    lines = []
    with open('2020/14/sample.txt', 'r') as f:
        mask, = MASK_RE.match(f.readline().strip()).groups()
        prog = []
        for l in f:
            addr, num = PROG_RE.match(l.strip()).groups()
            prog.append((addr, num))

    part_one(mask, prog)
    part_two(mask, prog)


if __name__ == '__main__':
    main()
