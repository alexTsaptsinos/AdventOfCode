import copy

with open("input.txt", "r") as f:
    lines = f.readlines()

instructions = [l for l in lines if l.startswith('move')]

init_idx = 0
for l in lines:
    if l.startswith('move'):
        break
    init_idx += 1

stack_idx = init_idx - 2
nstacks = int(lines[stack_idx].split()[-1])
stacks = [[] for i in range(nstacks)]

# init stacks
for i in range(stack_idx - 1, -1, -1):
    l = lines[i]
    for j, k in enumerate(range(1, 1 + nstacks * 4, 4)):
        if l[k] == ' ':
            continue
        stacks[j].append(l[k])

stacks2 = copy.deepcopy(stacks)
# instructions
for l in instructions:
    s = l.split()
    nmove = int(s[1])
    src = int(s[3]) - 1
    dst = int(s[5]) - 1

    stacks2[dst] += stacks2[src][-nmove:]

    for i in range(nmove):
        stacks[dst].append(stacks[src].pop())
        stacks2[src].pop()



part1 = ''.join([s[-1] for s in stacks])
part2 = ''.join([s[-1] for s in stacks2])
print(f"Part 1: {part1}")
print(f"Part 2: {part2}")
