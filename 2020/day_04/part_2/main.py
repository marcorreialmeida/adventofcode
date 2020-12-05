#!/usr/bin/env python3
import re

rules = {
    "byr": lambda field: re.match(r'^(\d{4})$', field) and 1920 <= int(re.match(r'^(\d{4})$', field).group(1)) <= 2002,
    "iyr": lambda field: re.match(r'^(\d{4})$', field) and 2010 <= int(re.match(r'^(\d{4})$', field).group(1)) <= 2020,
    "eyr": lambda field: re.match(r'^(\d{4})$', field) and 2020 <= int(re.match(r'^(\d{4})$', field).group(1)) <= 2030,
    "hgt": lambda field: (re.match(r'^(\d+)cm$', field) and 150 <= int(re.match(r'^(\d+)cm$', field).group(1)) <= 193) or (re.match(r'^(\d+)in$', field) and 59 <= int(re.match(r'^(\d+)in$', field).group(1)) <= 76),
    "hcl": lambda field: re.match(r'^#([0-9a-f]{6})$', field),
    "ecl": lambda field: field in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda field: re.match(r'^([0-9]{9})$', field),
}


def is_valid(passport):
    return all([rules[f](v) for f,v in passport.items()])


with open('input.txt') as file:
    lines = [line.replace('\n', ' ').strip() for line in file.read().split('\n\n')]
    passports = [dict(field.split(':') for field in line.split(' ')) for line in lines]
    for p in passports:
        if "cid" in p:
            del p["cid"]
    completes = [p for p in passports if len(p) == 7]
    valids = [p for p in completes if is_valid(p)]

print(len(valids))