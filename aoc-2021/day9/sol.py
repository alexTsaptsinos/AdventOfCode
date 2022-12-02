import numpy as np
from collections import defaultdict

filename = "input.txt"

with open(filename, "r") as f:
    lines = [str(line).strip() for line in f.readlines()]

m = len(lines)
n = len([int(x) for x in lines[0]])
ar = np.zeros((m, n), int)
for i, line in enumerate(lines):
    for j, x in enumerate(line):
        ar[i, j] = int(x)

seen = set()

def find_basin(i, j):
    if (i, j) in seen:
        return 0
    seen.add((i, j))
    local_sz = 1
    if i > 0 and ar[i - 1, j] > ar[i, j] and ar[i - 1, j] < 9:
        local_sz += find_basin(i - 1, j)
    if i < (m - 1) and ar[i + 1, j] > ar[i, j] and ar[i + 1, j] < 9:
        local_sz += find_basin(i + 1, j)
    if j > 0 and ar[i, j - 1] > ar[i, j] and ar[i, j - 1] < 9:
        local_sz += find_basin(i, j - 1)
    if j < (n - 1) and ar[i, j + 1] > ar[i, j] and ar[i, j + 1] < 9:
        local_sz += find_basin(i, j + 1)
    return local_sz

result = 0
basin_sizes = []
for i in range(m):
    for j in range(n):
        if i > 0 and ar[i, j] >= ar[i - 1, j]:
            continue
        if i < (m - 1) and ar[i, j] >= ar[i + 1, j]:
            continue
        if j > 0 and ar[i, j] >= ar[i, j - 1]:
            continue
        if j < (n - 1) and ar[i, j] >= ar[i, j + 1]:
            continue
        seen.clear()
        result += ar[i, j] + 1
        basin_sz = find_basin(i, j)
        basin_sizes.append(basin_sz)

basin_sizes = sorted(basin_sizes, reverse=True)
result2 = np.prod(basin_sizes[:3])

print(f"Part 1: {result}")
print(f"Part 2: {result2}")

