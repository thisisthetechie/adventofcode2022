## Advent of Code 2022
## Day 3 Part 2
import aoc_core as aoc
import re

f = aoc.fd
totalscore = 0

def chunk(l,n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

n = 3
my_arr = list(chunk(f,n))

for x in my_arr:
    print(x)
    for a in x[0]:
        c = re.findall(a, x[1])
        d = re.findall(a, x[2])
        if (len(c) > 0) & (len(d) > 0):
            if (c[0] == d[0]):
                if (re.search(r"[a-z]",c[0])):
                    totalscore += (ord(c[0]) - 96)
                    break
                else:
                    totalscore += (ord(c[0]) - 38)
                    break

print("The total score is: " + str(totalscore))
