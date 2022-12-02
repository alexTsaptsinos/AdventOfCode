import numpy as np
from collections import deque, defaultdict

filename = "input.txt"

with open(filename, 'r') as f:
    lines = f.readlines()

lines = [x.strip().split('-') for x in lines]

adj = defaultdict(set)
for s, t in lines:
    adj[s].add(t)
    adj[t].add(s)

seen = set()
npaths = [0]

def backtrack(s, seen):
    # print("Exploring", s)
    if s.islower():
        # print("Adding to seen", s)
        seen.add(s)
    for t in adj[s]:
        if t in seen:
            continue
        if t == 'end':
            # print("Incrementing", s)
            npaths[0] += 1
            continue
        backtrack(t, seen)
    if s.islower():
        # print("Removing from seen", s)
        seen.remove(s)

backtrack('start', seen)

print(f"Part 1: {npaths[0]}")

seen.clear()
npaths = [0]

def backtrack(s, seen, seentwice):
    # print("Exploring", s)
    flag = False
    if s.islower():
        if s in seen:
            # print("seentwice", s)
            flag = True
            seentwice = True
        else:
            # print("Adding to seen", s)
            seen.add(s)
    for t in adj[s]:
        if t in seen:
            if seentwice or t == 'start':
                continue
        if t == 'end':
            # print("Incrementing", s)
            npaths[0] += 1
            continue
        backtrack(t, seen, seentwice)
    if s.islower():
        if flag:
            # print("removing seentwice", s)
            seentwice = False
        else:
            # print("Removing from seen", s)
            seen.remove(s)

backtrack('start', seen, False)


print(f"Part 2: {npaths[0]}")
