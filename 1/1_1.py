with open("input.txt") as f:
    data = f.read().splitlines()

s = 0
while s <= len(data):
    for n in data[s:]:
        if int(n) + int(data[s]) == 2020:
            print(f"Value is {int(n) * int(data[s])}")
    s += 1
