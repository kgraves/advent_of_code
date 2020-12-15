import re
import sys


def part_one(lines):
    x, y = 0, 0
    curr_angle = 90
    compass = {
        0: 'N',
        90: 'E',
        180: 'S',
        270: 'W',
    }

    for line in lines:
        instr, unit = line[0], int(line[1:])

        if instr == 'F':
            instr = compass[curr_angle]

        if instr == 'N':
            y -= unit
        elif instr == 'E':
            x += unit
        elif instr == 'S':
            y += unit
        elif instr == 'W':
            x -= unit
        elif instr == 'L':
            curr_angle = (curr_angle - unit) % 360
        elif instr == 'R':
            curr_angle = (curr_angle + unit) % 360

    print(abs(x) + abs(y))


def part_two(lines):
    waypoint_x, waypoint_y = 10, 1
    ship_x, ship_y = 0, 0
    mults = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0),
    }

    for line in lines:
        instr, unit = line[0], int(line[1:])

        if instr == 'F':
            ship_x += waypoint_x * unit
            ship_y += waypoint_y * unit

        if instr in ('N', 'E', 'S', 'W'):
            xmult, ymult = mults[instr]
            waypoint_x += xmult * unit
            waypoint_y += ymult * unit
        elif instr in ('R', 'L'):
            right_steps = unit // 90

            if instr == 'L':
                right_steps = 4 - right_steps

            for s in range(right_steps):
                waypoint_x, waypoint_y = waypoint_y, waypoint_x*-1

    print(abs(ship_x) + abs(ship_y))


def main():
    lines = []
    with open('2020/12/input.txt', 'r') as f:
        for line in f:
            lines.append(line.strip())

    part_one(lines)
    part_two(lines)


if __name__ == '__main__':
    main()
