import collections
import sys
from dataclasses import dataclass


def part_one(num_lists, outputs):
    print(sum(len(n) in [2, 3, 4, 7] for o in outputs for n in o))


def part_two(num_lists, output):
    def sort(s):
        return "".join(sorted(s))

    grand_total = 0
    for i, nl in enumerate(num_lists):
        translator = dict()
        one = four = seven = eight = None

        for n in nl:
            if len(n) == 2:
                one = n
                translator[sort(n)] = '1'
            elif len(n) == 3:
                seven = n
                translator[sort(n)] = '7'
            elif len(n) == 4:
                four = n
                translator[sort(n)] = '4'
            elif len(n) == 7:
                eight = n
                translator[sort(n)] = '8'

        five_lengths = [n for n in nl if len(n) == 5]
        three = [f for f in five_lengths if set(f) & set(one) == set(one)][0]
        translator[sort(three)] = '3'

        six_lengths = [n for n in nl if len(n) == 6]
        six = [s for s in six_lengths if set(s) & set(one) != set(one)][0]
        translator[sort(six)] = '6'

        nine_lookalike = ''.join(set(seven) | set(four))
        nine = [s for s in six_lengths if len(set(s) - set(nine_lookalike)) == 1][0]
        translator[sort(nine)] = '9'

        upper_right = set(one) - set(six)
        two_or_five_candidates = set(five_lengths) - set([three])
        two = [f for f in two_or_five_candidates if len(set(f) & upper_right) == 1][0]
        translator[sort(two)] = '2'

        five = list(two_or_five_candidates - set([two]))[0]
        translator[sort(five)] = '5'

        zero = [z for z in six_lengths if z not in [six, nine]][0]
        translator[sort(zero)] = '0'

        translated = ''.join([translator[sort(o)] for o in output[i]])
        grand_total += int(translated)

    print(grand_total)


def main():
    lines = []
    nums = []
    outputs = []

    with open('2021/08/input.txt', 'r') as f:
        for line in f:
            ns, os = line.split('|')
            nums.append(ns.strip().split(' '))
            outputs.append(os.strip().split(' '))

    part_one(nums, outputs)
    part_two(nums, outputs)


if __name__ == '__main__':
    main()
