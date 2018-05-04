number = 6 #ask the user for input instead

myRange = range(1, number + 1)

total = 0

outputStr = ""

for num in myRange:
    # calculate the total
    total = total + num

    #prepare the pretty string output
    outputStr = outputStr + str(num)
    if num < number:
        outputStr = outputStr + " + "

outputStr = outputStr + " = " + str(total)

print(outputStr)