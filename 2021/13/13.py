def part_one(coords, folds):
    for dir_, offset in folds:
        new_coords = coords.copy()

        for x, y in coords:
            if dir_ == 'x':
                if x > offset:
                    new_coords.append((offset - (x - offset), y))
                    new_coords.remove((x, y))
            else:
                if y > offset:
                    new_coords.append((x, offset - (y - offset)))
                    new_coords.remove((x, y))

        coords = new_coords

    print(len(set(coords)))


def part_two(coords, folds):
    def get_width_and_height(coords, folds):
        max_x, max_y = 0, 0
        for x, y in coords:
            max_x = max(max_x, x)
            max_y = max(max_y, y)

        return max_x + 1, max_y + 1

    def print_map(coords, folds):
        w, h = get_width_and_height(coords, folds)

        map_ = [['.' for _ in range(w+1)] for _ in range(h)]
        for x, y in coords:
            map_[y][x] = '#'

        for row in map_:
            print(''.join(row))

    for dir_, offset in folds:
        new_coords = coords.copy()

        for x, y in coords:
            if dir_ == 'x':
                if x > offset:
                    if (offset - (x - offset), y) not in new_coords:
                        new_coords.append((offset - (x - offset), y))
                    new_coords.remove((x, y))
            else:
                if y > offset:
                    if (x, offset - (y - offset)) not in new_coords:
                        new_coords.append((x, offset - (y - offset)))
                    new_coords.remove((x, y))

        coords = new_coords

    print_map(coords, folds)


def main():
    coords = []
    folds = []

    with open('2021/13/input.txt', 'r') as f:
        while (line := f.readline().strip()):
            x, y = line.split(',')
            coords.append((int(x), int(y)))

        while (line := f.readline().strip()):
            dir_and_offset = line.split(' ')[-1]
            dir_, offset = dir_and_offset.split('=')
            folds.append((dir_, int(offset)))

    part_one(coords, folds[:1])
    part_two(coords, folds)


if __name__ == '__main__':
    main()
