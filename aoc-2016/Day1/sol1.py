f = open("input1.txt","r")

text = f.read()
floor = 0
character = 1
endcharacter = 0
for bracket in text:
    if bracket == "(":
        floor += 1
    elif bracket == ")":
        floor -= 1
    if floor == -1 and endcharacter == 0:
        endcharacter = character
    else:
        character += 1

print (floor)
print (endcharacter)