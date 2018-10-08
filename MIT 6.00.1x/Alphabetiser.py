def Alphabetiser(str):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    n = 0
    AB = ''

    def ABiser_1(str):
        for char in str:
            if (n + 1) == len(str):
                return AB
            # Only works at the end to avoid IndexError

            elif alphabet.index(str[n]) < alphabet.index(str[n + 1]):
                if AB == '':
                    AB += str[n]
                AB += str[n + 1]
            # Comparing one char against next char

            n += 1
