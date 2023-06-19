import sys
from locale import atoi
import time

start_time = time.time()

inputFile = sys.argv[1]
input = open(inputFile, 'r')
lines = input.readlines()

fishes = lines[0].strip().split(",")
fishes = [int(x) for x in fishes]
newFishes = []

for i in range(0, 256):
    newFishes = []
    j = 0

    for fish in fishes:
        if fish == 0:
            fishes[j] = 6

            newFishes.append(8)
        else:
            fishes[j] = fish - 1

        fish = fish
        j += 1

    for newFish in newFishes:
        fishes.append(newFish)

    # print("day: %d state: " % (1 + i), fishes)
print("fishes: %d" % len(fishes))