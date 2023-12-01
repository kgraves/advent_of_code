import collections
import functools
import itertools
import math
import operator
import re
import sys
from dataclasses import dataclass

INPUT_RE = re.compile(r'^(\d+),(\d+)\ -\>\ (\d+),(\d+)$')


# def take(iterable, n):
#     iterator = iter(iterable)

#     while slice_ := list(itertools.islice(iterator, n)):
#         yield slice_

@dataclass
class Monke:
    si: list
    op: str
    factor: int
    div: int
    tmn: int
    fmn: int

    def __repr__(self):
        return f'{[i for i in self.si]}'


OPS = {
    '+': operator.add,
    '*': operator.mul,
}


def process_lines(lines):
    monkes = []
    it = iter(lines)

    while slice_ := list(itertools.islice(it, 7)):
        si = [int(i) for i in slice_[1].split(': ')[1].split(', ')]
        op = slice_[2].split(' = ')[1].split(' ')
        div = int(slice_[3].split(' ')[-1])
        true_monke_num = int(slice_[4].split(' ')[-1])
        false_monke_num = int(slice_[5].split(' ')[-1])

        monkes.append(
            Monke(si, op, op, div, true_monke_num, false_monke_num)
        )

    return monkes


def part_one(lines):
    monkes = process_lines(lines)
    activities = [0] * len(monkes)

    for r in range(20):
        for idx, m in enumerate(monkes):
            activities[idx] += len(m.si)
            for i in m.si:
                # monke inspect
                lhs = int(m.op[0]) if m.op[0].isnumeric() else i
                rhs = int(m.op[2]) if m.op[2].isnumeric() else i
                inspect_worry = OPS[m.op[1]](lhs, rhs)

                # monke think
                inspect_worry //= 3

                # monke throw
                nm = m.tmn if inspect_worry % m.div == 0 else m.fmn
                monkes[nm].si.append(inspect_worry)

            m.si = []

    sa = sorted(activities, reverse=True)
    print(sa[0] * sa[1])


def part_two(lines):
    monkes = process_lines(lines)
    activities = [0] * len(monkes)

    fac = functools.reduce(operator.mul, [m.div for m in monkes])

    for r in range(10_000):
        for idx, m in enumerate(monkes):
            activities[idx] += len(m.si)
            for i in m.si:
                # monke inspect
                lhs = int(m.op[0]) if m.op[0].isnumeric() else i
                rhs = int(m.op[2]) if m.op[2].isnumeric() else i
                inspect_worry = OPS[m.op[1]](lhs, rhs)

                # monke think
                inspect_worry %= fac

                # monke throw
                nm = m.tmn if inspect_worry % m.div == 0 else m.fmn
                monkes[nm].si.append(inspect_worry)

            m.si = []

    sa = sorted(activities, reverse=True)
    print(sa[0] * sa[1])


def main():
    lines = []

    with open('2022/11/input.txt', 'r') as f:
        for line in f:
            lines.append(line.strip())

    part_one(lines)
    part_two(lines)


if __name__ == '__main__':
    main()
