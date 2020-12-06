#!/usr/bin/env python3


with open('input.txt') as file:
    group_answers = [[set(p) for p in line.split('\n')] for line in file.read().split('\n\n')]
    uniques = sum([len(set.intersection(*g)) for g in group_answers])

print("Answer:", uniques)