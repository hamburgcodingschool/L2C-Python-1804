def reverseWord(word):
    newWord = ""

    for pos in range(0, len(word)):
        mirrorPos = len(word) - 1 - pos
        mirrorLetter = word[mirrorPos]
        newWord = newWord + mirrorLetter

    return newWord

name = "helder"
r = reverseWord(name)
print(r)