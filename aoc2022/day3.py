import pathlib
import string

PRIORITY = {c: p for p, c in enumerate(string.ascii_letters, start=1)}


def read_input():
    here = pathlib.Path(__file__).parent
    *_, day = __name__.rsplit(".", 1)
    file = here / f"{day}_input.txt"
    return file.read_text().splitlines()


def shared_item(rucksack):
    compartment_a = rucksack[: len(rucksack) // 2]
    compartment_b = rucksack[len(rucksack) // 2 :]
    return next(iter(set(compartment_a).intersection(compartment_b)))


def group_badge(group):
    shared = set(string.ascii_letters)
    for rucksack in group:
        shared.intersection_update(rucksack)
    return next(iter(shared))


def part1():
    return sum(PRIORITY[shared_item(rucksack)] for rucksack in read_input())


def part2():
    rucksacks = read_input()
    return sum(
        PRIORITY[group_badge(rucksacks[i : i + 3])] for i in range(0, len(rucksacks), 3)
    )
