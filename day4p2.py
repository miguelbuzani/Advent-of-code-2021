import math as Math
import sys
from locale import atoi
import time

start_time = time.time()

inputFile = sys.argv[1]
input = open(inputFile, 'r')
lines = input.readlines()
nums = lines[0].split(',')

currentNums = []
finalNum = 0

winnerNums = []
winnerBoards = []
winnerRows = []
winnerCols = [[0] * 5] * len(lines)
# print(winnerCols)
# numboards = 0
numBoards = (len(lines) - 1) / 6
# print(nums)

for i in nums:
    currentNums.append(i.strip())

    if (len(winnerBoards) == numBoards):
        break

    boardNum = 0
    unmarkedSum = 0
    flag = False
    boardY = []
    # numboards = 0

    for j in range(2, len(lines)):

        scoreX = 0
        scoreY = {}
        #print(lines[j])

        if (lines[j] == "\n"):

            # if (flag):

            #     break
            scoreX = 0
            scoreY = {}
            unmarkedSum = 0
            #print(boardY)
            boardY = []
            #print(lines[j])
            # numboards += 1

        else:
            rowNums = lines[j].split(' ')
            rowNums = list(filter(lambda e: e != "", rowNums))

            for k in range(0, 5):
                num = rowNums[k].strip()
                if (num in currentNums):
                    scoreX += 1
                    if (scoreX == 5):
                        if (j not in winnerRows):
                            flag = True
                            #winnerNums.append(finalNum)
                            winnerRows.append(j)
                            finalNum = atoi(i)
                            tempJ = j
                            temp2J = j - 2
                            # print("Board: %s" % (numboards / 6))
                            # print(j)
                            asdf = ((temp2J) / 18)
                            # print((int)(asdf * numBoards))
                            if (((int)(asdf * numBoards)) not in winnerBoards):
                                winnerBoards.append((int)(asdf * numBoards))

                            # print(i, j, (int)(asdf * numBoards), currentNums)
                            # print([(int)(asdf * numBoards), i, j + 1])
                            # print(asdf)
                            # print((((j) / 18) * numBoards).toString("#"))
                            # print("Winner: %s" % i)
                    # print(scoreY, j, k)

                    scoreY[k] = 1

                else:
                    unmarkedSum += atoi(num)
                    scoreY[k] = 0

            boardY.append(scoreY)

            if len(boardY) == 5:
                totals = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
                for row in boardY:
                    if row[0] == 1:
                        totals[0] += 1
                    if row[1] == 1:
                        totals[1] += 1
                    if row[2] == 1:
                        totals[2] += 1
                    if row[3] == 1:
                        totals[3] += 1
                    if row[4] == 1:
                        totals[4] += 1

                for ii in range(0, 5):
                    # print(totals[i])
                    # print(j, ii)

                    if totals[ii] == 5:
                        if (winnerCols[j][ii] == 0):
                            # print(totals)
                            flag = True
                            finalNum = atoi(i)
                            tempJ = j
                            temp2J = j - 2
                            # print("Board: %s" % (numboards / 6))
                            # print(j)
                            asdf = ((temp2J) / 18)
                            winnerCols[j][ii] = 1
                            # winnerBoards.append([(int)(asdf * numBoards), i])
                            # winnerBoards.append((int)(asdf * numBoards))

                            if (((int)(asdf * numBoards)) not in winnerBoards):
                                winnerBoards.append((int)(asdf * numBoards))

                            # print(i, j, ii, (int)(asdf * numBoards),
                            #       currentNums)
                            # print("Board: %s" % (numboards / 6))
                            # print(i)
                    else:
                        winnerCols[j][ii] = 0

                boardY.append(totals)
            # print(totals)

            #print(boardY)

    # if (flag):
    #     break

# unmarkedSum = 0
# unmarkedNums = list(filter(lambda e: e not in currentNums, nums))
# for i,item in enumerate(unmarkedNums):
#     unmarkedNums[i] = item.strip()
#     unmarkedSum += atoi(item.strip())
print("--- %s seconds ---" % (time.time() - start_time))
print(finalNum * unmarkedSum)
print(finalNum)
print(unmarkedSum)
print(winnerNums)
print(winnerBoards[len(winnerBoards) - 1])
print(winnerBoards)
print(numBoards)
