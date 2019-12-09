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
        locs += directionFunctions[pathItem[0]](locs[-1], int(pathItem[1:]))
    return set(locs)

def pathsToIntersections(path, intersections):
    stepsToIntersections = {}
    for p in range(1, len(path)):
        locsInPartialPath = locations(path[0:p]) - {central}
        for inters in intersections:
            if inters in locsInPartialPath:
                if inters not in stepsToIntersections:
                    stepsToIntersections.update({inters: len(locsInPartialPath)})
    return stepsToIntersections

locations1 = locations(path1)
locations2 = locations(path2)
intersections = (locations1 & locations2) - {central}

path1StepsToInsters = pathsToIntersections(path1, intersections)
path2StepsToInsters = pathsToIntersections(path2, intersections)
print("I guess:", min(map(lambda x: path1StepsToInsters[x] + path2StepsToInsters[x], intersections)))
# wrong (too high): 301038, 92220, 92218

What I'm doing wrong:
 - locsInPartialPath eventually includes "inters" but that iteration includes more locations than it needed to reach it