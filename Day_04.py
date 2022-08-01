"""
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
"""
import unittest


def load_data(filename):
    with open(filename, 'r') as f:
        return f.read().split('\n\n')


def is_valid(passport):
    if passport.find('byr') == -1:
        return False
    if passport.find('iyr') == -1:
        return False
    if passport.find('eyr') == -1:
        return False
    if passport.find('hgt') == -1:
        return False
    if passport.find('hcl') == -1:
        return False
    if passport.find('ecl') == -1:
        return False
    if passport.find('pid') == -1:
        return False
    # if passport.find('cid') == -1:
    #     return False
    return True


def part1():
    data = load_data('Day_04.txt')
    tally = 0
    for item in data:
        print(f'Valid: {is_valid(item)}')
        print(item)
        print()
        if is_valid(item):
            tally += 1
    print(f'Total valid: {tally}')


def parse_value(field_name, passport):
    fields = passport.split()
    for field in fields:
        if field.find(field_name) == 0:
            return field[4:]
    return None


"""
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""


def hex_digit_only(hex):
    for c in hex:
        if c < '0' or ('9' < c < 'a') or c > 'z':
            return False
    return True


def is_valid_value(field_name, value):
    match field_name:
        case 'byr':
            if len(value) != 4:
                return False
            y = int(value)
            if y < 1920 or y > 2002:
                return False
            return True
        case 'iyr':
            if len(value) != 4:
                return False
            y = int(value)
            if y < 2010 or y > 2020:
                return False
            return True
        case 'eyr':
            if len(value) != 4:
                return False
            y = int(value)
            if y < 2020 or y > 2030:
                return False
            return True
        case 'hgt':
            if value.find('cm') != -1:
                n = int(value[:-2])
                if n < 150 or n > 193:
                    return False
            elif value.find('in'):
                n = int(value[:-2])
                if n < 59 or n > 76:
                    return False
            else:
                raise ValueError(f'{value} invalid. Expected "in" or "cm" suffix')
            return True
        case 'hcl':
            if len(value) != 7:
                return False
            if value[0:1] != '#':
                return False
            if not hex_digit_only(value[1:]):
                return False
            return True
        case 'ecl':
            if value not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
                return False
            return True
        case 'pid':
            if len(value) != 9:
                return False
            if not value.isnumeric():
                return False
            return True


def all_fields_valid(passport):
    print()
    for field_name in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
        value = parse_value(field_name, passport)
        print(f'{field_name}:{value} ', end='')
        if not is_valid_value(field_name, value):
            print(f'Invalid')
            return False
        print('Valid')
    return True


def tally_valid_passports(filename):
    data = load_data(filename)
    valid_passport_tally = 0
    for passport in data:
        # First a simple check: we assert all fields are present
        if not is_valid(passport):
            continue
        # Field validation
        if not all_fields_valid(passport):
            continue
        valid_passport_tally += 1
    print(f'Total valid passports: {valid_passport_tally}')
    return valid_passport_tally

print(tally_valid_passports('Day_04.py'))

class TestFieldValidation(unittest.TestCase):
    def test_field_validation(self):
        total_valid = tally_valid_passports('Day_04_valid.txt')
        self.assertEqual(4, total_valid)
        total_valid = tally_valid_passports('Day_04_invalid.txt')
        self.assertEqual(0, total_valid)


