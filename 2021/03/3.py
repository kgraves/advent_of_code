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


def narrow_candidates(candidates, index, keep_most_common=True):
    ones_count = sum([int(c[index]) for c in candidates])
    are_ones_most_common = ones_count >= (len(candidates) / 2)

    most_common_digit = '1' if are_ones_most_common else '0'
    least_common_digit = '0' if most_common_digit == '1' else '1'
    num_looking_for = most_common_digit if keep_most_common else least_common_digit

    return [c for c in candidates if c[index] == num_looking_for]


def part_two(lines):
    candidates = lines

    o2_candidates = lines[:]
    co2_candidates = lines[:]

    while len(o2_candidates) > 1:
        for i in range(len(o2_candidates[0])):
            o2_candidates = narrow_candidates(o2_candidates, i)

            if len(co2_candidates) == 1:
                break

    while len(co2_candidates) > 1:
        for i in range(len(co2_candidates[0])):
            co2_candidates = narrow_candidates(co2_candidates, i, keep_most_common=False)

            if len(co2_candidates) == 1:
                break

    print(int(o2_candidates[0], 2) * int(co2_candidates[0], 2))

def main():
    lines = []

    with open('2021/03/input.txt', 'r') as f:
        for line in f:
            lines.append(line.strip())

    part_one(lines)
    part_two(lines)


if __name__ == '__main__':
    main()
