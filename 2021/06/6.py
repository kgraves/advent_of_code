import collections


def part_one(fishys, end):
    clock = 1
    fishy_updates = fishys.copy()

    while clock <= end:
        num_new_fishys = 0

        for age, num_fishys in fishys.items():
            if age == 0:
                fishy_updates[age] -= num_fishys
                fishy_updates[6] += num_fishys
                num_new_fishys += num_fishys
            else:
                fishy_updates[age] -= num_fishys
                fishy_updates[age-1] += num_fishys

        fishy_updates[8] += num_new_fishys
        fishys = fishy_updates.copy()
        clock += 1

    print(sum(fishys.values()))


def part_two(fishys, end):
    # same as first part, with larger numbers
    pass


def main():
    with open('2021/06/input.txt', 'r') as f:
        line = f.read().strip()
        fishys = collections.Counter()
        for age in line.split(','):
                fishys[int(age)] += 1

    part_one(fishys, 256)


if __name__ == '__main__':
    main()
