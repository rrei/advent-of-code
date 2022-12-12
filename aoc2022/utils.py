import itertools
import math


def first(iterable, condition):
    for elem in iterable:
        if condition(elem):
            return elem
    raise ValueError(f"unable to find element for condition {condition}")


def lcm(*nums):
    x0, x1, *rest = nums
    lcm = x0 * x1 // gcd(x0, x1)
    for x in rest:
        lcm = lcm * x // gcd(lcm, x)
    return lcm


def gcd(*nums):
    x0, x1, *rest = nums
    gcd = math.gcd(x0, x1)
    for x in rest:
        gcd = math.gcd(gcd, x)
    return gcd


def factorize(n):
    for f in itertools.chain([2], itertools.count(start=3, step=2)):
        while n > 1 and n % f == 0:
            n //= f
            yield f
        if n == 1:
            return


def sign(x):
    return 0 if x == 0 else +1 if x > 0 else -1
