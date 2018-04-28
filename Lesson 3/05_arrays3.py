numbers = [4, 12, 15, 7]

highest = numbers[0]
lowest = numbers[0]
for num in numbers:
    if num > highest:
        highest = num
    if num < lowest:
        lowest = num

print(highest)
print(lowest)