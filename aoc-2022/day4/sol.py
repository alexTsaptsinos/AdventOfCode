import numpy as np

with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

part1 = 0
part2 = 0
for l in lines:
    elf1, elf2 = l.split(',')
    l1, u1 = [int(x) for x in elf1.split('-')]
    l2, u2 = [int(x) for x in elf2.split('-')]
    contained = (l2 <= l1 and u1 <= u2) or (l1 <= l2 and u2 <= u1)
    overlap = (l2 <= l1 and l1 <= u2) or (l1 <= l2 and l2 <= u1)
    part1 += contained
    part2 += overlap

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
