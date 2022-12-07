limit = 100000
disk_space = 70000000
space_needed = 30000000

with open("input.txt", "r") as f:
    lines = f.readlines()

class Node(object):
    def __init__(self, name, is_dir, size, parent):
        self.name = name
        self.is_dir = is_dir
        self.size = size
        self.children = dict()
        self.parent = parent
        self.total_size = 0

    def name(self):
        return self.name

    def add_child(self, name, is_dir, size):
        child = Node(name, is_dir, size, self)
        self.children[name] = child

    def has_child(self, name):
        return name in self.children

    def child(self, name):
        return self.children[name]

    def __repr__(self):
        t = "dir" if self.is_dir else "file"
        if not self.is_dir:
            t += f", size={self.size}"
        return f"- {self.name} ({t})"

def print_tree(sep, n):
    print(f"{sep}{n}")
    for name, child in n.children.items():
        print_tree(sep + "  ", child)

def print_total_sizes(sep, n):
    print(f"{sep}{n}")
    for name, child in n.children.items():
        print_tree(sep + "  ", child)

# build the tree
root = Node("/", True, 0, None)
current = None
for l in lines:
    s = l.split()
    if s[0] == "$":
        # command
        if s[1] == "cd":
            if s[2] == "/":
                current = root
            elif s[2] == "..":
                assert current.parent is not None
                current = current.parent
            else:
                assert current.has_child(s[2]), f"{current.name()} has no child named {s[2]}"
                current = current.child(s[2])
        elif s[1] == "ls":
            pass
    elif s[0] == "dir":
        # directory
        current.add_child(s[1], True, 0)
    else:
        # file
        current.add_child(s[1], False, int(s[0]))
# Part 1: find directory sizes
part1 = 0
def total_size(n):
    global part1
    for name, child in n.children.items():
        if child.is_dir:
            n.total_size += total_size(child)
        else:
            n.total_size += child.size
    if n.total_size <= limit:
        part1 += n.total_size
    return n.total_size

total_size(root)
print(f"Part 1: {part1}")

space_used = root.total_size
unused_space = disk_space - space_used
extra_required = space_needed - unused_space
print(f"Extra space required: {extra_required}")

# Part 2: find smallest directory larger than extra_required
part2 = space_used
def smallest_dir(n):
    global part2
    for name, child in n.children.items():
        if child.is_dir:
            smallest_dir(child)
    if n.total_size >= extra_required and n.total_size < part2:
        part2 = n.total_size

smallest_dir(root)
print(f"Part 2: {part2}")
