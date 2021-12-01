import re
import sys


def part_one(time, ids):
    min_wait = 9999999999
    bus = None

    for id_ in ids:
        if id_ == 'x':
            continue

        mins = id_ - time % id_
        if mins < min_wait:
            min_wait = mins
            bus = id_

    print(min_wait * bus)


def part_two(_, ids):
    time = 1
    int_ = 1
    bus_ids = [(i, id_) for i,id_ in enumerate(ids) if id_ != 'x']

    for bus in bus_ids:
        while (time + bus[0]) % bus[1] != 0:
            time += int_
        int_ *= bus[1]

    print(time)


def main():
    lines = []
    with open('2020/13/input.txt', 'r') as f:
        time = int(f.readline().strip())
        ids = []
        for id_ in f.readline().strip().split(','):
            ids.append(int(id_) if id_.isnumeric() else id_)

    part_one(time, ids)
    part_two(time, ids)


if __name__ == '__main__':
    main()
