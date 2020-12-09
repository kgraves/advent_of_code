import re
import sys


def part_one(lines, length):
    preamble = lines[:length]

    for i in range(len(preamble), len(lines)):
        last_n = lines[i-length:i]

        found = False
        for n in last_n:
            if lines[i]-n in last_n:
                found = True
                break

        if not found:
            return lines[i]


def part_two(lines, length, goal):
    for i, num in enumerate(lines):
        width = 1

        while width < len(lines):
            attempt = lines[i:i+width]
            sum_attempt = sum(attempt)

            if sum_attempt == goal:
                answer = min(attempt) + max(attempt)
                print(answer)
                return
            elif sum_attempt > goal:
                break

            width += 1


def main():
    lines = []
    with open('2020/9/input.txt', 'r') as f:
        for line in f:
            lines.append(int(line.strip()))

    answer = part_one(lines, 25)
    print(answer)

    part_two(lines, 25, answer)


if __name__ == '__main__':
    main()
