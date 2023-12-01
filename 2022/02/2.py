import re


INPUT_RE = re.compile('^([ABC]) ([XYZ])$')

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'
LOSS = 'loss'
DRAW = 'draw'
WIN = 'win'

PLAYS = {
    'A': ROCK,
    'B': PAPER,
    'C': SCISSORS,
    'X': ROCK,
    'Y': PAPER,
    'Z': SCISSORS,
}

SCORES = {
    ROCK: 1,
    PAPER: 2,
    SCISSORS: 3,
    LOSS: 0,
    DRAW: 3,
    WIN: 6,
}

# theirs -> ours
WIN_MOVES = {
    ROCK: PAPER,
    PAPER: SCISSORS,
    SCISSORS: ROCK,
}
LOSS_MOVES = {
    ROCK: SCISSORS,
    PAPER: ROCK,
    SCISSORS: PAPER,
}


def part_one(lines):
    score = 0

    def outcome(t, o):
        if t == o:
            return DRAW
        elif (
            (t == ROCK and o == SCISSORS) or
            (t == PAPER and o == ROCK) or
            (t == SCISSORS and o == PAPER)
        ):
            return LOSS
        else:
            return WIN

    for line in lines:
        theirs, ours = INPUT_RE.match(line).groups()
        score += SCORES[outcome(PLAYS[theirs], PLAYS[ours])] + SCORES[PLAYS[ours]]

    print(score)


def part_two(lines):
    PLAYS['X'] = LOSS
    PLAYS['Y'] = DRAW
    PLAYS['Z'] = WIN

    score = 0

    def counter(t, o):
        if o == WIN:
            return WIN_MOVES[PLAYS[theirs]]
        elif o == LOSS:
            return LOSS_MOVES[PLAYS[theirs]]
        else:
            return PLAYS[theirs]

    for line in lines:
        theirs, ours = INPUT_RE.match(line).groups()
        our_counter = counter(PLAYS[theirs], PLAYS[ours])

        score += SCORES[PLAYS[ours]] + SCORES[our_counter]

    print(score)


def main():
    lines = []

    with open('2022/02/input.txt', 'r') as f:
        for line in f:
            lines.append(line.strip())

    part_one(lines)
    part_two(lines)


if __name__ == '__main__':
    main()
