import re
f = open("input15.txt","r")
lines = f.readlines()
dictionary = {}

for line in lines:
    splitLine = line.split()
    name = splitLine[0]
    name = name[:-1]
    dictionary[name] = {}
    for i in range(int(len(splitLine)/2)):
        tempLabel = splitLine[2*i+1]
        tempValue = splitLine[2*(i+1)]
        tempValue = re.sub("\,","",tempValue)
        tempValue = int(tempValue)
        dictionary[name][tempLabel] = tempValue

print(dictionary)
