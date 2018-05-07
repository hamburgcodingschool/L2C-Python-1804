names = ["Helder", "Ragle", "Anna", "Tina", "Anni", "Marvin"]

highestLen = 0
counter = 0

for name in names:
    if len(name) > highestLen:
        highestLen = len(name)
        counter = 0

    if len(name) == highestLen:
        counter += 1 # counter = counter + 1


print(counter)

