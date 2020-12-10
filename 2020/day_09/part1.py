#!/usr/bin/env python3

p=25
i=p
with open('input.txt') as file:
    message = [int(n) for n in file.readlines()]
    while {-(n - message[i]) for n in message[i-p:i]} & set(message[i-p:i]):
        i+=1

print("Answer:", message[i])
