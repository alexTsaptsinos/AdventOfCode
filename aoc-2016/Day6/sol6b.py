import re,numpy
f = open("input6.txt","r")
text = f.readlines()
no_lines = len(text)
print(no_lines)

matrix = numpy.zeros((1000,1000),dtype=int)

for line in text:
    line = line.split(',')
    line = [item.split() for item in line]
    line = [item for sublist in line for item in sublist]
    #print(line)
    numbers = [int(s) for s in line if s.isdigit()]
    #print(numbers)
    if line[0] == "toggle":
        matrix[numbers[0]:numbers[2] + 1, numbers[1]:numbers[3] + 1] = matrix[numbers[0]:numbers[2] + 1,numbers[1]:numbers[3]+1]+2
    elif line[1] == "on":
        matrix[numbers[0]:numbers[2]+1,numbers[1]:numbers[3]+1] = matrix[numbers[0]:numbers[2]+1,numbers[1]:numbers[3]+1]+1
    elif line[1] == "off":
        for i in range(numbers[0],numbers[2]+1):
            for j in range(numbers[1],numbers[3]+1):
                matrix[i:i+1,j:j+1] = max(matrix[i:i+1,j:j+1]-1,0)

# Now count number of 1s
total = numpy.sum(matrix)
print("Number of lights on:",total)
