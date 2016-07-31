f = open("input3.txt","r")
text = f.read()

# split into instructions for santa and for robo-santa
santa_instructions = text[::2]
robo_instructions = text[1::2]

# get list of all houses santa visits
x_pos = 0
y_pos = 0
santa_houses = [(0,0)]
for move in santa_instructions:
    if move == ">":
        x_pos += 1
    elif move == "<":
        x_pos -= 1
    elif move == "^":
        y_pos += 1
    else:
        y_pos -= 1
    coord = (x_pos,y_pos)
    santa_houses.append(coord)

# add on list of all houses robo-santa visits
x_pos = 0
y_pos = 0
for move in robo_instructions:
    if move == ">":
        x_pos += 1
    elif move == "<":
        x_pos -= 1
    elif move == "^":
        y_pos += 1
    else:
        y_pos -= 1
    coord = (x_pos,y_pos)
    santa_houses.append(coord)

santa_houses = set(santa_houses)
no_houses = len(santa_houses)
print("Number of Visited Houses with Robo-Santa:",no_houses)

