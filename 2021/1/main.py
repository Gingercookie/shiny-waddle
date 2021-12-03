#!/usr/bin/python3

def part1(depths):
    inc = 0
    for i in range(len(depths)):
        if (depths[i] > depths[i-1]):
            inc += 1
    return inc

def part2(depths):
    inc = 0

    for i in range(len(depths)-1):
        cur_win = depths[i-1] + depths[i] + depths[i+1]
        prev_win = depths[i-2] + depths[i-1] + depths[i]
        if (cur_win > prev_win):
            inc += 1

    return inc

f = open('input.txt', 'r')
with f:
    depths = [int(number.strip()) for number in f.readlines()]

p1 = part1(depths)
p2 = part2(depths)

print(f"Total number of increments is {p1}")
print(f"Total number of increments is {p2}")
