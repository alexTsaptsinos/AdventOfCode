import numpy as np
from collections import deque, defaultdict
import copy
import heapq

filename = "input.txt"
scale = 16

with open(filename, 'r') as f:
    hexval = f.readlines()[0].strip()

b = ''
for l in hexval:
    d = bin(int(l, scale))[2:].zfill(4)
    b += '{}'.format(d)

part1 = [0]
def decode_packet(idx):
    # print("DECODE:", idx)
    v = int(b[idx:idx+3], 2)
    part1[0] += v
    # print("v=",v)
    idx += 3
    t = int(b[idx:idx+3], 2)
    idx += 3
    # print("t=",t)
    if t == 4:
        s = ''
        # print("literal")
        while True:
            s += b[idx+1:idx+5]
            if b[idx] == '0':
                idx += 5
                break
            else:
                idx += 5
        # print("s=",s)
        a = int(s, 2)
        # print("a=",a)
    else:
        i = int(b[idx], 2)
        idx += 1
        # print("i=",i)
        if i == 0:
            l = int(b[idx:idx+15], 2)
            # print("l=",l)
            idx += 15
            end = idx + l
            while idx < end:
                idx = decode_packet(idx)
        else:
            l = int(b[idx:idx+11], 2)
            # print("l=",l)
            idx += 11
            for i in range(l):
                idx = decode_packet(idx)

    return idx


decode_packet(0)
print(f"Part 1: {part1[0]}")

def decode_packet2(idx):
    v = int(b[idx:idx+3], 2)
    part1[0] += v
    idx += 3
    t = int(b[idx:idx+3], 2)
    idx += 3
    val = 0
    if t == 4:
        s = ''
        while True:
            s += b[idx+1:idx+5]
            if b[idx] == '0':
                idx += 5
                break
            else:
                idx += 5
        a = int(s, 2)
        val = a
    else:
        i = int(b[idx], 2)
        idx += 1
        vals = []
        if i == 0:
            l = int(b[idx:idx+15], 2)
            idx += 15
            end = idx + l
            while idx < end:
                idx, v = decode_packet2(idx)
                vals.append(v)
        else:
            l = int(b[idx:idx+11], 2)
            idx += 11
            for i in range(l):
                idx, v = decode_packet2(idx)
                vals.append(v)
        if t == 0:
            val = np.sum(vals)
        elif t == 1:
            val = np.prod(vals)
        elif t == 2:
            val = min(vals)
        elif t == 3:
            val = max(vals)
        elif t == 5:
            val = 1 if vals[0] > vals[1] else 0
        elif t == 6:
            val = 1 if vals[0] < vals[1] else 0
        elif t == 7:
            val = 1 if vals[0] == vals[1] else 0

    return idx, val

_, part2 = decode_packet2(0)
print(f"Part 2: {part2}")


