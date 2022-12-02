import re
f = open("input15.txt","r")
lines = f.readlines()
dictionary = {}

for line in lines:
    splitLine = line.split()
    name = splitLine[0]
    name = name[:-1]
    dictionary[name] = {}
    for i in range(int(len(splitLine)/2)):
        tempLabel = splitLine[2*i+1]
        tempValue = splitLine[2*(i+1)]
        tempValue = re.sub("\,","",tempValue)
        tempValue = int(tempValue)
        dictionary[name][tempLabel] = tempValue

print(dictionary)

# Going to apply brute force check on each. However we can minimalise the amount of loops by simply eyeballing some checks
# Sugar can have a maxm of 40g o/w texture will always be negative
sugar_max = 40
# Sprinkles can have a max of 50g
sprinkles_max = 50
# Candy can have a maxm of 75g
candy_max = 75
# Choc can have a maxm of 66g
choc_max = 67

best_total = 0
best_calories_total = 0
sugar = dictionary['Sugar']
sprinkles = dictionary['Sprinkles']
candy = dictionary['Candy']
choc = dictionary['Chocolate']

for i in range(sugar_max):
    for j in range(max(101-i,sprinkles_max)):
        for k in range(max(101-i-j,choc_max)):
            # i = sugar amount
            # j = sprinkles amount
            # k = choc amount
            l = 100 - i - j - k # candy amount
            if l > 75:
                continue

            product = 1
            for key in sugar:
                if key != "calories":
                    new_product = i*sugar[key] + j*sprinkles[key] + k*choc[key] + l*candy[key]
                    new_product = max(new_product,0)
                    product = product*new_product
                else:
                    calories_total = i*sugar[key] + j*sprinkles[key] + k*choc[key] + l*candy[key]

            if calories_total == 500:
                best_calories_total = max(product,best_calories_total)

            best_total = max(product,best_total)

print("Best Total:",best_total)
print("Best Calories Total:",best_calories_total)

