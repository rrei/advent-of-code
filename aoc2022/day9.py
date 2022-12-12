import pathlib

DIRECTIONS = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}


def read_input():
    here = pathlib.Path(__file__).parent
    *_, day = __name__.rsplit(".", 1)
    motions = []
    for line in (here / f"{day}_input.txt").read_text().splitlines():
        d, n = line.split()
        motions.append((DIRECTIONS[d], int(n)))
    return motions


def simulate(motions, n_knots=2):
    knots = [[0, 0] for _ in range(n_knots)]
    visited = {(0, 0)}
    for (dir_x, dir_y), n in motions:
        for _ in range(n):
            knots[0][0] += dir_x
            knots[0][1] += dir_y
            for i in range(1, n_knots):
                dx = knots[i - 1][0] - knots[i][0]
                dy = knots[i - 1][1] - knots[i][1]
                if abs(dx) > 1 or abs(dx) + abs(dy) > 2:
                    knots[i][0] += 1 if dx > 0 else -1
                if abs(dy) > 1 or abs(dx) + abs(dy) > 2:
                    knots[i][1] += 1 if dy > 0 else -1
            visited.add(tuple(knots[-1]))
    return visited


def part1():
    motions = read_input()
    return len(simulate(motions))


def part2():
    motions = read_input()
    return len(simulate(motions, n_knots=10))
