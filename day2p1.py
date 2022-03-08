import sys


horVal = 0
dephVal = 0

inputFile = sys.argv[1]

input = open(inputFile, 'r')

for lines in input:
    command = lines.split(' ')

    if command[0][0] == 'f':
        horVal += int(command[1])
    if command[0][0] == 'd':
        dephVal -= int(command[1])
    if command[0][0] == 'u':
        dephVal += int(command[1])

print(horVal*dephVal)
