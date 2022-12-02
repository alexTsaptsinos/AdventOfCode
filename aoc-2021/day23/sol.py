import numpy as np
from collections import deque, defaultdict
from itertools import product
import copy
import heapq

energy = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000,
}

class Board:
    def __init__(self, a0, a1, b0, b1, c0, c1, d0, d1):
        self.top = ['.'] * 11
        self.aroom = [a0, a1]
        self.broom = [b0, b1]
        self.croom = [c0, c1]
        self.droom = [d0, d1]

        self.aidx = 2
        self.bidx = 4
        self.cidx = 6
        self.didx = 8

    def nbrs(self):
        result = []
        # Try to move anything in top into a room
        for i, c in enumerate(self.top):
            if c == '.':
                continue
            elif c == 'A':
                if 'B' in self.aroom or 'C' in self.aroom or 'D' in self.aroom:
                    continue
                step = np.sign(self.aidx - i)
                blocked = False
                for idx in range(i + step, self.aidx, step):
                    if self.top[idx] != '.':
                        blocked = True
                if blocked:
                    continue
                cost = abs(self.aidx - i) + 1
                new = copy.deepcopy(self)
                new.top[i] = '.'
                if new.aroom[1] == '.':
                    new.aroom[1] = 'A'
                    cost += 1
                else:
                    new.aroom[0] = 'A'
                result.append((cost, new))
            elif c == 'B':
                if 'A' in self.broom or 'C' in self.broom or 'D' in self.broom:
                    continue
                step = np.sign(self.bidx - i)
                blocked = False
                for idx in range(i + step, self.bidx, step):
                    if self.top[idx] != '.':
                        blocked = True
                if blocked:
                    continue
                cost = abs(self.bidx - i) + 1
                new = copy.deepcopy(self)
                new.top[i] = '.'
                if new.broom[1] == '.':
                    new.broom[1] = 'B'
                    cost += 1
                else:
                    new.broom[0] = 'B'
                result.append((cost * 10, new))
            elif c == 'C':
                if 'A' in self.croom or 'B' in self.croom or 'D' in self.croom:
                    continue
                step = np.sign(self.cidx - i)
                blocked = False
                for idx in range(i + step, self.cidx, step):
                    if self.top[idx] != '.':
                        blocked = True
                if blocked:
                    continue
                cost = abs(self.cidx - i) + 1
                new = copy.deepcopy(self)
                new.top[i] = '.'
                if new.croom[1] == '.':
                    new.croom[1] = 'C'
                    cost += 1
                else:
                    new.croom[0] = 'C'
                result.append((cost * 100, new))
            elif c == 'D':
                if 'A' in self.droom or 'B' in self.droom or 'C' in self.droom:
                    continue
                step = np.sign(self.didx - i)
                blocked = False
                for idx in range(i + step, self.didx, step):
                    if self.top[idx] != '.':
                        blocked = True
                if blocked:
                    continue
                cost = abs(self.didx - i) + 1
                new = copy.deepcopy(self)
                new.top[i] = '.'
                if new.droom[1] == '.':
                    new.droom[1] = 'D'
                    cost += 1
                else:
                    new.droom[0] = 'D'
                result.append((cost * 1000, new))

        def maybe(idxs, room, room_idx):
            for i in idxs:
                if self.top[i] != '.':
                    break
                new = copy.deepcopy(self)
                cost = 0
                letter = None
                if room == 'A':
                    new.top[i] = self.aroom[room_idx]
                    new.aroom[room_idx] = '.'
                    cost += abs(i - self.aidx) + room_idx + 1
                    letter = self.aroom[room_idx]
                elif room == 'B':
                    new.top[i] = self.broom[room_idx]
                    new.broom[room_idx] = '.'
                    cost += abs(i - self.bidx) + room_idx + 1
                    letter = self.broom[room_idx]
                elif room == 'C':
                    new.top[i] = self.croom[room_idx]
                    new.croom[room_idx] = '.'
                    cost += abs(i - self.cidx) + room_idx + 1
                    letter = self.croom[room_idx]
                elif room == 'D':
                    new.top[i] = self.droom[room_idx]
                    new.droom[room_idx] = '.'
                    cost += abs(i - self.didx) + room_idx + 1
                    letter = self.droom[room_idx]
                else:
                    assert False

                cost *= energy[letter]

                result.append((cost, new))

        if self.aroom[0] != '.':
            maybe([1, 0], 'A', 0)
            maybe([3, 5, 7, 9, 10], 'A', 0)
        elif self.aroom[1] not in ['.', 'A']:
            maybe([1, 0], 'A', 1)
            maybe([3, 5, 7, 9, 10], 'A', 1)

        if self.broom[0] != '.':
            maybe([3, 1, 0], 'B', 0)
            maybe([5, 7, 9, 10], 'B', 0)
        elif self.broom[1] not in ['.', 'B']:
            maybe([3, 1, 0], 'B', 1)
            maybe([5, 7, 9, 10], 'B', 1)

        if self.croom[0] != '.':
            maybe([5, 3, 1, 0], 'C', 0)
            maybe([7, 9, 10], 'C', 0)
        elif self.croom[1] not in ['.', 'C']:
            maybe([5, 3, 1, 0], 'C', 1)
            maybe([7, 9, 10], 'C', 1)

        if self.droom[0] != '.':
            maybe([7, 5, 3, 1, 0], 'D', 0)
            maybe([9, 10], 'D', 0)
        elif self.droom[1] not in ['.', 'D']:
            maybe([7, 5, 3, 1, 0], 'D', 1)
            maybe([9, 10], 'D', 1)

        return result

    def __repr__(self):
        result = '\n'
        result += '#' * 13
        result += '\n#'
        for c in self.top:
            result += c
        result += '#\n###'
        result += self.aroom[0] + '#'
        result += self.broom[0] + '#'
        result += self.croom[0] + '#'
        result += self.droom[0] + '###\n'
        result += '  #'
        result += self.aroom[1] + '#'
        result += self.broom[1] + '#'
        result += self.croom[1] + '#'
        result += self.droom[1] + '#  \n'
        result += '  #########  '
        return result

    def __str__(self):
        result = '\n'
        result += '#' * 13
        result += '\n#'
        for c in self.top:
            result += c
        result += '#\n###'
        result += self.aroom[0] + '#'
        result += self.broom[0] + '#'
        result += self.croom[0] + '#'
        result += self.droom[0] + '###\n'
        result += '  #'
        result += self.aroom[1] + '#'
        result += self.broom[1] + '#'
        result += self.croom[1] + '#'
        result += self.droom[1] + '#  \n'
        result += '  #########  '
        return result

    def __eq__(self, other):
        if self.top != other.top:
            return False
        if self.aroom != other.aroom:
            return False
        if self.broom != other.broom:
            return False
        if self.croom != other.croom:
            return False
        if self.droom != other.droom:
            return False
        return True

    def __hash__(self):
        return hash(str(self))

    def __lt__(self, other):
        return str(self) < str(other)

# start = Board('B', 'A', 'C', 'D', 'B', 'C', 'D', 'A')
start = Board('D', 'C', 'B', 'A', 'D', 'A', 'B', 'C')
print(start)
end = Board('A', 'A', 'B', 'B', 'C', 'C', 'D', 'D')

# start = Board('.', 'A', 'B', 'B', 'C', 'C', '.', 'A')
# start.top[5] = 'D'
# start.top[7] = 'D'
# print(start)
# print(start.nbrs())

def shortest_path():
    q = [(0, start)]
    heapq.heapify(q)
    # visited = set()
    # visited.add(start)
    shortest = {}

    while len(q) > 0:
        top = heapq.heappop(q)
        d, new = top
        if new in shortest:
            continue
        # print("TOP:", top)
        shortest[new] = d
        # d, new = heapq.heappop(q)
        if new == end:
            return d

        nbrs = new.nbrs()
        for cost, nb in nbrs:
            if nb in shortest:
                continue
            new_cost = d + cost
            # print("Exploring", new_cost, nb)
            heapq.heappush(q, (new_cost, nb))
            # visited.add(nb)



part1 = shortest_path()
print(f"Part 1: {part1}")










