## Advent of Code 2022
## Day 1 Part 1
import aoc_core as aoc
f = aoc.fe

elf = 0
bigelf = 0

for x in f[0:]:
    if (x != ""):
        elf = int(x) + elf
    else:
        if (elf > bigelf):
            bigelf = elf
        print(elf)
        elf = 0

print("The highest calorie count is: " + str(bigelf))