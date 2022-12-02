with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

all_calories = []
elf_calories = 0
for l in lines:
    if len(l) == 0:
        all_calories.append(elf_calories)
        elf_calories = 0
    else:
        elf_calories += int(l)

all_calories.sort(reverse=True)
print(f"Part 1: {all_calories[0]}")
part2 = sum(all_calories[0:3])
print(f"Part 2: {part2}")
