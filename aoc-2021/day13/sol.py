import numpy as np
from collections import deque, defaultdict

filename = "input.txt"

M = 2000
ar = np.zeros((M, M), int)

folds = []
max_x = 0
max_y = 0
with open(filename, 'r') as f:
    lines = f.readlines()
    for line in lines:
        l = line.split()
        if len(l) == 0:
            continue
        if l[0] == 'fold':
            l = l[2].split('=')
            l[1] = int(l[1])
            folds.append(l)
        else:
            l = [int(x) for x in l[0].split(',')]
            ar[l[1], l[0]] = 1
            max_x = max(l[1], max_x)
            max_y = max(l[0], max_y)

ar = ar[:(max_x + 1), :(max_y + 1)]
print("Paper shape =", ar.shape)
nfolds = 1
result = 0
for i, f in enumerate(folds):
    f = folds[i]
    if f[0] == 'x':
        ar1 = ar[:, :f[1]]
        ar2 = ar[:, (f[1] + 1):]
        assert(ar1.shape == ar2.shape)
        # Flip ar2
        ar2 = ar2[:, ::-1]
        ar = ar1 | ar2
    else:
        ar1 = ar[:f[1], ]
        ar2 = ar[(f[1] + 1):, ]
        assert(ar1.shape == ar2.shape)
        # flip ar2
        ar2 = ar2[::-1, ]
        ar = ar1 | ar2
    if i == 0:
        result = np.sum(ar)

print(f"Part 1: {result}")

np.set_printoptions(linewidth=100)

print(ar)

