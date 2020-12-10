#!/usr/bin/env python3

min_cont=2
def get(target):
    with open('input.txt') as file:
        message = [int(n) for n in file.readlines()]
        for i in range(0, len(message)-min_cont):
            for j in range(i+1, len(message)):
                if sum(message[i:j]) > target:
                    break
                if sum(message[i:j]) == target:
                    return max(message[i:j]) + min(message[i:j])


print("Answer:", get(26796446))