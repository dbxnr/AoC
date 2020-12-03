import itertools


with open('input.txt') as f:
    data = f.readlines()
    data = [line.strip() for line in data]

num_cols = len(data[0])
num_lines = len(data)-1
ground = '.'
tree = '#'
cycle = itertools.cycle(range(num_cols))
right = 3
down = 1


def find_tree():
    row = -1
    col = 0
    count = 0

    while (col < num_cols) and (row < num_lines):
        n = next(cycle)
        for _ in range(right-1):
            next(cycle)
        col = n
        row += down
        print(f"pos({row}, {col})")
        count += data[row][col] == tree

    return count


print(find_tree())
