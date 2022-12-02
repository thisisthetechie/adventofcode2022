## Advent of Code 2022
## Day 2 Part 1
import aoc_core as aoc
f = aoc.fd

score = {
    "A": {"X": 3, "Y": 6, "Z": 0},
    "B": {"X": 0, "Y": 3, "Z": 6},
    "C": {"X": 6, "Y": 0, "Z": 3}
}

bonus = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

totalscore = 0
for x in f[0:]:
    gamescore = score[x.split(" ")[0]][x.split(" ")[1]] + bonus[x.split(" ")[1]]
    
    print(x.split(" ")[0] + " - " + x.split(" ")[1] + " = " + str(gamescore))
    totalscore += gamescore

print("The total score is: " + str(totalscore))