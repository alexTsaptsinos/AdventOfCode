from collections import defaultdict
import numpy as np

filename = "input.txt"

with open(filename, "r") as f:
    lines = [str(line).strip() for line in f.readlines()]

arr = np.zeros((1000, 1000), int)
arr2 = np.zeros((1000, 1000), int)
for line in lines:
    l = line.split()
    (x1, y1) = [int(x) for x in l[0].split(',')]
    (x2, y2) = [int(x) for x in l[2].split(',')]
    if x1 == x2:
        ystart = min(y1, y2)
        yend = max(y1, y2) + 1
        arr[x1, ystart:yend] += 1
        arr2[x1, ystart:yend] += 1
    elif y1 == y2:
        xstart = min(x1, x2)
        xend = max(x1, x2) + 1
        arr[xstart:xend, y1] += 1
        arr2[xstart:xend, y1] += 1
    else:
        xdiff = np.sign(x2 - x1)
        ydiff = np.sign(y2 - y1)
        while x1 != x2:
            arr2[x1, y1] += 1
            x1 += xdiff
            y1 += ydiff
        arr2[x1, y1] += 1


result = np.sum(arr > 1)
result2 = np.sum(arr2 > 1)
print(f"Part 1: {result}")
print(f"Part 2: {result2}")



