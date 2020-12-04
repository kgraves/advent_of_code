import re
import sys


HEX_RE = re.compile('^#[0-9a-f]{6}$')
REQ_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def int_in_range(value, min_, max_):
    if not value.isnumeric():
        return False

    return min_ <= int(value) <= max_


def valid_height(value):
    units = value[-2:]
    if units not in ['cm', 'in']:
        return False

    min_, max_ = (150, 193) if units == 'cm' else (59, 76)

    return int_in_range(value[:-2], min_, max_)

def valid_hex(value):
    return HEX_RE.match(value) is not None


def valid_eye_color(value):
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def valid_passport_id(value):
    return len(value) == 9 and value.isnumeric()


def is_valid_passport(p):
    keys = p.keys()

    return all([
        all(k in keys for k in REQ_FIELDS),
        int_in_range(p.get('byr', ''), 1920, 2002),
        int_in_range(p.get('iyr', ''), 2010, 2020),
        int_in_range(p.get('eyr', ''), 2020, 2030),
        valid_height(p.get('hgt', '')),
        valid_hex(p.get('hcl', '')),
        valid_eye_color(p.get('ecl', '')),
        valid_passport_id(p.get('pid', '')),
    ])


def make_passport(data):
    passport = {}
    for kv_pair in data.split(' '):
        k, v = kv_pair.split(':')
        passport[k] = v

    return passport


def part_one(passports):
    count = 0
    for p in passports:
        if all([rf in p for rf in REQ_FIELDS]):
            count += 1

    print(count)


def part_two(passports):
    count = 0
    for p in passports:
        if is_valid_passport(p):
            count += 1

    print(count)


def main():
    passports = []
    buffer = []

    with open('2020/4/input.txt', 'r') as f:
        for line in f:
            if not line.strip():
                data = ' '.join(buffer)
                passports.append(make_passport(data))
                buffer = []
            else:
                buffer.append(line.strip())

        if buffer:
            data = ' '.join(buffer)
            passports.append(make_passport(data))
            buffer = []

    part_one(passports)
    part_two(passports)


if __name__ == '__main__':
    main()
