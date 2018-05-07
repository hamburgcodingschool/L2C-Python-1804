def isPalindrome(word):

    for pos in range(0, int(len(word) * 0.5)):
        mirrorPos = len(word) - 1 - pos

        if (word[pos] != word[mirrorPos]):
            return False

    return True

print(isPalindrome("something"))
print(isPalindrome("anna"))


