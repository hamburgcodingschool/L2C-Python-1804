word = "abcdefedcb"

isPalindrome = True

for pos in range(0, len(word)):
    mirrorPos = len(word) - 1 - pos

    # print("{} :: {}".format(pos, mirrorPos))

    if (word[pos] != word[mirrorPos]):
        isPalindrome = False

print(isPalindrome)