def Alphabetiser(str):
    '''
    Testing version control with Anaconda Spyder3
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # Actually not necessary. Char can be directly compared to return
    # a Boolean value for use in if-clauses

    n = 0
    AB = ''

    for char in str:
        if (n + 1) == len(str):
            return
        # Only works at the end to avoid IndexError
        # Might be redundant with updated comparison code

        elif alphabet.index(str[n]) < alphabet.index(str[n + 1]):
            if AB == '':
                AB += str[n]
            AB += str[n + 1]
        # Comparing one char against next char

        elif alphabet.index(str[n]) > alphabet.index(str[n + 1]) \
                and AB != '':
            print("Longest substring in alphabetical order is: ", end='')
            return AB
        # Truncates output string, otherwise it keeps adding
        # in a non-AB manner

        n += 1
