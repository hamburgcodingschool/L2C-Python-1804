def sizeOfLongest(array):
    longest = 0
    for word in array:
        if len(word) > longest:
            longest = len(word)
    return longest


def printStars(number):
    starString = ""
    for i in range(0, number):
        starString += "*"
    print(starString)

# example: word = "a", longest = 9
def printWordWithStars(word, longest):
    remainingSpaces = longest - len(word)
    line = "* "
    line += word
    for i in range(0, remainingSpaces):
        line += " "
    line += " *"
    print(line)

def writeInFrame(sentence):
    # split string into array of strings separating by spaces
    words = sentence.split(" ")

    longest = sizeOfLongest(words)
    printStars(longest + 4)
    for word in words:
        printWordWithStars(word, longest)
    printStars(longest + 4)


print("Give me a sentence")
sentence = input()

writeInFrame(sentence)
