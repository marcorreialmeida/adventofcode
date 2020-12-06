#!/usr/bin/env python3


with open('input.txt') as file:
    distinct_answers = [len(set(line.replace('\n', ''))) for line in file.read().split('\n\n')]


print("Answer:", sum(distinct_answers))