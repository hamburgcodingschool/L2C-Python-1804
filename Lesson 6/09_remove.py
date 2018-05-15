names = ["Ragle", "Anna", "Tina", "Annie", "Marvin", "Helder"]

#remove all the names that have the letter 'a'

# maybe try first removing something from the array, the element
# at position 2 for instance
# always try to split a problem into smaller problems

counter = 0
while counter < len(names):
    name = names[counter]

    if "a" in name or "A" in name:
        names.remove(name)
    else:
        counter += 1

print(names)