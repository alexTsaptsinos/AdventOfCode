import numpy as np
from collections import deque, defaultdict
from itertools import product
import copy
import heapq

filename = 'input.txt'

with open(filename, 'r') as f:
    lines = [l.strip() for l in f.readlines()]

points = []
idx = -1
for line in lines:
    if '---' in line:
        idx += 1
        points.append([])
        continue
    elif line == "":
        continue
    else:
        pts = [int(x) for x in line.split(',')]
        points[idx].append(pts)

points = [np.array(x) for x in points]

vs = [np.array([1, 0, 0]), np.array([0, 1, 0]), np.array([0, 0, 1])]
vs2 = [-v for v in vs]
vs = vs + vs2
trans_matrices = []
for v in vs:
    for v2 in vs:
        if np.dot(v, v2) != 0:
            continue
        for v3 in vs:
            if np.dot(v, v3) != 0:
                continue
            if np.dot(v2, v3) != 0:
                continue
            m = np.zeros((3, 3), dtype=int)
            m[:,0] = v
            m[:,1] = v2
            m[:,2] = v3
            det = np.linalg.det(m)
            if det > 0:
                trans_matrices.append(m)

scanner_coords = [np.array([0,0,0], dtype=int)]

def check_match(matched, unmatched):
    for m in trans_matrices:
        tunmatched = np.matmul(unmatched, m)
        for p, p2 in product(tunmatched, matched):
            translation = p2 - p
            translated_pts = []
            for pt in tunmatched:
                t = pt + translation
                translated_pts.append((t[0], t[1], t[2]))
            overlap = [x for x in translated_pts if x in matched]
            if len(overlap) > 11:
                matched.update(translated_pts)
                scanner_coords.append((translation))
                return True

def find_match(matched, unmatched):
    for i, unmatch in enumerate(unmatched):
        if check_match(matched, unmatch):
            return i

matched = set([(x[0], x[1], x[2]) for x in points[0]])
unmatched = points[1:]

while len(unmatched) > 0:
    idx = find_match(matched, unmatched)
    del unmatched[idx]

part1 = len(matched)
print(f"Part 1: {part1}")

# Find largest distance
max_dist = 0
for i in range(len(scanner_coords)):
    for j in range(i + 1, len(scanner_coords)):
        p1 = scanner_coords[i]
        p2 = scanner_coords[j]
        d = np.sum(np.abs(p1 - p2))
        max_dist = max(max_dist, d)

print(f"Part 2: {max_dist}")


