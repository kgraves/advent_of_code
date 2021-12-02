from dataclasses import dataclass
import sys

@dataclass
class SubOne:
    x: int = 0
    y: int = 0
    dirs = {
        'forward': (1, 0),
        'down': (0, 1),
        'up': (0, -1),
    }

    def move(self, dir_, num):
        dx, dy = self.dirs[dir_]
        self.x += dx * num
        self.y += dy * num


@dataclass
class SubTwo:
    x: int = 0
    y: int = 0
    aim: int = 0

    def down(self, num):
        self.aim += num

    def up(self, num):
        self.aim -= num

    def forward(self, num):
        self.x += num
        self.y += self.aim * num


def part_one(lines):
    sub = SubOne()

    for line in lines:
        dir_, num = line.split(' ')
        sub.move(dir_, int(num))

    print(sub.x * sub.y)


def part_two(lines):
    sub = SubTwo()

    for line in lines:
        dir_, num = line.split(' ')
        getattr(sub, dir_)(int(num))

    print(sub.x * sub.y)


def main():
    lines = []

    with open('2021/02/input.txt', 'r') as f:
        for line in f:
            lines.append(line.strip())

    part_one(lines)
    part_two(lines)


if __name__ == '__main__':
    main()
