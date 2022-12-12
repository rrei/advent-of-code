import pathlib


def read_input():
    here = pathlib.Path(__file__).parent
    *_, day = __name__.rsplit(".", 1)
    elves = [[]]
    for line in (here / f"{day}_input.txt").read_text().splitlines():
        if not line.strip():
            elves.append([])
        else:
            elves[-1].append(int(line))
    return elves


def part1():
    return sum(max(read_input(), key=sum))


def part2():
    total_calories = sorted(sum(items) for items in read_input())
    return sum(total_calories[-3:])
