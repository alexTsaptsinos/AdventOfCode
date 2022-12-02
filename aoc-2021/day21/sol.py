import numpy as np
from collections import deque, defaultdict
from itertools import product
import copy
import heapq

# example
start1 = 4
start2 = 8
# actual
start1 = 2
start2 = 8

nsides = 100
npositions = 10
target = 1000

def mod1(n, k):
    return (n - 1) % k + 1

die = 1
position1 = start1
position2 = start2
total1 = 0
total2 = 0
player1 = True
nrolls = 0
while total1 < target and total2 < target:
    this_roll = die
    die += 1
    die = mod1(die, nsides)
    this_roll += die
    die += 1
    die = mod1(die, nsides)
    this_roll += die
    die += 1
    die = mod1(die, nsides)
    if player1:
        position1 += this_roll
        position1 = mod1(position1, npositions)
        total1 += position1
        player1 = False
    else:
        position2 += this_roll
        position2 = mod1(position2, npositions)
        total2 += position2
        player1 = True

    nrolls += 3

part1 = nrolls * min(total1, total2)
print(f"Part 1: {part1}")

# Map from (position1, position2, total1, total2, player1) to number of universes win in
# Solution is thus dp[(start1, start2, 0, 0, True)]
dp = {}
possibilities = defaultdict(int)
die = [1, 2, 3]
target = 21
for x in die:
    for y in die:
        for z in die:
            possibilities[x + y + z] += 1

def calc(position1, position2, total1, total2, player1):
    # print("Calling:", position1, position2, total1, total2, player1)
    if total1 >= target:
        return 1
    if total2 >= target:
        return 0
    if (position1, position2, total1, total2, player1) in dp:
        return dp[(position1, position2, total1, total2, player1)]
    total = 0
    if player1:
        for key, val in possibilities.items():
            new_position = mod1(position1 + key, npositions)
            total += val * calc(new_position, position2, total1 + new_position, total2, False)
    else:
        for key, val in possibilities.items():
            new_position = mod1(position2 + key, npositions)
            total += val * calc(position1, new_position, total1, total2 + new_position, True)
    # print("Added", total1, total2, player1, " = ", total)
    dp[(total1, total2, player1)] = total
    return total

player1 = calc(start1, start2, 0, 0, True)
player2 = calc(start1, start2, 0, 0, False)
part2 = max(player1, player2)
print(f"Part 2: {part2}")




