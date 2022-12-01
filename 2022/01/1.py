def part_one(lines):
    max_ = 0
    curr = 0

    for line in lines:
        if not line.strip():
            max_ = max(max_, curr)
            curr = 0
            continue

        curr += int(line.strip())

    print(max_)


def part_two(lines):
    top_three = [0, 0, 0]
    curr = 0

    def try_top_three(tops, candidate):
        for i in range(len(tops)):
            if candidate > tops[i]:
                candidate, tops[i] = tops[i], candidate

    for line in lines:
        if not line.strip():
            try_top_three(top_three, curr)
            curr = 0
            continue

        curr += int(line.strip())

    # process the last group
    try_top_three(top_three, curr)

    print(sum(top_three))


def main():
    lines = []

    with open('2022/01/input.txt', 'r') as f:
        for line in f:
            lines.append(line)

    part_one(lines)
    part_two(lines)


if __name__ == '__main__':
    main()
