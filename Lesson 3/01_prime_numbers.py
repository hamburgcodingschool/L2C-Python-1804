number = 8 # this will change to input later

test = 2
divCounter = 0

while test < number:

    if number % test == 0:
        print("{} is a divisor of {}".format(test, number))
        divCounter = divCounter + 1
    else:
        print("{} is NOT a divisor of {}".format(test, number))

    test = test + 1

print("-------------")

if divCounter == 0:
    print("{} is a prime number".format(number))
else:
    print("{} is NOT a prime number".format(number))