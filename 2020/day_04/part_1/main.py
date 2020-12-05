#!/usr/bin/env python3
import re


with open('input.txt') as f:
    lines = [line.replace('\n', ' ').strip() for line in f.read().split('\n\n')]
    passports = [dict(field.split(':') for field in line.split(' ')) for line in lines]
    for p in passports:
        if "cid" in p:
            del p["cid"]
    valids = [p for p in passports if len(p) == 7]

print(len(valids))