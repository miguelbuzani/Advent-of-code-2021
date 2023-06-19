import math as Math
import sys
from locale import atoi
import time

start_time = time.time()

inputFile = sys.argv[1]
input = open(inputFile, 'r')
lines = input.readlines()

maxX1 = (max(
    lines,
    key=lambda x: x.split("->")[0].split(",")[0])).split("->")[0].split(",")[0]
maxX2 = (max(
    lines,
    key=lambda x: x.split("->")[1].split(",")[0])).split("->")[1].split(",")[0]
maxY1 = (max(
    lines,
    key=lambda x: x.split("->")[0].split(",")[1])).split("->")[0].split(",")[1]
maxY2 = (max(
    lines,
    key=lambda x: x.split("->")[1].split(",")[1])).split("->")[1].split(",")[1]

lstMax = [maxX1, maxX2, maxY1, maxY2]

maxDim = atoi(max(lstMax)) + 1

print(maxDim)

floorMap = [[0] * maxDim for _ in range(maxDim)]

i = 0
numOL = 0

for line in lines:

    # print(i)
    cords = line.split("->")

    cord1 = cords[0].strip()
    arrCord1 = cord1.split(",")
    cordX1 = arrCord1[0]
    cordY1 = arrCord1[1]

    cord2 = cords[1].strip()
    arrCord2 = cord2.split(",")
    cordX2 = arrCord2[0]
    cordY2 = arrCord2[1]

    if cordX1 == cordX2 or cordY1 == cordY2:
        # print("x1: %s y1: %s" % (cordX1, cordY1))

        if cordX1 == cordX2:
            print("x1: %s y1: %s" % (cordX1, cordY1))
            print("x2: %s y2: %s" % (cordX2, cordY2))

            if atoi(cordY1) > atoi(cordY2):
                for j in range(atoi(cordY2), atoi(cordY1) + 1):
                    floorMap[j][atoi(cordX1)] = floorMap[j][atoi(cordX1)] + 1
                    # floorMap[atoi(cordX1)][j] = floorMap[atoi(cordX1)][j] + 1
            else:
                for j in range(atoi(cordY1), atoi(cordY2) + 1):
                    floorMap[j][atoi(cordX1)] = floorMap[j][atoi(cordX1)] + 1

        elif cordY1 == cordY2:
            print("x1: %s y1: %s" % (cordX1, cordY1))
            print("x2: %s y2: %s" % (cordX2, cordY2))

            if atoi(cordX1) > atoi(cordX2):
                for j in range(atoi(cordX2), atoi(cordX1) + 1):
                    floorMap[atoi(cordY1)][j] = floorMap[atoi(cordY1)][j] + 1

                    # floorMap[atoi(cordX1)][j] = floorMap[atoi(cordX1)][j] + 1
            else:
                for j in range(atoi(cordX1), atoi(cordX2) + 1):
                    floorMap[atoi(cordY1)][j] = floorMap[atoi(cordY1)][j] + 1

            # slope = NULL

            # if ((atoi(cordX2) - atoi(cordX1)) != 0):
            #     slope = (atoi(cordY2) - atoi(cordY1)) / (atoi(cordX2) -
            #                                              atoi(cordX1))
            #     print((atoi(cordY2) - atoi(cordY1)) /
            #           (atoi(cordX2) - atoi(cordX1)))
            # else:
            #     slope = 0
            #     print(0)

            # print(slope**0)

        i += 1

for item in floorMap:
    for cell in item:
        if cell >= 2:
            numOL += 1
    print(item)

print(numOL)