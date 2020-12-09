#!/usr/bin/env python3

cmds = {
    'nop': lambda p, switch: (1, 0) if not switch else (int(p), 0),
    'jmp': lambda p, switch: (int(p), 0) if not switch else (1, 0),
    'acc': lambda p, switch: (1, int(p))
}

with open('input.txt') as file:
    program = file.readlines()

    for candidate in range(0, len(program)):
        effects = [(cmds[l.strip().split(' ')[0]](l.strip().split(' ')[1], i==candidate)) for i,l in enumerate(program)]
        visited = []
        acc, ip = 0, 0
        while ip not in visited and (0 <= ip < len(program)):
            visited.append(ip)
            acc += effects[ip][1]
            ip += effects[ip][0]
        if ip == len(program):
            print("Answer:", acc)
            break
