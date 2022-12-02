import numpy as np
from collections import deque, defaultdict
from itertools import product
import copy
import heapq
import sympy as sym

filename = "input.txt"

ar = np.genfromtxt(filename, delimiter=1, dtype=str)
m = ar.shape[0]
n = ar.shape[1]

def step(cur):
    new = cur.copy()
    changed = False
    for i in range(m):
        for j in range(n):
            if ar[i, j] == '>':
                next_j = (j + 1) % n
                if ar[i, next_j] == '.':
                    new[i, j] = '.'
                    new[i, next_j] = '>'
                    changed = True

    # print("intermediate")
    # print(new)

    new2 = new.copy()
    for i in range(m):
        for j in range(n):
            if new[i, j] == 'v':
                next_i = (i + 1) % m
                if new[next_i, j] == '.':
                    new2[i, j] = '.'
                    new2[next_i, j] = 'v'
                    changed = True

    return changed, new2


# print(ar)

niter = 0
while True:
    niter += 1
    change, ar = step(ar)
    # print(change)
    # print(ar)
    # break
    if not change:
        break

print(f"Part 1: {niter}")

