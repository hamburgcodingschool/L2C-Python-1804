userNumber = 43 #ask the user for input instead
numbers = [12, 45, 2, 5, 10, 9, 42]

# itExists = False
#
# for number in numbers:
#     if number == userNumber:
#         itExists = True
#         break
#
# if itExists:
#     print("YAY IT EXISTS")
# else:
#     print("aaawwwww....")

if userNumber in numbers:
    print("YAY IT EXISTS")
else:
    print("aaawwwww....")