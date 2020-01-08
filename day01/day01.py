"""Advent of code 2019 day 1"""

import math

data = [line.rstrip('\n') for line in open("data.txt")]

data = list(map(int, data))

def calc_fuel(x):
    return math.floor(x/3) - 2

#part 1
total = 0
for i in data:
    total = total + calc_fuel(i)
print(total)

#part 2
total = 0
for i in data:
    while ((i/3) - 2) > 0:
        i = calc_fuel(i)
        total = total + i
print(total)
