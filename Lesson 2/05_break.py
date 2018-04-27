secretCode = 'password1'

triesLeft = 2
accessAllowed = True

print("What's the password?")
userCode = input()

# while userCode != secretCode:
#     if triesLeft <= 0:
#         accessAllowed = False
#         break
#
#     print("That's wrong. You have " + str(triesLeft) + " tries left.")
#     userCode = input()
#
#     triesLeft = triesLeft - 1

accessAllowed = False

while triesLeft > 0:



if accessAllowed:
    print("Welcome")
else:
    print("Sorry, you must contact your phone provider...")