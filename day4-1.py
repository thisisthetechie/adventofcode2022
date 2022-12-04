## Advent of Code 2022
## Day 4 Part 1
import aoc_core as aoc

f = aoc.fd
totalcount = 0

for x in f:
    a = x.split(",")
    lo1 = int(a[0].split("-")[0])
    hi1 = int(a[0].split("-")[1])
    lo2 = int(a[1].split("-")[0])
    hi2 = int(a[1].split("-")[1])
    if (((lo1 >= lo2) & (hi1 <= hi2)) | ((lo2 >= lo1) & (hi2 <= hi1))):
        totalcount += 1

print("The total count is: " + str(totalcount))
