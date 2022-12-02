import re,string

inputString = "hxbxxyzz"
alphabet = list(string.ascii_lowercase)
numbers = list(range(1,27))
alphabetDic = dict(zip(numbers,alphabet))
numberDic = dict(zip(alphabet,numbers))

def incrementPassword(oldString):
    # Will increment the password
    # First convert oldString to base26 number
    bases = [numberDic[x] for x in oldString]

    for i in range(len(bases)):
        idx = len(bases) - 1 - i
        bases[idx] += 1
        if bases[idx] <= 26:
            break
        else:
            bases[idx] = 1
    newString = "".join(alphabetDic[x] for x in bases)
    return newString


# Now find next valid password
found = False
#re.search(r'([aeiou].*){3,}', s)
while not found:
    # increment to next possible password
    inputString = incrementPassword(inputString)

    # now perform checks to see if a valid password
    # first check if i, o or l
    if not re.search(r'i|o|l',inputString) and \
            re.search(r'abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz',inputString) \
            and re.search(r'(.)\1.*(.)\2',inputString):
        found = True


print("Next password:",inputString)
