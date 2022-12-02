import numpy as np

filename = "input.txt"

with open(filename, "r") as f:
    lines = [str(line).strip() for line in f.readlines()]

init = [int(x) for x in lines[0].split(',')]

ar = np.array(init)

pos = np.median(ar)
print(f"Position: {pos}")
result = np.sum(abs(ar - pos))
print(f"Part 1: {result}")

pos = np.floor(np.mean(ar))
pos2 = np.ceil(np.mean(ar))
print(f"Position: {pos}")
v = abs(ar - pos)
v2 = abs(ar - pos2)
v = [x * (x + 1) / 2 for x in v]
v2 = [x * (x + 1) / 2 for x in v2]
result = np.sum(v)
result2 = np.sum(v2)
result = min(result, result2)
print(f"Part 2: {result}")





