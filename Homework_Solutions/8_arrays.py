names = ["Helder", "Ragle", "Anna", "Tina", "Anni", "Marvin"]

highestLen = 0
biggestName = ""
for name in names:
    if len(name) > highestLen:
        highestLen = len(name)
        biggestName = name

print(biggestName)

#homework:
# print how many words exist with the highest ammount of chars