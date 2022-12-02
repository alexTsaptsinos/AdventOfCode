import numpy as np
from collections import deque, defaultdict
from itertools import product
import copy
import heapq
import sympy as sym

filename = "input.txt"

with open(filename, 'r') as f:
    lines = f.readlines()

# w = sym.Symbol('w')
# x = sym.Symbol('x')
# y = sym.Symbol('y')
# z = sym.Symbol('z')

# str2sym = {
#     'w': w,
#     'x': x,
#     'y': y,
#     'z': z,
# }

# model = [9] * 14
# model_idx = 0

done = False

def test_inputs(inputs):
    vals = {
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
    }
    val_idx = 0
    ws = []
    xs = []
    ys = []
    zs = []
    for line in lines:
        l = line.strip().split()
        if len(l) == 2:
            if val_idx > 0:
                ws.append(vals['w'])
                xs.append(vals['x'])
                ys.append(vals['y'])
                zs.append(vals['z'])
            # Input
            vals['w'] = inputs[val_idx]
            val_idx += 1
        else:
            # Op
            val2 = vals[l[2]] if l[2] in vals else int(l[2])
            if l[0] == 'add':
                vals[l[1]] += val2
            elif l[0] == 'mul':
                vals[l[1]] *= val2
            elif l[0] == 'div':
                vals[l[1]] = vals[l[1]] // val2
            elif l[0] == 'mod':
                vals[l[1]] = vals[l[1]] % val2
            elif l[0] == 'eql':
                vals[l[1]] = 1 if vals[l[1]] == val2 else 0

    ws.append(vals['w'])
    xs.append(vals['x'])
    ys.append(vals['y'])
    zs.append(vals['z'])
    print(ws)
    print(xs)
    print(ys)
    print(zs)

    return zs

# inputs = [9] * 14
inputs = [6,9,9,1,4,9,9,9,9,7,5,3,6,9]
zs = test_inputs(inputs)

# print(inputs)
# print(zs)

