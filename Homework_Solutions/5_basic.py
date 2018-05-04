year = 2104 #ask the user for input instead

isLeap = False

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            isLeap = True
        else:
            isLeap = False
    else:
        isLeap = True
else:
    isLeap = False

if isLeap:
    print("YAY it's a leap year!!!")
else:
    print(":( it is not a leap year...")