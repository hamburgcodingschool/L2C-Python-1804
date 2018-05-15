import random

newMatrix = []

for i in range(0, 4):
    newLine = []
    for j in range(0, 4):
        randomNum = random.randint(1, 100)
        newLine.append(randomNum)
    newMatrix.append(newLine)

print(newMatrix)