import itertools,numpy,math
f = open("input17.txt","r")
lines = f.readlines()

container_sizes = [int(line) for line in lines]

combs = itertools.permutations(container_sizes,len(container_sizes))
no_containers = len(container_sizes)
no_combinations = 0

q2 = 0

for i in range(no_containers-1):
    for perm in itertools.combinations(container_sizes,i):
        if sum(perm) == 150:
            no_combinations+=1
    if no_combinations and not q2:
        q2 = no_combinations

print("Result:",no_combinations)
print("Result 2:",q2)