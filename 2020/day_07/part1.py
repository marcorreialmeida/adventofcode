#!/usr/bin/env python3
import re
from functools import reduce
import pprint

clean_re = r'( bags| bag| \d+|\.|no other)'

def pretty(col):
    pprint.PrettyPrinter().pprint(col)


with open('input.txt') as file:
    data_cleaned = re.sub(clean_re, '', file.read())
    rules = {
        line.split(' contain ')[0] : line.split(' contain ')[1].split(', ')
        for line in data_cleaned.split('\n')
    }
    contained_in_rule = [{c:C for c in cl} for C, cl in rules.items()]
    fittings = dict()
    for rule in contained_in_rule:
        for c,C in rule.items():
            if c:
                fittings[c].add(C) if c in fittings else fittings.update({c:{C}})
    pretty(fittings)

def fits(bag):
    if bag not in fittings:
        return set()
    return set.union(fittings[bag], *[fits(b) for b in fittings[bag]])

print("Answer:", len(fits('shiny gold')))