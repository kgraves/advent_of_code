import re
import sys


def part_one(seat_nums):
    max_ = 0

    for s in seat_nums:
        row = int(s[:7].replace('B', '1').replace('F', '0'), 2)
        col = int(s[7:].replace('R', '1').replace('L', '0'), 2)

        max_ = max(max_, (row * 8) + col)

    print(max_)


def part_two(seat_nums):
    nums = []

    for s in seat_nums:
        row = int(s[:7].replace('B', '1').replace('F', '0'), 2)
        col = int(s[7:].replace('R', '1').replace('L', '0'), 2)
        nums.append((row * 8) + col)

    snums = sorted(nums)
    for i,n in enumerate(snums):
        if n+1 != snums[i+1]:
            print(n+1)
            return


def main():
    seat_nums = []

    with open('2020/5/input.txt', 'r') as f:
        for line in f:
            seat_nums.append(line)

    part_one(seat_nums)
    part_two(seat_nums)


if __name__ == '__main__':
    main()
