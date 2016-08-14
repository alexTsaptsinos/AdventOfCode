import itertools,numpy
f = open("input24.txt","r")
lines = f.readlines()
no_lines = len(lines)
print(no_lines)

numbers = [int(item) for item in lines]
#print(numbers)
sum_numbers = sum(numbers)
#print(sum_numbers)

bag_weight = sum_numbers/4
print(bag_weight) # = 381
# So each bag needs to weigh 381
# Let's find the different ways we can sum to 508

good_combinations = []

# Good guess that passenger will have between 5-9 presents
for i in range(5,6):
    print(i)
    combs = itertools.combinations(numbers,i)
    for comb in combs:
        if sum(comb) == bag_weight:
            good_combinations.append(comb)

print(good_combinations)
print(len(good_combinations))

# A good guess that the passenger has 5 presents
found = False
i=0
while not found:
    comb = good_combinations[i]
    list_comb = list(comb)
    presents_left = [x for x in numbers if x not in list_comb]
    for i in range(5,9):
        combs2 = itertools.combinations(presents_left,i)
        for comb2 in combs2:
            if sum(comb2) == bag_weight:
                list_comb2 = list_comb + list(comb2)
                presents_left2 = [x for x in presents_left if x not in list_comb2]
                for j in range(5,10):
                    combs3 = itertools.combinations(presents_left2,j)
                    for comb3 in combs3:
                        if sum(comb3) == bag_weight:
                            found = True
                            min_product = numpy.product(comb)
                            break
                    if found:
                        break
                if found:
                    break

        if found:
            break
    i += 1


print("Min product:",min_product)
