import itertools,re
f = open("input13.txt","r")
textLines = f.readlines()

# Create a dictionary of happiness points

globalDic = {}
names = ["Alice","Bob","Carol","David","Eric","Frank","George","Mallory"]

for name in names:
    globalDic[name] = {}

for line in textLines:
    splitLine = line.split()
    firstName = splitLine[0]
    secondName = splitLine[-1]
    secondName = re.sub("\.","",secondName)
    direction = splitLine[2]
    amount = int(splitLine[3])
    if direction == "gain":
        globalDic[firstName][secondName] = amount
    else:
        globalDic[firstName][secondName] = -amount

print(globalDic)

# Now find optimal
def findOptimalHappiness(names):
    perms = itertools.permutations(names)

    maxHappiness = 0

    for perm in perms:
        happiness = 0
        for i in range(len(names)-1):
            happiness += globalDic[perm[i]][perm[i+1]] + globalDic[perm[i+1]][perm[i]]

        happiness += globalDic[perm[0]][perm[len(names)-1]] + globalDic[perm[len(names)-1]][perm[0]]
        maxHappiness = max(maxHappiness,happiness)

    return maxHappiness

# PART A
maxHappiness = findOptimalHappiness(names)
print("Optimal Seating Happiness:",maxHappiness)

# PART B
# First extend the globalDic to include you
globalDic["Me"] = {}
for name in names:
    globalDic["Me"][name] = 0
    globalDic[name]["Me"] = 0

namesPartB = names + ["Me"]
maxHappiness = findOptimalHappiness(namesPartB)

print("And with me included:",maxHappiness)