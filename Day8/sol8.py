import re
f = open("input8.txt","r")
text = f.readlines()

totalCodeCharacters = 0
totalStringCharacters = 0
totalCodeExtendedCharacters = 0

for line in text:
    line = re.sub("\n","",line)
    codeLength = len(line)
    totalCodeCharacters += codeLength

    decoded = eval(line)
    stringLength = len(decoded)
    totalStringCharacters += stringLength

    encoded = repr(line)
    encoded = re.sub("\"","\\\"",encoded)
    encodedLength = len(encoded)
    totalCodeExtendedCharacters += encodedLength

diff = totalCodeCharacters - totalStringCharacters
diff2 = totalCodeExtendedCharacters - totalCodeCharacters

print("Difference:",diff)
print("Difference part b:",diff2)


