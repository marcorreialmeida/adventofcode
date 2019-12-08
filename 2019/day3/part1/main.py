#!/usr/bin/env python3
import re

path1 = open('path1.txt').readline().strip().split(",")
path2 = open('path2.txt').readline().strip().split(",")

pathRegex = r'^(U|D|L|R)(\d+)$'
central = (0,0)
directionFunctions = {
    "R": lambda loc, length: [(loc[0]+i, loc[1]) for i in range(1, length+1)],
    "L": lambda loc, length: [(loc[0]-i, loc[1]) for i in range(1, length+1)],
    "U": lambda loc, length: [(loc[0], loc[1]+i) for i in range(1, length+1)],
    "D": lambda loc, length: [(loc[0], loc[1]-i) for i in range(1, length+1)],
}

def distance_from_closest(path1, path2):
    locations1 = locations(path1)
    locations2 = locations(path2)
    intersections = (locations1 & locations2) - {central}
    return min(map(lambda loc: abs(loc[0])+abs(loc[1]), intersections))

def locations(path):
    locs = [central]
    for pathItem in path:
        locs += draw_line(locs[-1], pathItem)
    return set(locs)

def draw_line(loc, pathItem):
    direction = re.search(pathRegex, pathItem).group(1)
    length = int(re.search(pathRegex, pathItem).group(2))
    return directionFunctions[direction](loc, length)

print(distance_from_closest(path1, path2))

#print("Distance from central point:", distance_from_closest(path1, path2))
