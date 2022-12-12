import pathlib

ROCK = "A"
PAPER = "B"
SCISSORS = "C"
SHAPE_SCORE = {ROCK: 1, PAPER: 2, SCISSORS: 3}
SHAPE_BEATS = {ROCK: SCISSORS, SCISSORS: PAPER, PAPER: ROCK}
SHAPE_LOSES = {v: k for k, v in SHAPE_BEATS.items()}
PART1_SHAPE_MAP = {"X": ROCK, "Y": PAPER, "Z": SCISSORS}
LOSE = "X"
DRAW = "Y"
WIN = "Z"


def read_input():
    here = pathlib.Path(__file__).parent
    *_, day = __name__.rsplit(".", 1)
    file = here / f"{day}_input.txt"
    return [line.split() for line in file.read_text().splitlines()]


def score(x, y):
    return SHAPE_SCORE[y] + (3 if x == y else 0 if SHAPE_BEATS[x] == y else 6)


def part1():
    return sum(score(x, PART1_SHAPE_MAP[y]) for x, y in read_input())


def part2():
    return sum(
        score(x, (x if y == DRAW else SHAPE_BEATS[x] if y == LOSE else SHAPE_LOSES[x]))
        for x, y in read_input()
    )
