from collections import defaultdict
import numpy as np

filename = "input.txt"

class BingoCard:
    def __init__(self, lines, num2card, idx):
        self.card = np.zeros((5, 5), dtype=int)
        self.marked = np.zeros((5, 5), dtype=bool)
        self.rows = 5 * [0]
        self.cols = 5 * [0]
        for row, line in enumerate(lines):
            vals = [int(x) for x in line.split()]
            for col, val in enumerate(vals):
                self.card[row][col] = val
                num2card[val].append((idx, row, col))

    def mark(self, row, col):
        self.rows[row] += 1
        self.cols[col] += 1
        self.marked[row][col] = True
        return (self.rows[row] == 5 or self.cols[col] == 5)

    def final_result(self, draw):
        # marked = np.sum(self.card * self.marked)
        print(self.card)
        print(self.marked)
        unmarked = np.sum(self.card * np.logical_not(self.marked))
        print("unmarked = ", unmarked)
        return draw * unmarked


with open(filename, "r") as f:
    lines = [str(line).strip() for line in f.readlines()]
    draws = [int(x) for x in lines[0].split(',')]
    idx = 2
    bingo_cards = []
    num2card = defaultdict(list)
    while idx < len(lines):
        b = BingoCard(lines[idx:(idx + 5)], num2card, len(bingo_cards))
        bingo_cards.append(b)
        idx += 6

    card = None
    final_draw = None
    final_i = None
    for i, draw in enumerate(draws):
        for (idx, row, col) in num2card[draw]:
            if bingo_cards[idx].mark(row, col):
                # Done!!
                if not card:
                    card = idx
                    final_draw = draw
                    final_i = i
        if card:
            break

    print("card=",card)
    print("final_draw=",final_draw)
    result = bingo_cards[card].final_result(final_draw)
    print(f"Part 1: {result}")
    print(draws)

    # Keep playing for Part 2
    cards_done = [False] * len(bingo_cards)
    cards_done[card] = True
    num_cards_done = 1
    final_draw = None
    card = None
    for draw in draws[(final_i + 1):]:
        print("draw = ", draw)
        for (idx, row, col) in num2card[draw]:
            if cards_done[idx]:
                continue
            print("marking:", idx)
            if bingo_cards[idx].mark(row, col):
                print(idx, "is done")
                cards_done[idx] = True
                num_cards_done += 1
                if num_cards_done == len(bingo_cards):
                    final_draw = draw
                    card = idx
                    break
        if card:
            break

    result = bingo_cards[card].final_result(final_draw)
    print(f"Part 2: {result}")



