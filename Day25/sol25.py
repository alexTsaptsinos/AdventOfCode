
multiplier = 252533
divider = 33554393

def next_code(cur_code):
    return (cur_code * multiplier) % divider

def get_code_count(row, column):
    return sum(range(row + column - 1)) + column

first_code = 20151125
code_coords = (2981, 3075)

code_count = get_code_count(*code_coords)
cur_code = first_code
for i in range(code_count - 1):
    cur_code = next_code(cur_code)
print(cur_code)