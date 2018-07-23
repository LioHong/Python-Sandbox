def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    Infinite loop occurs here because there is a possibility that char is
    absent, unlike the secret number which requires only enough time to find
    the number.
    '''
    start = 0
    end = len(aStr)
    mid = int(len(aStr) / 2)
    guess = mid
    print(start)
    print(mid)
    print(end)
    print(guess)

    while char != aStr[guess]:
        if char < aStr[guess]:
            end = max(mid, guess)
            mid = (end - start) // 2
            guess = start + mid
            print('left')
            print(start)
            print(mid)
            print(end)
            print(guess)

        elif char > aStr[mid]:
            start = min(mid, guess)
            mid = (end - start) // 2
            guess = start + mid
            print('right')
            print(start)
            print(mid)
            print(end)
            print(guess)

        elif guess == 0:
            print('ZeroError')
            break

        else:
            break

    if char == aStr[guess]:
        return True

    elif len(aStr) == 1:
        return False
