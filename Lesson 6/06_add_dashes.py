word = "banana" # ask user for word instead

wordDash = ""

for i in range(0, len(word)):
    letter = word[i]

    if i > 0:
        wordDash += " - "
    wordDash += letter # wordDash = wordDash + letter


print(wordDash)
