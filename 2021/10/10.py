matches = {
    '[': ']',
    '{': '}',
    '(': ')',
    '<': '>',
}


def process_line(line):
    stack = []

    for c in line:
        if c in matches:
            stack.append(c)
        elif c != matches[stack[-1]]:
            return c, stack
        else:
            stack.pop()

    return None, stack


def part_one(lines):
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    score = 0

    for l in lines:
        c, stack = process_line(l)
        score += points[c] if c else 0

    print(score)


def part_two(lines):
    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }
    scores = []

    for l in lines:
        c, stack = process_line(l)

        if c is None:
            score = 0
            for s in stack[::-1]:
                score *= 5
                score += points[matches[s]]

            scores.append(score)

    mid = (len(scores) - 1) // 2
    print(sorted(scores)[mid])


def main():
    lines = []

    with open('2021/10/input.txt', 'r') as f:
        for line in f:
            lines.append(line.strip())

    part_one(lines)
    part_two(lines)


if __name__ == '__main__':
    main()
