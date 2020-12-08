#!/usr/bin/env python3
import re
from functools import reduce
import pprint

clean_re = r'( bags| bag|\.|no other)'

def pretty(col):
    pprint.PrettyPrinter().pprint(col)


with open('input.txt') as file:
    data_cleaned = re.sub(clean_re, '', file.read())
    rules = {
        line.split(' contain ')[0]: line.split(' contain ')[1].split(', ')
        for line in data_cleaned.split('\n') if line.split(' contain ')[1]
    }
    bags = {
        C: [c[2:] for c in cl for i in range(0, int(c[0]))]
        for C, cl in rules.items()
    }
    pretty(bags)


def totals_bags(bag):
    return 1 + sum([totals_bags(inner_bag) for inner_bag in bags.get(bag, [])])


print("Answer:", totals_bags("shiny gold") - 1)
