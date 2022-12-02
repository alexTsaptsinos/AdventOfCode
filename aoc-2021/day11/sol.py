import numpy as np
from collections import deque

filename = "input.txt"

ar = np.genfromtxt(filename, delimiter=1, dtype=int)
m = ar.shape[0]
n = ar.shape[1]

def flash(i, j, current):
    for x in [-1, 0, 1]:
        inew = i + x
        if inew < 0 or inew == m:
            continue
        for y in [-1, 0, 1]:
            jnew = j + y
            if jnew < 0 or jnew == n:
                continue
            if current[inew, jnew] == 0:
                continue
            current[inew, jnew] += 1
            if current[inew, jnew] > 9:
                current[inew, jnew] = 0
                flash(inew, jnew, current)


def take_step(current):
    current += 1
    for i in range(m):
        for j in range(n):
            if current[i, j] > 9:
                current[i, j] = 0
                flash(i, j, current)
    nflashes = np.sum(current == 0)
    return nflashes

nsteps = 100
result = 0
step = 0
allflash = m * n
l = 0
while l != allflash:
    l = take_step(ar)
    if step < nsteps:
        result += l
    step += 1

print(f"Part 1: {result}")
print(f"Part 2: {step}")
