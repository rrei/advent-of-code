import pathlib


def read_input():
    here = pathlib.Path(__file__).parent
    *_, day = __name__.rsplit(".", 1)
    assignments = []
    for line in (here / f"{day}_input.txt").read_text().splitlines():
        a, b = line.split(",")
        a0, a1 = map(int, a.split("-"))
        b0, b1 = map(int, b.split("-"))
        assignments.append(((a0, a1), (b0, b1)))
    return assignments


def part1():
    return sum(
        (a0 <= b0 and b1 <= a1) or (b0 <= a0 and a1 <= b1)
        for (a0, a1), (b0, b1) in read_input()
    )


def part2():
    return sum(not (a1 < b0 or b1 < a0) for (a0, a1), (b0, b1) in read_input())
