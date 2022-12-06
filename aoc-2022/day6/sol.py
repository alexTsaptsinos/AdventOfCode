with open("input.txt", "r") as f:
    inp = f.readline().strip()

n = len(inp)

def nonrepeat(k):
    """"
    Find first non-repeating sequence of length k and return the index it
    occurs.
    """
    for i in range(0, n - k):
        s = set(inp[i:i + k])
        if len(s) == k:
            return i + k

print(f"Part 1: {nonrepeat(4)}")
print(f"Part 2: {nonrepeat(14)}")
