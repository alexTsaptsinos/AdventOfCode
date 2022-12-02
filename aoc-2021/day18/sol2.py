import numpy as np
from collections import deque, defaultdict
import copy

filename = "basic_input5.txt"

with open(filename, 'r') as f:
    lines = [l.strip() for l in f.readlines()]

print(lines)

def process_line(cur):
    depths = []
    depth = 0
    raw = []
    for l in cur:
        if l == '[':
            depth += 1
        elif l == ']':
            depth -= 1
        elif l == ',':
            continue
        else:
            depths.append(depth)
            raw.append(int(l))
    return raw, depths

def split(current, depths, i):
    print("SPLIT AT", i)
    print(current, depths)
    left = current[i] // 2
    right = (current[i] + 1) // 2
    current.insert(i, left)
    current[i + 1] = right
    depths.insert(i, depths[i] + 1)
    depths[i + 1] = depths[i]
    print("AFTERSPLIT:", current, depths)

def explode(current, depths, i):
    print("EXPLODE AT", i)
    print(current, depths)
    if i > 0:
        current[i - 1] += current[i]
    assert depths[i + 1] > 4, "Expect next to also be greater"
    if (i + 2) < len(depths):
        current[i + 2] += current[i + 1]

    print("UPDATED:", current, depths)

    current[i] = 0
    depths[i] -= 1
    del current[i + 1]
    del depths[i + 1]

    print("AFTER", current, depths)
    if current[i - 1] > 9:
        split(current, depths, i - 1)
    if current[i] > 9:
        split(current, depths, i)
    return current, depths

def take_action(current, depths):
    while True:
        action_taken = False
        for i, d in enumerate(depths):
            if d > 4:
                current, depths = explode(current, depths, i)
                action_taken = True
                break
        if not action_taken:
            break

def add_line(lold, dold, new):
    lnew, dnew = process_line(new)
    print("NEW", lnew, dnew)
    dold = [x+1 for x in dold] + [x+1 for x in dnew]
    lold += lnew
    print("CUR", lold, dold)
    take_action(lold, dold)
    # dnew = calculate_depths(new)
    # cur = '[' + cur + ',' + new + ']'
    # d = [x+1 for x in d]
    # d2 = [x+1 for x in dnew]
    # d = d + d2
    return lold, dold

current, depths = process_line(lines[0])
print(current)
print("depths =", depths)

for line in lines[1:]:
    current, depths = add_line(current, depths, line)
