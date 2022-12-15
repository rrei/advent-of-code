import pathlib


def read_input():
    here = pathlib.Path(__file__).parent
    *_, day = __name__.rsplit(".", 1)
    lines = (here / f"{day}_input.txt").read_text().splitlines()
    return [(eval(lines[i]), eval(lines[i + 1])) for i in range(0, len(lines), 3)]


def get_order(left, right):
    if isinstance(left, int):
        if isinstance(right, int):
            return +1 if left < right else 0 if left == right else -1
        left = [left]
    elif isinstance(right, int):
        right = [right]
    for l, r in zip(left, right):
        order = get_order(l, r)
        if order != 0:
            return order
    return get_order(len(left), len(right))


def quicksort(packets, lo=0, hi=None):
    if hi is None:
        hi = len(packets)
    if hi - lo < 2:
        return packets[lo:hi]
    smaller = []
    greater = []
    equal = [packets[lo]]
    for i in range(lo + 1, hi):
        order = get_order(packets[i], packets[lo])
        (smaller if order > 0 else greater if order < 0 else equal).append(packets[i])
    return quicksort(smaller) + equal + quicksort(greater)


def part1():
    return sum(
        i
        for i, (left, right) in enumerate(read_input(), start=1)
        if get_order(left, right) > 0
    )


def part2():
    packets = []
    for pair in read_input():
        packets.extend(pair)
    packets.append([[2]])
    packets.append([[6]])
    packets = quicksort(packets)
    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)
