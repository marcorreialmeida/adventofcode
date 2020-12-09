#!/usr/bin/env python3

acc = 0
visited = []
cmds = {
    'nop': lambda p: (1, 0),
    'jmp': lambda p: (int(p), 0),
    'acc': lambda p: (1, int(p))
}

with open('input.txt') as file:
    effects = [(cmds[i.strip().split(' ')[0]](i.strip().split(' ')[1])) for i in file.readlines()]
    ip = 0
    while ip not in visited:
        visited.append(ip)
        acc += effects[ip][1]
        ip += effects[ip][0]

print("Answer:", acc)
