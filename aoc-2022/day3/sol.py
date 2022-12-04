with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

def priority(c):
    if c.isupper():
        pts = ord(c) - ord('A') + 27
    else:
        pts = ord(c) - ord('a') + 1
    return pts

part1 = 0
for l in lines:
    n = len(l) // 2
    first = l[0:n]
    second = l[n:]
    lts1 = set(first)
    lts2 = set(second)
    intersect = lts1.intersection(lts2)
    assert len(intersect) == 1
    c = intersect.pop()
    part1 += priority(c)

print(f"Part 1: {part1}")

nlines = len(lines)
part2 = 0
for i in range(nlines // 3):
    lts1 = set(lines[3 * i])
    lts2 = set(lines[3 * i + 1])
    lts3 = set(lines[3 * i + 2])
    intersect = lts1.intersection(lts2).intersection(lts3)
    assert len(intersect) == 1
    c = intersect.pop()
    part2 += priority(c)

print(f"Part 2: {part2}")
