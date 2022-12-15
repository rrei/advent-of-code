import itertools
import math
import pathlib


def read_input():
    here = pathlib.Path(__file__).parent
    *_, day = __name__.rsplit(".", 1)
    walls = set()
    for line in (here / f"{day}_input.txt").read_text().splitlines():
        points = [tuple(int(x) for x in p.split(",")) for p in line.split(" -> ")]
        for (x0, y0), (x1, y1) in itertools.pairwise(points):
            assert x0 == x1 or y0 == y1
            xmin, xmax = sorted((x0, x1))
            ymin, ymax = sorted((y0, y1))
            walls.update((x0, y) for y in range(ymin, ymax + 1))
            walls.update((x, y0) for x in range(xmin, xmax + 1))
    return walls


def drop_sand(obstacles, source=(500, 0), bottom=math.inf):
    """Simulate dropping a unit of sand from `source` and return its resting position
    or `None` if it will keep falling into the cold void.
    """
    void = max(y for _, y in obstacles) if math.isinf(bottom) else math.inf
    x, y = source
    while y < bottom - 1 and y < void:
        next_pos = next(
            (
                p
                for p in ((x, y + 1), (x - 1, y + 1), (x + 1, y + 1))
                if p not in obstacles
            ),
            None,
        )
        if next_pos is None:
            break
        x, y = next_pos
    return None if y == void else (x, y)


def part1():
    walls = read_input()
    obstacles = set(walls)
    while (p := drop_sand(obstacles)) is not None:
        obstacles.add(p)
    return len(obstacles) - len(walls)


def part2():
    walls = read_input()
    obstacles = set(walls)
    bottom = max(y for _, y in walls) + 2
    while (p := drop_sand(obstacles, bottom=bottom)) != (500, 0):
        obstacles.add(p)
    return len(obstacles) - len(walls) + 1
