import itertools
inputString = "3113322113"

no_times = 50



'''for j in range(no_times):
    in_a_row = 1
    numbersString = ""

    for i in range(len(inputString)):
        if i+1 < len(inputString):
            if inputString[i] == inputString[i+1]:
                in_a_row += 1
                continue
            else:
                numbersString = numbersString + str(in_a_row) + str(inputString[i])
                in_a_row = 1
        else:
            numbersString = numbersString + str(in_a_row) + str(inputString[i])
            in_a_row = 1

    #print(numbersString)
    print(j+1,"is:",len(numbersString))
    inputString = numbersString

print("Final Length:", len(inputString))'''

# Works for first part but is too time consuming for second. Used reddit solns:

def look_and_say2(input):
    return ''.join(str(len([1 for _ in v])) + k for k, v in itertools.groupby(input))

for _ in range(50):
    inputString = look_and_say2(inputString)
print(len(inputString))