# import functools
# import operator


def part_one(lines):
    for i in range(0, len(lines[0])):
        if len(set(lines[0][i:i+4])) == 4:
            print(i + 4)
            return


def part_one_golf(lines):
    print([i+4 for i in range(0, len(lines[0])) if len(set(lines[0][i:i+4])) == 4][0])


# def part_one(lines):
#     for i in range(0, len(lines[0])):
#         l = [set(c) for c in lines[0][i:i+4]]
#         if len(functools.reduce(operator.or_, l)) == 4:
#             print(i + 4)
#             return


def part_two(lines):
    for i in range(0, len(lines[0])):
        if len(set(lines[0][i:i+14])) == 14:
            print(i + 14)
            return


# def part_two(lines):
#     for i in range(0, len(lines[0])):
#         l = [set(c) for c in lines[0][i:i+14]]
#         if len(functools.reduce(operator.or_, l)) == 14:
#             print(i + 14)
#             return


def main():
    lines = []

    with open('2022/06/input.txt', 'r') as f:
        for line in f:
            lines.append(line.strip())

    part_one(lines)
    part_two(lines)


if __name__ == '__main__':
    main()
