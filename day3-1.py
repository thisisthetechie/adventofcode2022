## Advent of Code 2022
## Day 3 Part 1
import aoc_core as aoc
import re

f = aoc.fd
totalscore = 0

for x in f[0:]:

    for a in str(x[:int(len(x)/2)]):
        #print(a)
        c = re.findall(a,x[int(len(x)/2):])
        if (len(c) > 0):
            if (re.search(r"[a-z]",c[0])):
                totalscore += (ord(c[0]) - 96)
            else:
                totalscore += (ord(c[0]) - 38)
            break

print("The total score is: " + str(totalscore))