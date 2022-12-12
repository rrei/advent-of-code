import collections
import pathlib
import re

item_regex = re.compile(r"\[(?P<id>\w)]")
move_regex = re.compile(r"move (\d+) from (\d+) to (\d+)")


def read_input():
    here = pathlib.Path(__file__).parent
    *_, day = __name__.rsplit(".", 1)
    lines = iter((here / f"{day}_input.txt").read_text().splitlines())
    items = collections.defaultdict(list)
    stacks = None
    for y, line in enumerate(lines):
        n_matches = 0
        for match in item_regex.finditer(line):
            items[match.start("id")].append(match["id"])
            n_matches += 1
        if n_matches == 0:
            stack_ids = [int(s) for s in line.split()]
            stacks = {
                stack_id: list(reversed(stack_items))
                for stack_id, (_, stack_items) in zip(stack_ids, sorted(items.items()))
            }
            break
    next(lines)  # skip separator line
    moves = [[int(x) for x in move_regex.match(line).groups()] for line in lines]
    return stacks, moves


def part1():
    stacks, moves = read_input()
    for n, src, tgt in moves:
        for _ in range(n):
            stacks[tgt].append(stacks[src].pop())
    return "".join(stack[-1] for _, stack in sorted(stacks.items()))


def part2():
    stacks, moves = read_input()
    for n, src, tgt in moves:
        stacks[tgt].extend(stacks[src][-n:])
        del stacks[src][-n:]
    return "".join(stack[-1] for _, stack in sorted(stacks.items()))
