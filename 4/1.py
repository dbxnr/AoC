import re

data = r"""ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

with open("input.txt") as f:
    data = f.read()
#    # data = [line.strip() for line in data]

fields = {
    "byr": True,
    "iyr": True,
    "eyr": True,
    "hgt": True,
    "hcl": True,
    "ecl": True,
    "pid": True,
}


def parse_data(data):
    # Adapted from stackoverflow.com/questions/38852712
    regex = r"(?:\n){2,}"
    passports = []
    for line in re.split(regex, data.strip()):
        line = line.replace("\n", " ")
        passports.append(line)

    print(passports)
    return passports


def validate_passports(passports):
    valid_passports = len(passports)
    for p in passports:
        for k in fields.keys():
            if k not in p:
                valid_passports -= 1
                break
    return valid_passports


passports = parse_data(data)
valid = validate_passports(passports)
print(valid)
