number = 17 #ask the user for input instead

myRange = range(1, number + 1)

total = 0

outputStr = ""

for num in myRange:
    if num % 3 == 0 or num % 5 == 0:
        # calculate the total
        total = total + num

        #prepare the pretty string output
        if num > 3:
            outputStr = outputStr + " + "

        outputStr = outputStr + str(num)


outputStr = outputStr + " = " + str(total)

print(outputStr)