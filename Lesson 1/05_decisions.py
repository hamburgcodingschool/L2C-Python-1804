print("What is the first number?")
value1 = input()
number1 = int(value1)
print("What is the second number?")
number2 = int(input())

if number1 == number2:
    print("THEY ARE THE SAME!!!!")
else:
    if number1 > number2:
        print("The biggest is " + str(number1))
    else:
        print("The biggest is " + str(number2))
