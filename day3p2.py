from os import lstat
import sys


inputFile = sys.argv[1]

input = open(inputFile, 'r')

gamma = {}

oxyRate = {}
co2Rate = {}

vals = []

lines = input.readlines()

for e in range(0,len(lines[0].strip())):
    gamma[e] = [0,0]


for line in lines:
    for i in range(0,len(line.strip())):
        if(line[i] == '0'):
            gamma[i] = [gamma[i][0]+1,gamma[i][1]]
        else:
            gamma[i] = [gamma[i][0],gamma[i][1]+1]

gammaStr = ""
for i in range(0,len(gamma)):
    gammaStr += str(gamma[i].index(max(gamma[i])))

# print(gammaStr)

# print("-----")
# epsilonStr = ""
# for i in range(0,len(gamma)):
#     epsilonStr += str(gamma[i].index(min(gamma[i])))
# print(epsilonStr)

# print("-----")

# print(int(gammaStr,2)*int(epsilonStr,2))

def getOXY(lst,i):
    global oxyVal 

    freqs = [0,0]
    oxyLst = []
    co2Lst = []
    newStr = ""

    for line in lst:
        if(line[i] == '0'):
            freqs = [freqs[0]+1,freqs[1]]
        else:
            freqs = [freqs[0],freqs[1]+1]

    oxyNum = freqs.index(max(freqs))
    if (freqs[0] == freqs[1]):
        oxyNum = 1

    for line in lst:
        if(line[i] == str(oxyNum)):
            oxyLst.append(line)
        
    print("OXY: ",int(oxyLst[0],2))
    oxyVal = int(oxyLst[0],2)

    if(len(oxyLst) != 1):
        getOXY(oxyLst,i+1)
    else:
        pass
    #print(co2Lst)




def getCO2(lst,i):
    

    freqs = [0,0]
    oxyLst = []
    co2Lst = []
    newStr = ""

    for line in lst:
        if(line[i] == '0'):
            freqs = [freqs[0]+1,freqs[1]]
        else:
            freqs = [freqs[0],freqs[1]+1]

    co2Num = freqs.index(min(freqs))
    if (freqs[0] == freqs[1]):
        co2Num = 0

    for line in lst:
        if(line[i] == str(co2Num)):
            co2Lst.append(line)
        
    #print(co2Lst)
    #print(co2Num)
    print("C02: ",int(co2Lst[0],2))
    global co2Val 
    co2Val = int(co2Lst[0],2)

    if(len(co2Lst) != 1):
        getCO2(co2Lst,i+1)

    #print(co2Lst)



getOXY(lines,0)
getCO2(lines,0)

print(co2Val)
print(oxyVal)
print(co2Val*oxyVal)