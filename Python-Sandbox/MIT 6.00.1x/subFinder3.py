def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    Recursive function
    Basically just copied the answer.
    But I did end up comparing aStr == char for the 3rd base case
    That was bad.
    '''

    # Base cases:
    guess = len(aStr) // 2

    if aStr == '':
        return False

    if len(aStr) == 1:
        return aStr == char

    if char == aStr[guess]:
        return aStr[guess] == char

    # Recursion section
    if char < aStr[guess]:
        return isIn(char, aStr[:guess])

    elif char > aStr[guess]:
        return isIn(char, aStr[guess + 1:])
