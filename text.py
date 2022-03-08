from asyncio.windows_events import NULL
from queue import Empty


map = {}

i = 0
for e in range(0,5):
    map[i] = [0,0]
    i=+1


for i in range(0,10):
    for j in range(0,5):
        map[j] = [map[i][0]+1,map[i][1]+1]



print(map)