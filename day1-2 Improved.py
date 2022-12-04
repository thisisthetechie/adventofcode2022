## Advent of Code 2022
## Day 1 Part 1
import aoc_core as aoc
import numpy, math
f = aoc.fd
f = list(filter(None, f))
a = numpy.array(f, dtype='int32')
ind = numpy.argpartition(a, -3)[-3:]

print("Highest Calories = " + str(a.max()))
print("Top 3 Calories combined = " + str(sum(a[ind])))