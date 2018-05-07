def isPrime(number):

    for test in range(2, number):
        if number % test == 0:
            return False

    return True

# prime numbers between 1 and 100
#
# for i in range(1, 101):
#     if isPrime(i):
#         print(i)

# first 100 prime numbers
#

primesFound = 0
numberToCheck = 1

while primesFound < 100:
    if isPrime(numberToCheck):
        primesFound += 1
        print("{}: {}".format(primesFound, numberToCheck))
    numberToCheck += 1




name = "Samantha"

print(name[2])