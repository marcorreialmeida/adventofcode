#!/usr/bin/env python3
import math

slopes = [
    {"x": 1, "y": 1},
    {"x": 3, "y": 1},
    {"x": 5, "y": 1},
    {"x": 7, "y": 1},
    {"x": 1, "y": 2}
]

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    height = len(lines)
    width = len(lines[0])

def countTrees(slope):
    trees = 0
    x, y = 1, 1
    while y < height:
        y = y + slope["y"]
        x = (x + slope["x"]) % width
        trees += 1 if lines[y-1][x-1] == "#" else 0
    return trees

print(math.prod(map(countTrees, slopes)))