import numpy as np
from collections import deque, defaultdict
import copy
import heapq

filename = "input.txt"

ar1 = np.genfromtxt(filename, delimiter=1, dtype=int)

def shortest_path(ar):
    end = (ar.shape[0] - 1, ar.shape[1] - 1)

    visited = set()

    q = [(0, (0, 0))]
    visited.add((0, 0))
    heapq.heapify(q)

    while True:
        top = heapq.heappop(q)
        # print(top)
        if top[1] == end:
            return top[0]
        # Explore nbrs
        x, y = top[1]
        for offset in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new = (x + offset[0], y + offset[1])
            if new[0] < 0 or new[0] > end[0]:
                continue
            if new[1] < 0 or new[1] > end[1]:
                continue
            if new in visited:
                continue
            # print(new)
            new_cost = top[0] + ar[new[0], new[1]]
            # print(new_cost)
            heapq.heappush(q, (new_cost, new))
            visited.add(new)


result = shortest_path(ar1)
print(f"Part 1: {result}")

m = ar1.shape[0]
n = ar1.shape[1]
ar2 = np.zeros((m * 5, n * 5), dtype=int)
for i in range(5):
    for j in range(5):
        subar = ar1 + i + j
        subar = ((subar - 1) % 9) + 1
        starti = i * m
        endi = (i + 1) * m
        startj = j * n
        endj = (j + 1) * n
        ar2[starti:endi, startj:endj] = subar


result2 = shortest_path(ar2)
print(f"Part 2: {result2}")


