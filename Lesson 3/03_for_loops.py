
names = ["Helder", "Ragle", "Anna", "Tina", "Anni", "Marvin"]

for name in names:
    print(name)

print("-------------")

numbers = [1, 2, 3, 105, 207, 11, 13, 17, 19, 23, 29, 31, 37, 41]

total = 0
for num in numbers:
    print(total)
    total = total + num

print("-------------")

print(total)
print(total / len(numbers))

numbers = [4, 12, 15, 7]

highest = numbers[0]
lowest = numbers[0]
for num in numbers:
    if num > highest:
        highest = num
    if num < lowest:
        lowest = num


print("-------------")

print(highest)
print(lowest)