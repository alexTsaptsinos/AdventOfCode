with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

# Part 1: X=rock, Y=paper, Z=scissors
part1 = 0
for line in lines:
    elf, you = [ord(l) for l in line.split()]
    elf -= ord('A')
    you -= ord('X')

    pts = you + 1
    if elf == you:
        # draw
        pts += 3
    elif (you + 2) % 3 == elf:
        # win
        pts += 6


    part1 += pts

print(f"Part 1: {part1}")

# Part 2: X=lose, Y=draw, Z=win
part2 = 0
for line in lines:
    elf, outcome = [ord(l) for l in line.split()]
    elf -= ord('A')
    outcome -= ord('X')
    play = (elf + outcome + 2) % 3

    pts = outcome * 3 + play + 1
    part2 += pts

print(f"Part 2: {part2}")
