numbers = [12, 4, 9, 10, 7]

total = 0
for num in numbers:
    total = total + num

print("total: {}".format(total))

avg = total / len(numbers)
print("average: {}".format(avg))
