import collections
import pathlib


def read_input():
    here = pathlib.Path(__file__).parent
    *_, day = __name__.rsplit(".", 1)
    return (here / f"{day}_input.txt").read_text()


def find_unique_subsequence(sequence, size):
    chars = collections.deque(maxlen=size)
    for i, char in enumerate(sequence):
        chars.append(char)
        if len(set(chars)) == size:
            return i + 1
    raise RuntimeError("oh my...")


def part1():
    return find_unique_subsequence(read_input(), 4)


def part2():
    return find_unique_subsequence(read_input(), 14)
