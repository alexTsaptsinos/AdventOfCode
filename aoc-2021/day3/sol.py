filename = "input.txt"

with open(filename, "r") as f:
    lines = [str(line).strip() for line in f.readlines()]
    n = len(lines[0])
    counts = [sum([int(line[i]) for line in lines]) for i in range(n)]
    vals = [i >= (len(lines) / 2) for i in counts]
    gamma = 0
    epsilon = 0
    for i, val in enumerate(vals):
        gamma |= (val << (n - 1 - i))
        epsilon |= ((not val) << (n - 1 - i))

power = gamma * epsilon
print(f"Part 1 = {power}")

with open(filename, "r") as f:
    lines = [str(line).strip() for line in f.readlines()]
    n = len(lines[0])
    idx = 0
    while len(lines) > 1:
        count = sum([int(line[idx]) for line in lines])
        val = count >= len(lines) / 2
        lines = [line for line in lines if int(line[idx]) == val]
        idx += 1
    assert(len(lines) == 1)
    oxygen = int(lines[0], 2)

with open(filename, "r") as f:
    lines = [str(line).strip() for line in f.readlines()]
    idx = 0
    while len(lines) > 1:
        count = sum([int(line[idx]) for line in lines])
        val = count < len(lines) / 2
        lines = [line for line in lines if int(line[idx]) == val]
        idx += 1
    assert(len(lines) == 1)
    co2 = int(lines[0], 2)

life = oxygen * co2
print(f"Part 2 = {life}")
