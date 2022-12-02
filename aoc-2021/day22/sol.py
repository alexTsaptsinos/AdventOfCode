import numpy as np
from collections import deque, defaultdict
from itertools import product
import copy
import heapq

filename = "input.txt"

with open(filename, 'r') as f:
    lines = f.readlines()

lines = [l.strip().split() for l in lines]

def pos_to_idx(x):
    x = max(-51, x)
    x = min(51, x)
    x = x + 50
    return x

ar = np.zeros((101, 101, 101), dtype=int)

for l in lines:
    l[1] = l[1].split(',')
    l[1] = [el[2:].split('..') for el in l[1]]
    l[1] = [item for sublist in l[1] for item in sublist]
    l[1] = [int(x) for x in l[1]]

for line in lines:
    mask = 1 if line[0] == 'on' else 0
    xstart = pos_to_idx(line[1][0])
    xend = pos_to_idx(line[1][1])
    ystart = pos_to_idx(line[1][2])
    yend = pos_to_idx(line[1][3])
    zstart = pos_to_idx(line[1][4])
    zend = pos_to_idx(line[1][5])
    ar[xstart:xend+1, ystart:yend+1, zstart:zend+1] = mask

part1 = np.sum(ar)
print(f"Part 1: {part1}")

class Range:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def length(self):
        return (self.end - self.start)

    def __and__(self, other):
        return self.start <= other.end and self.end >= other.start

    def __contains__(self, other):
        return self.start <= other.start and self.end >= other.end

    def __repr__(self):
        rep = f"[{self.start},{self.end})"
        return rep

    def __str__(self):
        rep = f"[{self.start},{self.end})"
        return rep

class Cube:
    def __init__(self, xstart, xend, ystart, yend, zstart, zend):
        self.x = Range(xstart, xend)
        self.y = Range(ystart, yend)
        self.z = Range(zstart, zend)

    def volume(self):
        return self.x.length() * self.y.length() * self.z.length()

    def __and__(self, other):
        return self.x & other.x and self.y & other.y and self.z & other.z

    def __contains__(self, other):
        return other.x in self.x and other.y in self.y and other.z in self.z

    def __sub__(self, other):
        # if this cube contained in other
        if self in other:
            return []

        # if no intersection
        if not (self & other):
            return [self]

        xs = [self.x.start]
        if self.x.start < other.x.start < self.x.end:
            xs.append(other.x.start)
        if self.x.start < other.x.end < self.x.end:
            xs.append(other.x.end)
        xs.append(self.x.end)

        ys = [self.y.start]
        if self.y.start < other.y.start < self.y.end:
            ys.append(other.y.start)
        if self.y.start < other.y.end < self.y.end:
            ys.append(other.y.end)
        ys.append(self.y.end)

        zs = [self.z.start]
        if self.z.start < other.z.start < self.z.end:
            zs.append(other.z.start)
        if self.z.start < other.z.end < self.z.end:
            zs.append(other.z.end)
        zs.append(self.z.end)

        result = []
        for xfrom, xto in zip(xs, xs[1:]):
            for yfrom, yto in zip(ys, ys[1:]):
                for zfrom, zto in zip(zs, zs[1:]):
                    r = Cube(xfrom, xto, yfrom, yto, zfrom, zto)
                    if r in other or r.volume() <= 0:
                        continue
                    result.append(r)

        return result

    def __repr__(self):
        rep = "{} x {} x {}".format(self.x, self.y, self.z)
        return rep

    def __str__(self):
        rep = "{} x {} x {}".format(self.x, self.y, self.z)
        return rep


def update_cubes(cubes, new_cube, add):
    new_cubes = []
    for cube in cubes:
        new_cubes.extend(cube - new_cube)

    if add:
        new_cubes.append(new_cube)
    return new_cubes

cubes = []
for i, line in enumerate(lines):
    new_cube = Cube(line[1][0], line[1][1] + 1, line[1][2], line[1][3] + 1, line[1][4], line[1][5] + 1)
    if line[0] == 'on':
        cubes = update_cubes(cubes, new_cube, True)
    else:
        cubes = update_cubes(cubes, new_cube, False)

part2 = 0
for cube in cubes:
    part2 += cube.volume()

print(f"Part 2: {part2}")

