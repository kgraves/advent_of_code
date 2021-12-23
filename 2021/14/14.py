import collections
import itertools


def iter_pairs(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def count_pairs(pairs, rules, counts):
    new_pairs = pairs.copy()

    for (a, c), count in pairs.items():
        b = rules[(a, c)]
        new_pairs[a + b] += count
        new_pairs[b + c] += count
        new_pairs[a + c] -= count
        counts[b] += count

    return new_pairs, counts


def part_one(template, rules):
    counts = collections.Counter(template)
    pairs = collections.Counter([a + b for a, b in iter_pairs(template)])

    for _ in range(10):
        pairs, counts = count_pairs(pairs, rules, counts)

    print(max(counts.values()) - min(counts.values()))


def part_two(template, rules):
    counts = collections.Counter(template)
    pairs = collections.Counter([a + b for a, b in iter_pairs(template)])

    for _ in range(40):
        pairs, counts = count_pairs(pairs, rules, counts)

    print(max(counts.values()) - min(counts.values()))


def main():
    template = ''
    rules = dict()

    with open('2021/14/input.txt', 'r') as f:
        template = f.readline().strip()
        f.readline()

        while (line := f.readline().strip()):
            pair, result = line.split(' -> ')
            rules[(pair[0], pair[1])] = result

    part_one(template, rules)
    part_two(template, rules)


if __name__ == '__main__':
    main()
