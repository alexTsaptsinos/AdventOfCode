import numpy as np
from collections import deque, defaultdict
from itertools import product
import copy
import heapq

filename = 'input.txt'

with open(filename, 'r') as f:
    lines = [l.strip() for l in f.readlines()]

key = lines[0]
print(len(key))

height = len(lines[2:])
width = len(lines[2])
print("height =", height, "width =", width)
ar = np.zeros((height, width), dtype=int)

for i, l in enumerate(lines[2:]):
    for j, c in enumerate(l):
        if c == '.':
            ar[i, j] = 0
        elif c == '#':
            ar[i, j] = 1

s = ar.shape
print("Shape:", s)

def conv(m, i, j, fill):
    s = ''
    for row in [i - 1, i, i + 1]:
        for col in [j - 1, j, j + 1]:
            if row < 0 or row == m.shape[0]:
                s += '{}'.format(fill)
            elif col < 0 or col == m.shape[1]:
                s += '{}'.format(fill)
            else:
                s += '{}'.format(m[row, col])
    assert len(s) == 9
    b = int(s, 2)
    k = key[b]
    if k == '#':
        return 1
    else:
        return 0

def transform(m, fill):
    read = np.pad(m, 2, constant_values=fill)
    new = read.copy()
    for i in range(read.shape[0]):
        for j in range(read.shape[1]):
            new[i, j] = conv(read, i, j, fill)
    new_fill = 1 if key[511 * fill] == '#' else 0
    return new, new_fill

fill = 0
for i in range(50):
    ar, fill = transform(ar, fill)

part1 = np.sum(ar)
print(ar)
print(f"Part 1: {part1}")
