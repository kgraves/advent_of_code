import math


def part_one(lines):
    num_digits = len(lines[0])
    ones = [0] * num_digits
    gamma = [0] * num_digits
    epsilon = [0] * num_digits

    for line in lines:
        for i, digit in enumerate(line):
            ones[i] += int(digit)

    half_length_lines = math.ceil(len(lines) / 2)
    for i, count in enumerate(ones):
        gamma[i] = 1 if count >= half_length_lines else 0
        epsilon[i] = int(not gamma[i])

    gamma_int = int("".join([str(i) for i in gamma]), 2)
    epsilon_int = int("".join([str(i) for i in epsilon]), 2)

    print(gamma_int * epsilon_int)


def part_two(lines):
    # TODO
    pass


def main():
    lines = []

    with open('2021/03/input.txt', 'r') as f:
        for line in f:
            lines.append(line.strip())

    part_one(lines)
    # part_two(lines)


if __name__ == '__main__':
    main()
