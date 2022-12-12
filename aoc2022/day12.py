import collections
import itertools
import math
import pathlib


def read_input():
    here = pathlib.Path(__file__).parent
    *_, day = __name__.rsplit(".", 1)
    grid = (here / f"{day}_input.txt").read_text().splitlines()
    rows, cols = len(grid), len(grid[0])
    graph = collections.defaultdict(set)
    start = end = None
    for x0, y0 in itertools.product(range(cols), range(rows)):
        c0 = grid[y0][x0]
        if c0 == "S":
            start = (x0, y0)
        elif c0 == "E":
            end = (x0, y0)
        h0 = height(c0)
        graph[x0, y0].update(
            (x1, y1)
            for x1, y1 in neighbors(x0, y0, rows, cols)
            if height(grid[y1][x1]) - h0 <= 1
        )
    return grid, graph, start, end


def height(char):
    if char == "S":
        char = "a"
    elif char == "E":
        char = "z"
    return ord(char) - ord("a")


def neighbors(x0, y0, rows, cols):
    return (
        (x1, y1)
        for x1, y1 in ((x0 - 1, y0), (x0 + 1, y0), (x0, y0 - 1), (x0, y0 + 1))
        if 0 <= x1 < cols and 0 <= y1 < rows
    )


def dijkstra(graph, start, end=None):
    distance = {n: math.inf for n in graph.keys()}
    distance[start] = 0
    predecessor = {}
    queue = set(graph.keys())
    while len(queue) > 0:
        n0 = min(queue, key=lambda n: distance[n])
        if n0 == end:
            break
        d = distance[n0] + 1
        for n1 in graph[n0]:
            if d < distance[n1]:
                distance[n1] = d
                predecessor[n1] = n0
        queue.remove(n0)
    return distance, predecessor


def shortest_path(graph, start, end):
    distance, predecessor = dijkstra(graph, start, end)
    if end not in predecessor:
        return None
    path = collections.deque([end])
    while path[0] != start:
        path.appendleft(predecessor[path[0]])
    return path


def part1():
    _, graph, start, end = read_input()
    return len(shortest_path(graph, start, end)) - 1


def part2():
    grid, graph, _, end = read_input()
    # NOTE: create a graph with reverse connectivity and run dijkstra to find the
    # shortest distance from `end` to all points in the the reverse graph.
    rgraph = {n: set() for n in graph.keys()}
    for source, targets in graph.items():
        for target in targets:
            rgraph[target].add(source)
    distance, predecessor = dijkstra(rgraph, start=end, end=None)
    return min(
        distance[x, y]
        for y, row in enumerate(grid)
        for x, char in enumerate(row)
        if height(char) == 0
    )
