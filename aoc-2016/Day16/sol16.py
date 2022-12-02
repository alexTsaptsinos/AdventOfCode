import re
f = open("input16.txt","r")
lines = f.readlines()

mfcsam_output = {}
mfcsam_output['children'] = 3
mfcsam_output['cats'] = 7
mfcsam_output['samoyeds'] = 2
mfcsam_output['pomeranians'] = 3
mfcsam_output['akitas'] = 0
mfcsam_output['vizslas'] = 0
mfcsam_output['goldfish'] = 5
mfcsam_output['trees'] = 3
mfcsam_output['cars'] = 2
mfcsam_output['perfumes'] = 1

# Comment this out for part a
mfcsam_output = {}
mfcsam_output['children'] = [3]
mfcsam_output['cats'] = [8,9,10,11,12,13,14,15,16,17,18,19,20]
mfcsam_output['samoyeds'] = [2]
mfcsam_output['pomeranians'] = [0,1,2]
mfcsam_output['akitas'] = [0]
mfcsam_output['vizslas'] = [0]
mfcsam_output['goldfish'] = [0,1,2,3,4]
mfcsam_output['trees'] = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
mfcsam_output['cars'] = [2]
mfcsam_output['perfumes'] = [1]

for line in lines:
    split_line = line.split()
    sue_number = split_line[1]
    first_indicator = re.sub(":","",split_line[2])
    value = int(re.sub(",","",split_line[3]))
    if value in mfcsam_output[first_indicator]:
        # first matches, check second
        second_indicator = re.sub(":", "", split_line[4])
        value = int(re.sub(",", "", split_line[5]))
        if value in mfcsam_output[second_indicator]:
            # second matches, check third
            third_indicator = re.sub(":", "", split_line[6])
            value = int(split_line[7])
            if value in mfcsam_output[third_indicator]:
                # third matches, stop
                break

print("Aunt Sue Number:",sue_number)