#!/usr/bin/env python3

with open('input.txt') as file:
    jolts = [int(n) for n in file.readlines()]
    jolts.append(0)
    jolts.sort()
    jolts.append(max(jolts)+3)
    diffs = [jolts[i + 1] - a for i, a in enumerate(jolts) if i < len(jolts) - 1]

print("Answer:", len([1 for i in diffs if i==1]) * len([1 for i in diffs if i==3]))
