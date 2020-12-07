from itertools import permutations
import math

with open("input.txt") as f:
    data = list(map(int, f.readlines()))


def permute():
    p = list(permutations(data, 3))
    for i in p:
        if sum(list(i)) == 2020:
            return math.prod(list(i))
