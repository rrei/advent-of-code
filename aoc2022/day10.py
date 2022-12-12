import pathlib


def read_input():
    here = pathlib.Path(__file__).parent
    *_, day = __name__.rsplit(".", 1)
    return [
        None if line == "noop" else int(line[len("addx") :])
        for line in (here / f"{day}_input.txt").read_text().splitlines()
    ]


def run(program):
    x = 1
    clock = 0
    for instruction in program:
        if instruction is None:
            clock += 1
            yield clock, x
        else:
            clock += 1
            yield clock, x
            clock += 1
            yield clock, x
            x += instruction


def part1():
    program = read_input()
    return sum(
        clock * x
        for clock, x in run(program)
        if clock <= 220 and (clock - 20) % 40 == 0
    )


def part2():
    program = read_input()
    screen = [[None for _ in range(40)] for _ in range(6)]
    for clock, x in run(program):
        row, col = divmod(clock - 1, 40)
        screen[row][col] = "#" if abs(col - x) <= 1 else "."
        if clock >= 240:
            break
    return "\n".join("".join(r) for r in screen)
