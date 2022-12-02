import numpy as np
from collections import deque, defaultdict
import copy

filename = "input.txt"

with open(filename, 'r') as f:
    lines = [l.strip() for l in f.readlines()]

debug = False

class Tree:
    def __init__(self, parent):
        self.left = None
        self.right = None
        self.data = None
        self.prev = None
        self.next = None
        self.parent = parent

def print_tree(node, indent):
    if node.data is not None:
        print(indent * " ", node.data, end='')
        if node.prev:
            print(f", (prev={node.prev.data})", end='')
        if node.next:
            print(f", (next={node.next.data})", end='')
        print("")
    else:
        if node.left:
            print_tree(node.left, indent + 2)
        if node.right:
            print_tree(node.right, indent + 2)

def build_tree(line):
    root = Tree(None)
    current = root
    prev = None
    for c in line:
        if c == '[':
            current.left = Tree(current)
            current.right = Tree(current)
            current = current.left
        elif c == ']':
            assert current.parent, "Must have parent"
            current = current.parent
        elif c == ',':
            assert current.parent, "Must have parent"
            current = current.parent.right
        else:
            current.data = int(c)
            current.prev = prev
            if prev:
                prev.next = current
            prev = current
    assert current == root
    return root

def find_end(node):
    while node.data is None:
        node = node.right
    return node

def find_start(node):
    while node.data is None:
        node = node.left
    return node

def combine_tree(old, new):
    root = Tree(None)
    root.left = old
    root.right = new
    root.left.parent = root
    root.right.parent = root
    old_end = find_end(old)
    new_start = find_start(new)
    if debug:
        print("old end:", old_end.data, "new start:", new_start.data)
    old_end.next = new_start
    new_start.prev = old_end
    return root

def action_explode(node):
    assert node.data is not None
    prev = node.prev
    parent = node.parent
    assert parent
    sibling = node.parent.right
    assert sibling
    next_ = sibling.next
    if prev:
        prev.data += node.data
        prev.next = parent
        parent.prev = prev
    if next_:
        next_.data += sibling.data
        next_.prev = parent
        parent.next = next_
    # Update parent
    parent.left = None
    parent.right = None
    parent.data = 0

def check_for_explode(node, level):
    if level > 4 and node.data is not None and node.parent.right.data is not None:
        action_explode(node)
        return True
    else:
        if node.left:
            action = check_for_explode(node.left, level + 1)
            if action:
                return True
        if node.right:
            action = check_for_explode(node.right, level + 1)
            if action:
                return True
    return False

def action_split(node):
    left = node.data // 2
    right = (node.data + 1) // 2
    node.left = Tree(node)
    node.right = Tree(node)
    node.left.data = left
    node.right.data = right
    node.left.prev = node.prev
    node.left.next = node.right
    node.right.prev = node.left
    node.right.next = node.next
    if node.prev:
        node.prev.next = node.left
    if node.next:
        node.next.prev = node.right
    # Clear node
    node.data = None
    node.prev = None
    node.next = None

def check_for_split(node):
    if node.data is not None and node.data > 9:
        action_split(node)
        return True
    else:
        if node.left:
            action = check_for_split(node.left)
            if action:
                return True
        if node.right:
            action = check_for_split(node.right)
            if action:
                return True
    return False

def take_action(root):
    while True:
        action_taken = check_for_explode(root, 0)
        if action_taken:
            if debug:
                print('exploded:')
                print_tree(current, 0)
        else:
            action_taken = check_for_split(root)
            if action_taken and debug:
                print('splitted:')
                print_tree(current, 0)
        if not action_taken:
            break

def magnitude_recur(node):
    if node.left and node.right and node.left.data is not None and node.right.data is not None:
        node.data = 3 * node.left.data + 2 * node.right.data
        node.left = None
        node.right = None
        return True
    else:
        if node.left:
            action = magnitude_recur(node.left)
            if action:
                return True
        if node.right:
            action = magnitude_recur(node.right)
            if action:
                return True

    return False

def calculate_magnitude(root):
    while True:
        action_taken = magnitude_recur(root)
        if not action_taken:
            return root.data

def part1(lines):
    current = build_tree(lines[0])
    if debug:
        print("start tree")
        print_tree(current, 0)
    for i, line in enumerate(lines[1:]):
        new_tree = build_tree(line)
        if debug:
            print("new tree")
            print_tree(new_tree, 0)
        current = combine_tree(current, new_tree)
        if debug:
            print("Reducing:")
            print_tree(current, 0)
        take_action(current)
    if debug:
        print("Result:")
        print_tree(current, 0)
    result = calculate_magnitude(current)
    return result

p1 = part1(lines)
print(f"Part 1: {p1}")

max_p2 = 0
for i in range(len(lines)):
    for j in range(len(lines)):
        if i == j:
            continue
        sublines = [lines[i], lines[j]]
        p2 = part1(sublines)
        max_p2 = max(p2, max_p2)

print(f"Part 2: {max_p2}")



