names = ["Helder", "Ragle", "Anna", "Tina", "Anni", "Marvin"]

# counter = 0
# for name in names:
#     if counter % 2 != 0:
#         print("{}: {}".format(counter, name))
#     counter = counter + 1

for i in range(0, len(names)):
    if i % 2 != 0:
        print("{}: {}".format(i, names[i]))