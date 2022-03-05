from locale import atoi
from queue import PriorityQueue
import sys
import time
start_time = time.time()

inputFile = sys.argv[1]

input = open(inputFile, 'r')
temp = 0
result = 0

for line in input:
    val = atoi(line)
    if(temp<val):
        result+=1
    temp = val

print("--- %s seconds ---" % (time.time() - start_time))
print(result)

    
