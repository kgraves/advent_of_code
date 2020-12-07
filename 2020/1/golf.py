import operator
import sys
from itertools import combinations

def part_one(i):
    print([c[0]*c[1] for c in combinations(i,2) if sum(c)==2020])


def part_two(i):
    print([c[0]*c[1]*c[2] for c in combinations(i,3) if sum(c)==2020])


def main():
    i = [int(l.strip()) for l in sys.stdin]

    part_one(i)
    part_two(i)


main()
