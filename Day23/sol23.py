import re
f = open("input23.txt","r")
lines = f.readlines()
print(len(lines))

index = 0
finished = False
dicValue = {}
dicValue['a'] = 0
#part b
dicValue['a'] = 1
dicValue['b'] = 0

while not finished:
    #print("a val:",dicValue['a'])
    #print(index)
    line = lines[index].strip()
    #print(line)
    split_line = line.split()
    instruction = split_line[0].strip()
    variable = re.sub(",","",split_line[1]).strip()
    if instruction == "inc":
        dicValue[variable] += 1
        index += 1
    elif instruction == "hlf":
        dicValue[variable] = int(dicValue[variable]/2)
        index += 1
    elif instruction == "tpl":
        dicValue[variable] = dicValue[variable]*3
        index += 1
    elif instruction == "jmp":
        if "+" in variable:
            index += int(re.sub("\+","",variable))
        else:
            index -= int(re.sub("\-","",variable))
    elif instruction == "jio":
        if dicValue[variable] == 1:
            if "+" in split_line[2]:
                index += int(re.sub("\+", "", split_line[2]))
            else:
                index -= int(re.sub("\-", "", split_line[2]))
        else:
            index += 1
    elif instruction == "jie":
        if dicValue[variable] % 2 == 0:
            if "+" in split_line[2]:
                index += int(re.sub("\+", "", split_line[2]))
            else:
                index -= int(re.sub("\-", "", split_line[2]))
        else:
            index += 1
    else:
        # Got weird instruction
        print("WEIRD")
        finished = True

    if index >= len(lines):
        finished = True

print("a value:",dicValue['a'])
print("b value:",dicValue['b'])



