## Advent of Code 2022
## Day 6 Part 1
import aoc_core as aoc
import re

f = aoc.fd
c = 4
regex = re.compile("^(?!.*(.).*\1)[a-z]+$")
for x in f:
    for i in range(c, len(x)):
        if re.search(r"^(?!.*(.).*\1)[a-z]+$",x[i-c:i]):
            print(i)
            break