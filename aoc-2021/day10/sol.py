import numpy as np
from collections import deque

filename = "input.txt"

with open(filename, "r") as f:
    lines = [str(line).strip() for line in f.readlines()]

scoring = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
pair = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}
scoring2 = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}

def parse_line(line):
    q = deque()
    for c in line:
        if c in pair:
            top = q.pop()
            if pair[c] != top:
                return (True, scoring[c])
        else:
            q.append(c)

    score2 = 0
    while len(q):
        c = q.pop()
        score2 *= 5
        score2 += scoring2[c]

    return (False, score2)

result = 0
scores = []
for line in lines:
    (part1, r) = parse_line(line)
    if part1:
        result += r
    else:
        scores.append(r)

result2 = np.median(scores)


print(f"Part 1: {result}")
print(f"Part 2: {result2}")

