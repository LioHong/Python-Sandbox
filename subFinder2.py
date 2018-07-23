def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    Recursive function
    I couldn't make this functional for all test cases. I'll leave this for another time.
    '''

    guess = len(aStr) // 2

    if len(aStr) == 1:
        return aStr == char

    if len(aStr) > 1:
        # This splits the string into two substrings, where the lesser-valued substring
        # is also sometimes shorter in length by 1.
        # Without guess+1, it would always be shorter.
        if char < aStr[guess]:
            aStr = aStr[:guess]
            isIn(char, aStr)

        elif char > aStr[guess]:
            aStr = aStr[guess:]
            isIn(char, aStr)

        elif char == aStr[guess]:
            return aStr[guess] == char
    # This was the final case that eluded me.

    # Interestingly any output here will be repeated for each recursion of
    # the function i.e. print
