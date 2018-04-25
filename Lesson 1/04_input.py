print("What is your name?")

name = input()

print("Hello " + name)

print("How old are you " + name + "?")

ageInput = input()  # ex: ageInput = "34"
age = int(ageInput)  # ex: age = 34

if age >= 18:
	print("Have a Beer!")
else:
	print("Have a Fritz!")




print ("What is your first name?")
firstName = input()

print ("What is your last name?")
lastName = input()

fullName = firstName + " " + lastName

print("Hello " + fullName + " how are you?")