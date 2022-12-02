import itertools

f = open("input9.txt","r")
text = f.readlines()

cities = ["AlphaCentauri","Snowdin","Tambi","Faerun","Norrath","Straylight","Tristram","Arbre"]

no_cities = len(cities)

# First build a dictionary of dictionaries of lengths
distanceDic = {}
for city in cities:
    distanceDic[city] = {}

for line in text:
    splitLine = line.split()
    firstCity = splitLine[0]
    secondCity = splitLine[2]
    distance = int(splitLine[4])
    distanceDic[firstCity][secondCity] = distance
    distanceDic[secondCity][firstCity] = distance

# Now find minimum distance
perms = itertools.permutations(cities)
minDistance = 1000000000
maxDistance = 0

for perm in perms:
    distance = 0
    for i in range(no_cities-1):
        distance += distanceDic[perm[i]][perm[i+1]]

    minDistance = min(distance,minDistance)
    maxDistance = max(distance,maxDistance)

print("Minimum Distance:",minDistance)
print("Maximum Distance:",maxDistance)

