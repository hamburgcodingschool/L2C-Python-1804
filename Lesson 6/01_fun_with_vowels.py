def isVowel(letter):
    return letter in "aeiouAEIOU"
    # if letter in "aeiouAEIOU":
    #     return True
    # else:
    #     return False

def vowelCounter(word):
    counter = 0
    for letter in word:
        if isVowel(letter):
            counter += 1

    return counter

print(vowelCounter("Pokemon"))