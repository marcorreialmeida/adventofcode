#!/usr/bin/env python3
import re

with open('input.txt') as f:
    expense_report = [int(x.strip()) for x in f.readlines()]

def sumFactor(expenses, target):
    for iterator_a in range(0, len(expenses)-1):
        for iterator_b in range(iterator_a+1, len(expenses)-1):
            print(expenses[iterator_a], expenses[iterator_b], expenses[iterator_a] + expenses[iterator_b])
            if expenses[iterator_a] + expenses[iterator_b] == target:
                return expenses[iterator_a] * expenses[iterator_b];

print(sumFactor(expense_report, 2020))