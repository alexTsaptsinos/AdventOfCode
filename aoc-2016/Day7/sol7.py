import re

f = open("input7.txt", "r")
text = f.readlines()
print(len(text))
variableDic = {}

while len(text) > 0:
    print(len(text))
    for line in text[:]:
        inputs = line.split()

        if len(inputs) == 3:
            # initialising input
            variable = inputs[2]
            try:
                num = int(inputs[0])
                variableDic[variable] = num
                text.remove(line)
            except ValueError:
                try:
                    existVar = variableDic[inputs[0]]
                    variableDic[variable] = existVar
                    text.remove(line)
                except KeyError:
                    pass
        elif len(inputs) == 4:
            # not assignment
            assignedVar = inputs[3]
            existVar = inputs[1]
            try:
                existVal = variableDic[existVar]
                newVal = 65536 + ~existVal
                variableDic[assignedVar] = newVal
                text.remove(line)
            except KeyError:
                pass
        elif len(inputs) == 5:
            # one of the other assignments
            assignedVar = inputs[4]
            existVar1 = inputs[0]
            if inputs[1] == "AND":
                existVar2 = inputs[2]
                try:
                    existVar1 = int(existVar1)
                    try:
                        newVal = existVar1 & variableDic[existVar2]
                        variableDic[assignedVar] = newVal
                        text.remove(line)
                    except KeyError:
                        pass
                except ValueError:
                    try:
                        newVal = variableDic[existVar1] & variableDic[existVar2]
                        variableDic[assignedVar] = newVal
                        text.remove(line)
                    except KeyError:
                        pass

            elif inputs[1] == "OR":
                existVar2 = inputs[2]
                try:
                    newVal = variableDic[existVar1] | variableDic[existVar2]
                    variableDic[assignedVar] = newVal
                    text.remove(line)
                except KeyError:
                    pass
            elif inputs[1] == "LSHIFT":
                try:
                    newVal = variableDic[existVar1] << int(inputs[2])
                    variableDic[assignedVar] = newVal
                    text.remove(line)
                except KeyError:
                    pass
            elif inputs[1] == "RSHIFT":
                try:
                    newVal = variableDic[existVar1] >> int(inputs[2])
                    variableDic[assignedVar] = newVal
                    text.remove(line)
                except KeyError:
                    pass
        else:
            print("got here")

    try:
        print("a value:", variableDic["a"])
        break
    except KeyError:
        pass

# Adding code for part b
aValue = variableDic["a"]
f = open("input7.txt", "r")
text = f.readlines()
variableDic = {}
variableDic["b"] = aValue

while len(text) > 0:
    print(len(text))
    for line in text[:]:
        variableDic["b"] = aValue
        inputs = line.split()

        if len(inputs) == 3:
            # initialising input
            variable = inputs[2]
            try:
                num = int(inputs[0])
                variableDic[variable] = num
                text.remove(line)
            except ValueError:
                try:
                    existVar = variableDic[inputs[0]]
                    variableDic[variable] = existVar
                    text.remove(line)
                except KeyError:
                    pass
        elif len(inputs) == 4:
            # not assignment
            assignedVar = inputs[3]
            existVar = inputs[1]
            try:
                existVal = variableDic[existVar]
                newVal = 65536 + ~existVal
                variableDic[assignedVar] = newVal
                text.remove(line)
            except KeyError:
                pass
        elif len(inputs) == 5:
            # one of the other assignments
            assignedVar = inputs[4]
            existVar1 = inputs[0]
            if inputs[1] == "AND":
                existVar2 = inputs[2]
                try:
                    existVar1 = int(existVar1)
                    try:
                        newVal = existVar1 & variableDic[existVar2]
                        variableDic[assignedVar] = newVal
                        text.remove(line)
                    except KeyError:
                        pass
                except ValueError:
                    try:
                        newVal = variableDic[existVar1] & variableDic[existVar2]
                        variableDic[assignedVar] = newVal
                        text.remove(line)
                    except KeyError:
                        pass

            elif inputs[1] == "OR":
                existVar2 = inputs[2]
                try:
                    newVal = variableDic[existVar1] | variableDic[existVar2]
                    variableDic[assignedVar] = newVal
                    text.remove(line)
                except KeyError:
                    pass
            elif inputs[1] == "LSHIFT":
                try:
                    newVal = variableDic[existVar1] << int(inputs[2])
                    variableDic[assignedVar] = newVal
                    text.remove(line)
                except KeyError:
                    pass
            elif inputs[1] == "RSHIFT":
                try:
                    newVal = variableDic[existVar1] >> int(inputs[2])
                    variableDic[assignedVar] = newVal
                    text.remove(line)
                except KeyError:
                    pass
        else:
            print("got here")

    try:
        print("final a value:", variableDic["a"])
        break
    except KeyError:
        pass