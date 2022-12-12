import itertools
import pathlib


def read_input():
    here = pathlib.Path(__file__).parent
    *_, day = __name__.rsplit(".", 1)
    return [
        [int(digit) for digit in line.strip()]
        for line in (here / f"{day}_input.txt").read_text().splitlines()
    ]


def is_visible(grid, x, y):
    w, h = len(grid[0]), len(grid)
    t = grid[y][x]
    return (
        all(grid[y][x1] < t for x1 in range(x))
        or all(grid[y][x1] < t for x1 in range(x + 1, w))
        or all(grid[y1][x] < t for y1 in range(y))
        or all(grid[y1][x] < t for y1 in range(y + 1, h))
    )


def scenic_score(grid, x, y):
    w, h = len(grid[0]), len(grid)
    t = grid[y][x]
    return (
        visibility(t, (grid[y][x1] for x1 in reversed(range(x))))
        * visibility(t, (grid[y][x1] for x1 in range(x + 1, w)))
        * visibility(t, (grid[y1][x] for y1 in reversed(range(y))))
        * visibility(t, (grid[y1][x] for y1 in range(y + 1, h)))
    )


def visibility(t, seq):
    v = 0
    for t1 in seq:
        v += 1
        if t1 >= t:
            break
    return v


def part1():
    grid = read_input()
    return sum(
        is_visible(grid, x, y)
        for x, y in itertools.product(
            range(len(grid[0])),
            range(len(grid)),
        )
    )


def part2():
    grid = read_input()
    return max(
        scenic_score(grid, x, y)
        for x, y in itertools.product(
            range(len(grid[0])),
            range(len(grid)),
        )
    )
