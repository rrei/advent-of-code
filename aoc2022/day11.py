import dataclasses
import math
import pathlib
import re

monkey_regex = re.compile(
    r"""Monkey (?P<id>.+):
  Starting items:( (?P<items>.+))?
  Operation: new = (?P<operation>.+)
  Test: divisible by (?P<test>.+)
    If true: throw to monkey (?P<test_pass>.+)
    If false: throw to monkey (?P<test_fail>.+)
""",
    flags=re.MULTILINE,
)


def read_input():
    here = pathlib.Path(__file__).parent
    *_, day = __name__.rsplit(".", 1)
    return {
        match["id"]: Monkey(
            id=match["id"],
            items=[int(n) for n in match["items"].split(",")],
            operation=match["operation"],
            test=int(match["test"]),
            test_pass=match["test_pass"],
            test_fail=match["test_fail"],
        )
        for match in monkey_regex.finditer((here / f"{day}_input.txt").read_text())
    }


@dataclasses.dataclass
class Monkey:
    id: str
    items: [int]
    operation: str
    test: int
    test_pass: str
    test_fail: str
    inspections: int = 0

    def turn(self, monkeys, relief=3, test_prod=None):
        for item in self.items:
            item = eval(self.operation.replace("old", str(item)))
            if relief:
                item //= relief
            if test_prod:
                item %= test_prod
            target = self.test_pass if item % self.test == 0 else self.test_fail
            monkeys[target].items.append(item)
        self.inspections += len(self.items)
        self.items = []


def part1():
    monkeys = read_input()
    for _ in range(20):
        for monkey in monkeys.values():
            monkey.turn(monkeys)
    x, y = sorted(m.inspections for m in monkeys.values())[-2:]
    return x * y


def part2():
    monkeys = read_input()
    test_prod = math.prod(m.test for m in monkeys.values())
    for _ in range(10_000):
        for monkey in monkeys.values():
            monkey.turn(monkeys, relief=0, test_prod=test_prod)
    x, y = sorted(m.inspections for m in monkeys.values())[-2:]
    return x * y
