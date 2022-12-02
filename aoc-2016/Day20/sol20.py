import math
input_number = 34000000

# want min integer such that
# sum of factors X 10 > 34000000

target_total = input_number/11

def factors(n):
    return set(
        factor for i in range(1, int(n**0.5) + 1) if n % i == 0
        for factor in (i, n//i)
    )

def factors_partb(n):
    first_run = set(
        factor for i in range(1, int(n ** 0.5) + 1) if n % i == 0
        for factor in (i, n // i)
    )
    second_run = set(elem for elem in first_run if n // elem <= 50)
    return second_run



found = False
j = 1

while not found:
    list_of_factors = list(factors_partb(j))
    sum_of_list = sum(list_of_factors)
    #print(sum_of_list)
    if sum_of_list >= target_total:
        found = True
    else:
        j += 1

print("Lowest house number:", j)