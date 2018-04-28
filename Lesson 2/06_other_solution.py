secretCode = 'password1'

triesLeft = 3
accessAllowed = False

while triesLeft > 0:

    print("What's the password?")
    userCode = input()

    if userCode == secretCode:
        accessAllowed = True
        break

    triesLeft = triesLeft - 1

    if triesLeft != 0:
        print("That's wrong you have {} tries left".format(triesLeft))





if accessAllowed:
    print("Welcome")
else:
    print("Sorry, you must contact your phone provider...")