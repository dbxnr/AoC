import re


with open("input.txt") as f:
    data = f.readlines()


def part_one(data):
    valid_passwords = 0

    for line in data:
        line = line.split(":")
        letter = line[0][-1]
        pword = line[1].strip()
        numbers = re.findall("[0-9]+", line[0])
        nmin = int(numbers[0])
        nmax = int(numbers[1])
        count = pword.count(letter)

        if (count <= nmax) and (count >= nmin):
            valid_passwords += 1

    return valid_passwords
