import numpy as np

filename = "input.txt"
ndays = 256

with open(filename, "r") as f:
    lines = [str(line).strip() for line in f.readlines()]

init = [int(x) for x in lines[0].split(',')]
# print(init)

cache = {}

def produces_fish(days):
    if days in cache:
        return cache[days]
    result = days // 7 + 1
    resdays = days
    while (resdays - 9) >= 0:
        result += produces_fish(resdays - 9)
        resdays -= 7
    cache[days] = result
    # print(days, "=", result)
    return result


result = len(init)
for v in init:
    result += produces_fish(ndays - v - 1)

print(f"Part 1: {result}")
# result2 = np.sum(arr2 > 1)
# print(f"Part 2: {result2}")



