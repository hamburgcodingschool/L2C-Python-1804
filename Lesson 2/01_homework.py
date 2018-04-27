# VARIABLES CAN BE int, float, str, bool

print('What is the first number?')
num1 = int(input())
print('What is the second number?')
num2 = int(input())
print('What is the third number?')
num3 = int(input())

# if num1 > num2:
#     if num1 > num3:
#         print(num1)
#     else:
#         print(num3)
# else:
#     if num2 > num3:
#         print(num2)
#     else:
#         print(num3)

if num1 > num2:
    biggest = num1
else:
    biggest = num2

if num3 > biggest:
    biggest = num3

print(biggest)