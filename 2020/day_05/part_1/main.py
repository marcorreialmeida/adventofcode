#!/usr/bin/env python3
import re


def get_seat(boarding_pass):
    row = navigate_range(boarding_pass, 0, 6, 'F', list(range(0, 128)))
    col = navigate_range(boarding_pass, 7, 9, 'L', list(range(0, 8)))
    return row, col


def navigate_range(boarding_pass, code_start_pos, code_end_pos, to_zero_move, available_range):
    for region in boarding_pass[code_start_pos:code_end_pos+1]:
        available_range = available_range[:len(available_range)//2] if region == to_zero_move else available_range[len(available_range)//2:]
    return available_range[0]


with open('input.txt') as file:
    boarding_passes = [line.strip() for line in file.readlines()]
    seats = [get_seat(bp) for bp in boarding_passes]
    seat_ids = [row * 8 + col for (row, col) in seats]

print("Answer:", max(seat_ids))