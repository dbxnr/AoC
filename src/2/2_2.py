import re


with open("input.txt") as f:
    data = f.readlines()


def part_two(data):
    valid_passwords = 0
    passwords = 0

    for line in data:
        passwords += 1
        line = line.split(":")
        letter = line[0][-1]
        pword = line[1].strip()
        numbers = re.findall("[0-9]+", line[0])
        nmin = int(numbers[0]) - 1
        nmax = int(numbers[1]) - 1

        if len(pword) > nmax:
            if (pword[nmax] is letter) ^ (pword[nmin] is letter):
                valid_passwords += 1

    return valid_passwords
