filename = "input.txt"

part1 = 0
part2 = 0
with open(filename, "r") as f:
    lines = [int(i) for i in f.readlines()]
    for i, line in enumerate(lines):
        # Part 1
        if i > 0:
            if lines[i] > lines[i - 1]:
                part1 += 1

        # Part 2
        if i > 2:
            prev = lines[i - 3] + lines[i - 2] + lines[i - 1]
            current = lines[i - 2] + lines[i - 1] + lines[i]
            if current > prev:
                part2 += 1

print("Part 1: Increased {} times".format(part1))
print("Part 2: Increased {} times".format(part2))

