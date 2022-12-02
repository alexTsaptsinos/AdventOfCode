filename = "input.txt"

pos = 0
depth = 0
with open(filename, "r") as f:
    for line in f.readlines():
        l = line.split(' ')
        cmd = l[0]
        val = int(l[1])
        if cmd == "forward":
            pos += val
        elif cmd == "down":
            depth += val
        elif cmd == "up":
            depth -= val
        else:
            assert False, "Invald cmd: {}".format(cmd)

result = pos * depth

print("Part 1")
print(f"Position={pos}, Depth={depth}, Result={result}")

aim = 0
pos = 0
depth = 0
with open(filename, "r") as f:
    for line in f.readlines():
        l = line.split(' ')
        cmd = l[0]
        val = int(l[1])
        if cmd == "forward":
            pos += val
            depth += aim * val
        elif cmd == "down":
            aim += val
        elif cmd == "up":
            aim -= val
        else:
            assert False, "Invald cmd: {}".format(cmd)

result = pos * depth
print("Part 2")
print(f"Position={pos}, Depth={depth}, Result={result}")
