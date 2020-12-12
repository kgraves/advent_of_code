import copy
import re
import sys


def print_seats(seats):
    for row in seats:
        print(row)


def part_one(seats):
    def get_surrounding_seats(seats, i, j):
        valid_i = range(0, len(seats))
        valid_j = range(0, len(seats[0]))
        candidates = []

        for i,j in [
            (i-1, j-1), (i-1, j), (i-1, j+1),
            (i,   j-1),           (i,   j+1),
            (i+1, j-1), (i+1, j), (i+1, j+1),
        ]:
            if (i in valid_i and j in valid_j):
                candidates.append((i,j))

        return candidates

    is_stable = False
    while not is_stable:
        to_fill = []
        to_unfill = []

        for i in range(len(seats)):
            for j in range(len(seats[i])):
                candidates = get_surrounding_seats(seats, i, j)

                if seats[i][j] == 'L':
                    if all(seats[x][y] in ('.', 'L') for x,y in candidates):
                        to_fill.append((i,j))
                elif seats[i][j] == '#':
                    if sum(int(seats[x][y] == '#') for x,y in candidates) >= 4:
                        to_unfill.append((i,j))

        if len(to_fill) == 0 and len(to_unfill) == 0:
            is_stable = True

        for i,j in to_fill:
            seats[i][j] = '#'

        for i,j in to_unfill:
            seats[i][j] = 'L'

        to_fill = []
        to_unfill = []

    count = sum(int(seat == '#') for row in seats for seat in row)
    print(count)


def part_two(seats):
    def get_visible_seats(seats, i, j):
        valid_i = range(0, len(seats))
        valid_j = range(0, len(seats[0]))
        candidates = []
        steps = [
            (-1, -1), (-1, 0), (-1, 1),
            (0,  -1),          (0,  1),
            (1,  -1), (1,  0), (1,  1),
        ]

        for step in steps:
            x, y = i, j
            found = None

            x += step[0]
            y += step[1]
            while x in valid_i and y in valid_j:
                if seats[x][y] in ('#', 'L'):
                    candidates.append((x,y))
                    break

                x += step[0]
                y += step[1]

        return candidates

    is_stable = False
    while not is_stable:
        to_fill = []
        to_unfill = []

        for i in range(len(seats)):
            for j in range(len(seats[i])):
                candidates = get_visible_seats(seats, i, j)

                if seats[i][j] == 'L':
                    if all(seats[x][y] in ('.', 'L') for x,y in candidates):
                        to_fill.append((i,j))
                elif seats[i][j] == '#':
                    if sum(int(seats[x][y] == '#') for x,y in candidates) >= 5:
                        to_unfill.append((i,j))

        if len(to_fill) == 0 and len(to_unfill) == 0:
            is_stable = True

        for i,j in to_fill:
            seats[i][j] = '#'

        for i,j in to_unfill:
            seats[i][j] = 'L'

        to_fill = []
        to_unfill = []

    count = sum(int(seat == '#') for row in seats for seat in row)
    print(count)


def main():
    lines = []
    with open('2020/11/input.txt', 'r') as f:
        for line in f:
            lines.append(list(line.strip()))

    part_one(copy.deepcopy(lines))
    part_two(lines)


if __name__ == '__main__':
    main()
