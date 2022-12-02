import re
f = open("input5.txt","r")
text = f.readlines()

no_nice = 0
no_lines = len(text)
letters = ['ab','cd','pq','xy']
doubles = ['aa','bb','cc','dd','ee','ff','gg','hh','ii','jj','kk','ll','mm','nn','oo','pp','qq','rr','ss','tt','uu','vv','ww','xx','yy','zz']
vowels = ['a','e','i','o','u']

for i in range(no_lines):
    line = text[i]
    bad = 0

    # first search for letters
    for letter in letters:
        if letter in line:
            bad = 1
            break

    if bad == 0:
        # has passed letters test, check for doubles
        for double in doubles:
            if double in line:
                break
            else:
                if double == 'zz':
                    bad = 1

    # now check for 3 vowels if not already bad
    if bad == 0:
        no_vowels = 0
        for vowel in vowels:
            searchVowel = re.findall(vowel,line)
            tempLen = len(searchVowel)
            no_vowels = no_vowels + tempLen

        if no_vowels < 3:
            bad = 1

    if bad == 0:
        no_nice += 1

print('Number of nice lines:',no_nice)


