#!/usr/bin/python3

f = open('input.txt', 'r')
with f:
    instructions = f.readlines()

x = 0
y = 0

for i in instructions:
    direction, value = i.split(' ')
    if direction == "forward" : x += int(value)
    if direction == "backward" : x -= int(value)
    if direction == "up" : y -= int(value)
    if direction == "down" : y += int(value)

print(x, y)
print(x*y)

x = 0
y = 0
aim = 0

for i in instructions:
    direction, value = i.split(' ')
    if direction == "forward" :
        x += int(value)
        y += (aim*int(value))
    if direction == "up" : aim -= int(value)
    if direction == "down" : aim += int(value)

print(f"x = {x}")
print(f"y = {y}")
print(f"aim = {aim}")
print(x*y)
