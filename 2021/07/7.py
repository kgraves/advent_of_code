import collections


def bin_search(positions, calc_costs):
    lo = min(positions)
    hi = max(positions)
    mid = int((lo+hi)/2)
    crabs = collections.Counter()
    for p in positions:
        crabs[p] += 1

    left, curr, right = calc_costs(crabs, mid)

    while not(left > curr and right > curr):
        if left < right:
            hi = mid
            mid = int((lo+hi)/2)
        else:
            lo = mid
            mid = int((lo+hi)/2)

        left, curr, right = calc_costs(crabs, mid)

    return curr


def part_one(positions):
    def calc_costs(crabs, mid):
        return (
            (
                sum([(((mid - 1) - c) * crabs[c]) for c in crabs if c < mid - 1]) +
                sum([((c - (mid - 1)) * crabs[c]) for c in crabs if c > mid - 1])
            ),
            (
                sum([((mid - c) * crabs[c]) for c in crabs if c < mid]) +
                sum([((c - mid) * crabs[c]) for c in crabs if c > mid])
            ),
            (
                sum([(((mid + 1) - c) * crabs[c]) for c in crabs if c < mid + 1]) +
                sum([((c - (mid + 1)) * crabs[c]) for c in crabs if c > mid + 1])
            ),
        )

    print(bin_search(positions, calc_costs))


def part_two(positions):
    def calc_costs(crabs, mid):
        return (
            (
                sum([(sum(range(((mid - 1) - c) + 1)) * crabs[c]) for c in crabs if c < mid - 1]) +
                sum([(sum(range((c - (mid - 1)) + 1)) * crabs[c]) for c in crabs if c > mid - 1])
            ),
            (
                sum([(sum(range((mid - c) + 1)) * crabs[c]) for c in crabs if c < mid]) +
                sum([(sum(range((c - mid) + 1)) * crabs[c]) for c in crabs if c > mid])
            ),
            (
                sum([(sum(range(((mid + 1) - c) + 1)) * crabs[c]) for c in crabs if c < mid + 1]) +
                sum([(sum(range((c - (mid + 1)) + 1)) * crabs[c]) for c in crabs if c > mid + 1])
            ),
        )

    print(bin_search(positions, calc_costs))


def main():
    with open('2021/07/input.txt', 'r') as f:
        line = f.read().strip()
        positions = [int(pos) for pos in line.split(',')]

    part_one(positions)
    part_two(positions)


if __name__ == '__main__':
    main()
