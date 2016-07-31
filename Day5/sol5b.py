import re
f = open("input5.txt","r")
text = f.readlines()

no_nice = 0
no_lines = len(text)

for line in text:
    text_len = len(line)
    halfgood = 0 # turn to 1 if first condition fine
    good = 0 # turn to 1 if good

    # test for same letter with other in the middle ie xyx
    for i in range(text_len-2):
        if line[i] == line[i+2]:
            halfgood = 1
            break

    if halfgood == 1:
        for i in range(text_len-1):
            subtextToMatch = line[i:i+2]
            for j in range(i+2,text_len-1):
                if line[j:j+2] == subtextToMatch:
                    good = 1
                    break

            if good == 1:
                break

    if good == 1:
        no_nice += 1

print('Number of nice lines:',no_nice)

# NICE QUICKER SOLN FROM REDDIT SOLUTION PAGE UTILISING COUNT FN

def day5_part1():
    text = 'INPUT'

    n = 0
    for s in text:
        if 'ab' in s or 'cd' in s or 'pq' in s or 'xy' in s:
            continue
        if (s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')) < 3:
            continue
        for i in range(0, len(s)-1):
            if s[i] == s[i+1]:
                n += 1
                break

    print(n)

def day5_part2():
    text = 'INPUT'

    n = 0
    for s in text:
        for i in range(0, len(s)-2):
            if s[i] == s[i+2]:
                break
        else:
            continue

        for i in range(0, len(s)-1):
            if s.count(s[i] + s[i+1]) > 1:
                n += 1
                break
        else:
            continue

    print(n)

# OR ANOTHER EVEN QUICKER ONE USING REGEX EVEN BETTER

import sys
import re

strings = [x.strip() for x in sys.stdin.readlines()]

# Part 1
print(len([s for s in strings if (re.search(r'([aeiou].*){3,}', s) and
                                  re.search(r'(.)\1', s) and
                                  not re.search(r'ab|cd|pq|xy', s))]))

# Part 2
print(len([s for s in strings if (re.search(r'(..).*\1', s) and
                                  re.search(r'(.).\1', s))]))