from ast import For, If
from cgi import print_arguments
from os import lstat
from pickle import FALSE, TRUE
import sys
from locale import atoi
from typing import final

inputFile = sys.argv[1]
input = open(inputFile, 'r')
lines = input.readlines()
nums = lines[0].split(',')

currentNums = []
finalNum = 0


for i in nums:
    currentNums.append(i.strip())

    boardNum = 0
    unmarkedSum = 0
    flag = False
    
    for j in range(2,len(lines)):
        scoreX = 0
        scoreY = {}
        

        if(lines[j]=="\n"):
            if(flag):
                break
            scoreX = 0
            scoreY = {}
            unmarkedSum = 0

        else:
            rowNums = lines[j].split(' ')
            rowNums = list(filter(lambda e: e != "",rowNums))

            for k in range(0,5):
                num = rowNums[k].strip()
                if(num in currentNums):
                    scoreX += 1 

                else:
                    unmarkedSum += atoi(num)
            
            if (scoreX == 5):
                flag = True
                print(str(j%6)+" "+i)
                finalNum = atoi(i)
    if(flag):
            break

# unmarkedSum = 0
# unmarkedNums = list(filter(lambda e: e not in currentNums, nums))
# for i,item in enumerate(unmarkedNums):
#     unmarkedNums[i] = item.strip()
#     unmarkedSum += atoi(item.strip())

print(finalNum)
print(unmarkedSum)