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
numboards = 0
print((len(lines) - 1))

for i in nums:
    currentNums.append(i.strip())

    boardNum = 0
    unmarkedSum = 0
    flag = False
    boardY = []
    numboards = 0

    for j in range(2, len(lines)):
        scoreX = 0
        scoreY = {}
        #print(lines[j])

        if (lines[j] == "\n"):

            if (flag):

                break
            scoreX = 0
            scoreY = {}
            unmarkedSum = 0
            #print(boardY)
            boardY = []
            #print(lines[j])
            numboards += 1

        else:
            rowNums = lines[j].split(' ')
            rowNums = list(filter(lambda e: e != "", rowNums))

            for k in range(0, 5):
                num = rowNums[k].strip()
                if (num in currentNums):
                    scoreX += 1
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
                    if totals[ii] == 5:
                        flag = True
                        finalNum = atoi(i)
                        tempJ = j
                        print("Board: %s" % (numboards / 6))
                        print(i)
                # print(totals)

                boardY.append(totals)

            #print(boardY)

            if (scoreX == 5):
                flag = True
                #winnerNums.append(finalNum)
                #print(i)
                finalNum = atoi(i)
                tempJ = j
                print("Board: %s" % (numboards / 6))
                print(i)

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
