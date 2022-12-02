import numpy as np
from collections import deque, defaultdict
import copy
import heapq

txt = "target area: x=20..30, y=-10..-5"
txt = "target area: x=169..206, y=-108..-68"

targetx = [20, 30]
targety = [-10, -5]
targetx = [169, 206]
targety = [-108, -68]

# initial = (0, 0)
# velocity = (x, y)

# step1 = (x, y)
# x -= np.sign(x)
# y -= 1
# step2 = (x + (x - 1), y + (y - 1))
# step3 = (x + (x - 1) + (x - 2), y + (y - 1) + (y - 2))
# stepn = (n*x - n * (n + 1) / 2, n * y - n * (n + 1) / 2)

size = 500
offset = size // 2
arx = np.zeros((size, size), dtype=int)
ary = np.zeros((size, size), dtype=int)
step = 0
highesty = np.zeros((size, size), dtype=int)
achieved = np.zeros((size, size), dtype=int)
while np.any(arx <= targetx[1]) and np.any(ary >= targety[1]):
    for i in range(size):
        xspeed = i - offset
        for j in range(size):
            yspeed = j - offset
            arx[i, j] += max(xspeed - step, 0)
            ary[i, j] += yspeed - step
            highesty[i, j] = max(ary[i, j], highesty[i, j])
            if arx[i, j] >= targetx[0] and arx[i, j] <= targetx[1] \
                    and ary[i, j] >= targety[0] and ary[i, j] <= targety[1]:
                        achieved[i, j] = 1
    step += 1

b = achieved * highesty
idx = np.argmax(b, axis=0)
i, j = np.unravel_index(b.argmax(), b.shape)
part1 = (i - offset, j - offset)
print(f"Part 1: {part1} with height {highesty[i, j]}")

part2 = np.sum(achieved)
print(f"Part 2: {part2}")
