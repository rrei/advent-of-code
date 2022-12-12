import pathlib

TOTAL_SIZE = object()  # just a "special" key to track the total size of directories


def read_input():
    here = pathlib.Path(__file__).parent
    *_, day = __name__.rsplit(".", 1)
    root = {TOTAL_SIZE: 0}
    stack = []
    for line in (here / f"{day}_input.txt").read_text().splitlines():
        if line.startswith("$ cd "):
            target = line[len("$ cd ") :]
            if target == "/":
                stack = [root]
            elif target == "..":
                stack.pop()
            else:
                stack.append(stack[-1][target])
        elif line.startswith("$ ls"):
            continue
        elif line.startswith("dir "):
            dirname = line[len("dir ") :]
            stack[-1].setdefault(dirname, {TOTAL_SIZE: 0})
        else:
            filesize, filename = line.split(maxsplit=1)
            if filename not in stack[-1]:
                filesize = int(filesize)
                stack[-1][filename] = filesize
                for dir in stack:
                    dir[TOTAL_SIZE] += filesize
    return root


def iterdirs(root):
    stack = [root]
    while len(stack) > 0:
        dir = stack.pop()
        yield dir
        stack.extend(child for child in dir.values() if isinstance(child, dict))


def part1():
    return sum(
        dir_size
        for dir in iterdirs(read_input())
        if (dir_size := dir[TOTAL_SIZE]) <= 100000
    )


def part2():
    root = read_input()
    total_space = 70000000
    unused_space = total_space - root[TOTAL_SIZE]
    required_space = 30000000 - unused_space
    return min(
        dir_size
        for dir in iterdirs(read_input())
        if (dir_size := dir[TOTAL_SIZE]) >= required_space
    )
