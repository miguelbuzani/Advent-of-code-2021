import sys
from locale import atoi
import time

start_time = time.time()

inputFile = sys.argv[1]
input = open(inputFile, 'r')
lines = input.readlines()

fishes = lines[0].strip().split(",")
fishes = [int(x) for x in fishes]
fishCount = [0, 0, 0, 0, 0, 0, 0, 0, 0]

j = 0
for fish in fishes:
    if fish == 0:
        fishCount[5] += 1
        fishCount[8] += 1

    else:
        fishCount[fish] += 1

    j += 1

    # print(fishCount)

for i in range(1, 257):
    # print(fishCount)
    fishCountTemp = fishCount.copy()

    for x in range(0, 9):
        if x == 0:
            fishCount[6] += fishCountTemp[x]
            fishCount[8] += fishCountTemp[x]
            fishCount[x] -= fishCountTemp[x]
        else:
            fishCount[x - 1] += fishCountTemp[x]
            fishCount[x] -= fishCountTemp[x]

print("fishes: %d" % sum(fishCount))

# print("day: %d state: " % (1 + i), fishes)