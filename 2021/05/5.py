import collections
import re
from dataclasses import dataclass


INPUT_RE = re.compile('^(\d+),(\d+)\ -\>\ (\d+),(\d+)$')


@dataclass
class Vector:
    x1: int
    y1: int
    x2: int
    y2: int

    def is_vertical(self):
        return self.x2 - self.x1 == 0

    def is_horizontal(self):
        return self.y2 - self.y1 == 0

    def coords(self):
        if self.is_vertical():
            y_start = min(self.y1, self.y2)
            y_end = max(self.y1, self.y2)
            curr_x = self.x1
            for curr_y in range(y_start, y_end+1):
                yield (curr_x, curr_y)
        else:
            slope = (self.y2 - self.y1) / (self.x2 - self.x1)
            inter = self.y1 - (slope * self.x1)

            x_start = min(self.x1, self.x2)
            x_end = max(self.x1, self.x2)
            for curr_x in range(x_start, x_end+1):
                curr_y = int((slope * curr_x) + inter)
                yield (curr_x, curr_y)


def part_one(vectors):
    vecs = [v for v in vectors if v.is_vertical() or v.is_horizontal()]
    points = collections.Counter()

    for v in vecs:
        for coord_tuple in v.coords():
            points[coord_tuple] += 1

    peligroso = sum(int(o >= 2) for c,o in points.items())
    print(peligroso)


def part_two(vectors):
    points = collections.Counter()

    for v in vectors:
        for coord_tuple in v.coords():
            points[coord_tuple] += 1

    peligroso = sum(int(o >= 2) for c,o in points.items())
    print(peligroso)


def main():
    vectors = []

    with open('2021/05/input.txt', 'r') as f:
        for line in f:
            res = INPUT_RE.match(line.strip())

            vectors.append(
                Vector(
                    int(res.group(1)),
                    int(res.group(2)),
                    int(res.group(3)),
                    int(res.group(4)),
                )
            )

    part_one(vectors)
    part_two(vectors)


if __name__ == '__main__':
    main()
