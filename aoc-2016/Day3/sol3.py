f = open("input3.txt","r")
text = f.read()
no_houses = 1
x_pos = 0
y_pos = 0
visited_houses = [(0,0)]

for move in text:
    if move == ">":
        x_pos += 1
    elif move == "<":
        x_pos -= 1
    elif move == "^":
        y_pos += 1
    else:
        y_pos -= 1

    coord = (x_pos,y_pos)
    visited_houses.append(coord)

visited_houses = set(visited_houses)
no_houses = len(visited_houses)

print("Number of Visited Houses:",no_houses)

