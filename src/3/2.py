import itertools
import math

data = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""".splitlines()


r = 3492520200
# with open('input3.txt') as f:
#    data = f.readlines()
#    data = [line.strip() for line in data]

num_cols = len(data[0])
num_lines = len(data)-1
ground = '.'
tree = '#'
cycle = itertools.cycle(range(num_cols))
routes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]


def find_tree():
    totals = []

    for route in routes:
        row = -1
        col = 0
        count = 0
        while (col < num_cols) and (row < num_lines):
            n = next(cycle)
            for _ in range(route[0]-1):
                next(cycle)
            col = n
            if ((row + route[1]) > num_lines):
                print(row, num_lines)
                break
            else:
                row += route[1]
                count += data[row][col] == tree

        totals.append(count)
        print(totals)

    # assert(math.prod(totals) == r)
    return math.prod(totals)


print(find_tree())
