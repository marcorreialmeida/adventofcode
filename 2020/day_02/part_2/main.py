#!/usr/bin/env python3
import re


with open('input.txt') as f:
    lines = [x.strip() for x in f.readlines()]
    rowRegex = r'^(\d+)\-(\d+) ([a-z])\: ([a-z]+)$'
    passwords = [
        {
            "first": int(re.search(rowRegex, line).group(1)),
            "second":int(re.search(rowRegex, line).group(2)),
            "letter": re.search(rowRegex, line).group(3),
            "password": re.search(rowRegex, line).group(4)
        } for line in lines
    ]
    valid = [p for p in passwords if (p["password"][p["first"]-1] == p["letter"]) ^ (p["password"][p["second"]-1] == p["letter"])]

print(len(valid))