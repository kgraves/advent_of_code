MARKER = -1
NUM_ROWS = 5
NUM_COLS = 5


class Board:
    def __init__(self, board):
        self.rows = [[0] * NUM_COLS for i in range(NUM_ROWS)]
        self.cols = [[0] * NUM_ROWS for i in range(NUM_COLS)]

        for i in range(NUM_ROWS):
            for j in range(NUM_COLS):
                self.rows[i][j] = board[i][j]
                self.cols[j][i] = board[j][i]

    def mark(self, num):
        for i, row in enumerate(self.rows):
            for j, _ in enumerate(row):
                if self.rows[i][j] == num:
                    self.rows[i][j] = MARKER
                    self.cols[j][i] = MARKER

    def is_winner(self):
        for row in self.rows:
            if sum(n for n in row if not n == MARKER) == 0:
                return True

        for col in self.cols:
            if sum(n for n in col if not n == MARKER) == 0:
                return True

    def sum(self):
        return sum(d for row in self.rows for d in row if not d == MARKER)


def part_one(drawn, boards):
    bs = [Board(b) for b in boards]

    for d in drawn:
        for b in bs:
            b.mark(d)

            if b.is_winner():
                print(b.sum() * d)
                return


def part_two(lines):
    # TODO
    pass


def main():
    lines = []
    drawn = []
    boards = []

    with open('2021/04/input.txt', 'r') as f:
        drawn = [int(d) for d in f.readline().split(',')]
        f.readline()  # read blank line

        board = []
        for line in f:
            if line.strip() == '':
                boards.append(board)
                board = []
            else:
                board.append([int(d) for d in line.split()])

        # capture last board
        if not board == []:
            boards.append(board)

    part_one(drawn, boards)
    # part_two(lines)


if __name__ == '__main__':
    main()
