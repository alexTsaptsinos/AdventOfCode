import regex as re
import json

f = open("input12.txt", "r")
text = f.read()

print(text)

numbers = re.findall(r'-?\d+', text)
print(numbers)
numbers = list(map(int, numbers))
sumNumbers = sum(numbers)
print("Sum of Numbers:", sumNumbers)

# Part b
redCheck = re.findall(r'\"red\"',text)

data = json.loads(text)
print(data)

redObjects = []

def stripLayer(d):
    # strips a dictionary layer
    arrays = []
    objects = []
    if "red" in d.values():
        # this object is red, add to delete list
        #print("found a red")
        redObjects.append(d)
    else:
        for key, value in d.items():
            #print(key,value)
            if type(value) == list:
                arrays.append(value)
            elif type(value) == dict:
                objects.append(value)

    return arrays, objects

def stripArrayLayer(ar):
    # strips an array layer
    arrays = []
    objects = []
    for item in ar:
        if type(item) == list:
            arrays.append(item)
        elif type(item) == dict:
            objects.append(item)

    return arrays, objects


newArrays, newObjects = stripLayer(data)
finished = False

while not finished:
    tempArrays = []
    tempArrays2 = []
    tempObjects = []
    tempObjects2 = []
    for ar in newArrays:
        arrays, objects = stripArrayLayer(ar)
        tempArrays.extend(arrays)
        tempObjects.extend(objects)
    for d in newObjects:
        arrays, objects = stripLayer(d)
        tempArrays.extend(arrays)
        tempObjects.extend(objects)


    newArrays = tempArrays + tempArrays2
    newObjects = tempObjects + tempObjects2
    if len(newArrays) == 0 and len(newObjects) == 0:
        finished = True


print("RED check:", len(redCheck))
print("Length is:",len(redObjects))
redTotal = 0
for dic in redObjects:
    dicString = json.dumps(dic)
    redTemp = re.findall(r'-?\d+', dicString)
    numbers = list(map(int,redTemp))
    redTotal += sum(numbers)

print(redTotal)
partbTotal = sumNumbers - redTotal
print("Part b total:",partbTotal)

