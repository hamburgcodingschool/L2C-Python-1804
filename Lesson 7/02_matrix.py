matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)
print("---------")

# print the element in the center of this specific array

print(matrix[1][1])
print("---------")

for i in range(0, len(matrix)):
    print("START INNER LOOP")
    for j in range(0, len(matrix[i])):
        print("i: {}  j: {}".format(i, j))
        print(matrix[i][j])

# print(matrix[0][0])
# print(matrix[0][1])
# print(matrix[0][2])
# print(matrix[1][0])
# print(matrix[1][1])
# print(matrix[1][2])
# print(matrix[2][0])
# print(matrix[2][1])
# print(matrix[2][2])

print(".......")


for i in range(0, len(matrix)):
    newString = ""
    lineTotal = 0
    for j in range(0, len(matrix[i])):
        if j > 0:
            newString += " + "
        newString += str(matrix[i][j])

        lineTotal += matrix[i][j]

    print(newString + " = " + str(lineTotal))


# 1 + 2 + 3 = 6
# 4 + 5 + 6 = 15
# 7 + 8 + 9 = 24