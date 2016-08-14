import re

f = open("input19.txt","r")
lines = f.readlines()
molecule = lines[-1]
del lines[-1]
del lines[-1]
print(lines)
print(molecule)

list_words = []
list_molecules = []
molecule_dic = {}

#lines = ["Al => ThF"]
for line in lines:
    if line.strip()=="":
        break

    split_line = line.split()
    print(line.strip())
    m1 = split_line[0]
    m2 = split_line[2]


    molecule_dic[m2] = m1
    list_molecules.append(m2)

    searches = re.finditer(m1,molecule)
    for item in searches:
        location = item.span()
        startlocation = item.start()
        endlocation = item.end()
        new_word = molecule[:startlocation]+m2+molecule[endlocation:]
        list_words.append(new_word)


print(list_words)
print(len(list_words))

set_words = set(list_words)

print("Result:",len(set_words))

# PART B

print(list_molecules)
print(molecule_dic)

list_molecules.sort(key=len,reverse=True)
print(list_molecules)

no_steps_needed = 0

while len(molecule) > 1:
    for trans_mol in list_molecules:
        if trans_mol in molecule:
            no_matches = len(re.findall(trans_mol,molecule))
            molecule = re.sub(trans_mol,molecule_dic[trans_mol],molecule)
            no_steps_needed += no_matches
            break


print(molecule)
print("Min number of steps:",no_steps_needed)