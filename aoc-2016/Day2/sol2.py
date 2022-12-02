f = open("input2.txt", "r")
text = f.read()

total_area = 0
total_ribbon = 0

def surface_area(numbers):
    # input three numbers and will calculate surface area
    first_number = numbers[0]
    second_number = numbers[1]
    third_number = numbers[2]

    total = 2*first_number*second_number + 2*first_number*third_number + 2*second_number*third_number
    return total

lines = text.splitlines()

for line in lines:
    numbers = line.split(sep='x')
    numbers = sorted(numbers,key = int)
    numbers = [int(x) for x in numbers]
    temparea = surface_area(numbers)
    temparea = temparea + numbers[0]*numbers[1]

    tempribbon = 2*numbers[0] + 2*numbers[1] + numbers[0]*numbers[1]*numbers[2]

    total_area += temparea
    total_ribbon += tempribbon

print("Wrapping Paper:",total_area)
print("Ribbon:",total_ribbon)
