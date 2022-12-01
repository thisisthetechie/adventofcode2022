## Advent of Code 2022
## Day 1 Part 1
import aoc_core as aoc
f = aoc.fd

elf = 0
elflist = [0]

for x in f[0:]:
    if (x != ""):
        print(x)
        elf = int(x) + elf
    else:
        elflist.append(elf)
        print(elf)
        elf = 0

elflist.sort(reverse = True)
bigelf = 0
for i in range(0,3):
    bigelf = bigelf + elflist[i]
print("The highest calorie count is: " + str(bigelf))