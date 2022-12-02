import numpy as np
from collections import deque, defaultdict
import copy

filename = "input.txt"

subs = {}
with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        l = line.strip().split()
        if len(l) == 0:
            continue
        elif len(l) == 1:
            polymer0 = l[0]
        else:
            subs[l[0]] = l[2]

n0 = len(polymer0)
pairs = [polymer0[i:(i + 2)] for i in range(n0 - 1)]
pair_counts = defaultdict(int)
for p in pairs:
    pair_counts[p] += 1

def step(counts):
    new_counts = copy.deepcopy(counts)
    for k, v in counts.items():
        if v == 0:
            continue
        new_counts[k] -= v
        s = subs[k]
        new_counts[k[0] + s] += v
        new_counts[s + k[1]] += v
    return new_counts

nsteps = 40
for i in range(nsteps):
    pair_counts = step(pair_counts)

dtotal = defaultdict(int)
for k, v in pair_counts.items():
    dtotal[k[0]] += v
dtotal[polymer0[-1]] += 1

vals = dtotal.values()
result = max(vals) - min(vals)
print(f"Part 1: {result}")
