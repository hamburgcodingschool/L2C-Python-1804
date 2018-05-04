number = 4 #ask the user for input instead

print("Multiply (m) or Sum (s) ?")
choice = input()

if choice == "m":
    total = 1
if choice == "s":
    total = 0

for num in range(1, number + 1):
    if choice == "m":
        total = total * num
    if choice == "s":
        total = total + num

print(total)

#extra homework: make it prettier with a full string like the previous ones