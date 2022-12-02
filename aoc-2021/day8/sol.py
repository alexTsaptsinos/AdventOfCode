import copy
import numpy as np
from collections import defaultdict

filename = "input.txt"

unique_lengths = [2, 3, 4, 7]
rev = {6:'b', 4:'e', 9:'f'}
orig = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9
}

with open(filename, "r") as f:
    lines = [str(line).strip() for line in f.readlines()]

result = 0
for line in lines:
    words = line.split()
    add = False
    for w in words:
        if w == '|':
            add = True
        elif add and len(w) in unique_lengths:
            result += 1

print(f"Part 1: {result}")

def calc_line(line):
    words = line.split()
    mapping = {}
    counts = defaultdict(int)
    idx = words.index('|')
    for w in words[:idx]:
        for l in w:
            counts[l] += 1

    word2 = [w for w in words if len(w) == 2][0]
    word4 = [w for w in words if len(w) == 4][0]

    for l, c in counts.items():
        if c == 8:
            if l in word2:
                mapping[l] = 'c'
            else:
                mapping[l] = 'a'
        elif c == 7:
            if l in word4:
                mapping[l] = 'd'
            else:
                mapping[l] = 'g'
        else:
            mapping[l] = rev[c]

    val = 0
    for w in words[(idx+1):]:
        val *= 10
        s = ""
        for l in w:
            s += mapping[l]
        s = ''.join(sorted(s))
        val += orig[s]
    return val

result = 0
for line in lines:
    result += calc_line(line)

print(f"Part 2: {result}")

