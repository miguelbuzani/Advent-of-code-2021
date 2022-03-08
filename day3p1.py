import sys


inputFile = sys.argv[1]

input = open(inputFile, 'r')

gamma = {}
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

print(gammaStr)

print("-----")
epsilonStr = ""
for i in range(0,len(gamma)):
    epsilonStr += str(gamma[i].index(min(gamma[i])))
print(epsilonStr)

print("-----")

print(int(gammaStr,2)*int(epsilonStr,2))
