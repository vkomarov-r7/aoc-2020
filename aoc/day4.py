import re
from aoc.input import open_input


REQUIRED_FIELDS = {
    'byr', 'iyr', 'eyr', 'hgt',
    'hcl', 'ecl', 'pid',  # (optional) 'cid',
}


def read_passports():
    passport = {}
    for line in open_input('4.txt'):
        line = line.strip()
        if not line:
            yield passport
            passport = {}
            continue

        pairs = line.split(' ')
        for pair in pairs:
            k, v = pair.split(':')
            passport[k] = v
    yield passport


def part_1_is_passport_valid(passport):
    missing_fields = REQUIRED_FIELDS - passport.keys()
    return not missing_fields


def part_1():
    n_valid = 0

    for passport in read_passports():
        if part_1_is_passport_valid(passport):
            n_valid += 1

    print("Number of valid passports:", n_valid)


def part_2_is_passport_valid(passport):
    eye_colors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
    validators = {
        'byr': lambda byr: len(byr) == 4 and 1920 <= int(byr) <= 2002,
        'iyr': lambda iyr: len(iyr) == 4 and 2010 <= int(iyr) <= 2020,
        'eyr': lambda eyr: len(eyr) == 4 and 2020 <= int(eyr) <= 2030,
        'hgt': validate_hgt,
        'hcl': lambda hcl: bool(re.match(r'#[0-9a-f]{6}', hcl)),
        'ecl': lambda ecl: ecl in eye_colors,
        'pid': lambda pid: bool(re.match(r'^\d{9}$', pid)),
        'cid': lambda cid: True,
    }
    missing_fields = REQUIRED_FIELDS - passport.keys()
    if missing_fields:
        return False

    # print("Processing passport:", passport)
    for field, value in passport.items():
        validator = validators[field]
        try:
            result = validator(value)
        except Exception:
            result = False
        if result is False:
            return False
    return True


def validate_hgt(hgt):
    match = re.match(r'(\d+)(cm|in)', hgt)
    if not match:
        return False

    n, units = match.groups()
    n = int(n)
    if units == 'cm':
        return 150 <= n <= 193
    elif units == 'in':
        return 59 <= n <= 76
    else:
        raise ValueError


def part_2():
    n_valid = 0

    for passport in read_passports():
        if part_2_is_passport_valid(passport):
            n_valid += 1

    print("Number of valid passports:", n_valid)


part_1()
part_2()
