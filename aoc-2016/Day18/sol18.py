import re,numpy
#numpy.set_printoptions(threshold=numpy.inf)
f = open("input18.txt","r")
lines = f.readlines()

matrix = numpy.zeros((102,102),dtype=int)
i=1
for line in lines:
    text = re.sub(r"\.","0",line)
    text = re.sub(r"#","1",text)
    text = text.strip()
    split_numbers = [int(elem) for elem in text]
    matrix[i:i+1,1:101] = split_numbers
    i += 1

print(matrix)

def update_matrix(input_matrix):
    updated_matrix = numpy.copy(input_matrix)
    for i in range(1,101):
        for j in range(1,101):
            first_sum = sum(input_matrix[i-1:i+2,j-1:j+2])
            no_neighbours_on = sum(sum(input_matrix[i-1:i+2,j-1:j+2])) - input_matrix[i,j]
            light = input_matrix[i,j]
            if (light == 1) and (no_neighbours_on == 2 or no_neighbours_on == 3):
                # light stays on
                pass
            elif (light == 0) and (no_neighbours_on == 3):
                # light turns on
                updated_matrix[i,j] = 1
            else:
                updated_matrix[i,j] = 0

    # EDIT FOR PART B
    updated_matrix[1,1] = 1
    updated_matrix[1,100] = 1
    updated_matrix[100,1] = 1
    updated_matrix[100,100] = 1

    return updated_matrix

for k in range(100):
    matrix = update_matrix(matrix)

no_lights_on_at_end = sum(sum(matrix))
print("Result:",no_lights_on_at_end)
