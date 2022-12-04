## Advent of Code 2022
## Day 4 Part 2 improved
import aoc_core as aoc

f = aoc.fd
totalcount = 0
counttotal = 0

for x in f:
    a = x.split(",")
    set1 = set(range(int(a[0].split("-")[0]),int(a[0].split("-")[1])+1))
    set2 = set(range(int(a[1].split("-")[0]),int(a[1].split("-")[1])+1))

    if set1.issubset(set2) | set2.issubset(set1):
        totalcount += 1

    if set1.intersection(set2):
        counttotal += 1

print("The First total count is: " + str(totalcount))
print("The Second total count is: " + str(counttotal))
