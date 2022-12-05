## Advent of Code 2022
## Day 5 Part 2
import aoc_core as aoc
import numpy, re, math
from collections import defaultdict

f = aoc.fd

linebreak = f.index("")
dimension = len(re.sub(r'\s','',f[linebreak - 1]))
s = [''] * (dimension)

# Parse input containers
for x in reversed(f[:linebreak]):
    if re.findall('\[', x):
        for i in range(dimension):
            index = i * 4 + 1
            if index <= len(x):
                if x[index].isalpha(): 
                    s[i] += x[index]

for x in f[linebreak + 1:]:
    count   = int(x.split()[1])
    colfrom = int(x.split()[3]) - 1
    colto   = int(x.split()[5]) - 1

    s[colto] += s[colfrom][len(s[colfrom]) - count:]
    s[colfrom] = s[colfrom][:len(s[colfrom]) - count]

toprow = ""
for r in range(dimension):
    toprow += s[r][-1]

print("The top row consists of:",toprow )