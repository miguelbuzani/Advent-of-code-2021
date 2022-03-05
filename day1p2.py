from locale import atoi
from queue import PriorityQueue
import sys
import time
start_time = time.time()

inputFile = sys.argv[1]

input = open(inputFile, 'r')
lines = input.readlines()
temp = 0
result = 0

i = 0
for i in range(0, len(lines)-2):
    val1 = atoi(lines[i])
    val2 = atoi(lines[i+1])
    val3 = atoi(lines[i+2])

    sumVals = val1+val2+val3
    if(sumVals > temp):
        result += 1

    temp = sumVals

print("--- %s seconds ---" % (time.time() - start_time))
print(result)

    
