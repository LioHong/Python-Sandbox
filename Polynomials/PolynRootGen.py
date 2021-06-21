def RootReader():
    print('This function produces a polynomial from roots ' + \
          'of the form (a*n-b).')
    factors = input('Enter your roots: ')
    countf = 0

    for h in range(len(factors)):
        if factors[h] == '(':
            countf += 1

    roots = [[0 for i in range(countf)] for i in range(2)]
    counta = 0
    countb = 0

    for i in range(len(factors)):
        if factors[i] == '(':
            if factors[i + 1] == 'n':
                roots[0][counta] = 1
                counta += 1



            else:
                countna = 1
                while factors[i + countna] != 'n':
                    countna += 1

                if factors[i + 1:i + 3] == '-n':
                    roots[0][counta] = -1
                    counta += 1

                else:
                    roots[0][counta] = float(factors[(i + 1):(i + countna)])
                    counta += 1

        if factors[i] == ')':
            if factors[i - 3:i - 1] == 'n+':
                roots[1][countb] = float(factors[i - 1])
                countb += 1

            elif factors[i - 3:i - 1] == 'n-':
                roots[1][countb] = -float(factors[i - 1])
                countb += 1

            else:
                countnb = -3
                while factors[i + countnb] != 'n':
                    countnb -= 1

                if factors[i + countnb + 1] == '+':
                    roots[1][countb] = float(factors[(i + countnb + 2):i])
                    countb += 1
                else:
                    roots[1][countb] = float(factors[(i + countnb + 1):i])
                    countb += 1

    print(roots)
    return roots, countf


def RootMul():
    roots, countf = RootReader()
    expression = [1 for i in range(countf + 1)]

    for i in range(countf):
        expression[0] *= roots[0][i]
    # n^x term

    for i in range(countf):
        expression[countf] *= roots[1][i]
    # n^0 term

    return expression


'''
Although I've separated the n^x and n^0 cases, I think they can
actually be combined under a general formula.
Well, I'd think so but look at RootReader. I had to cover so many cases.
Still, it was worth the effort because now the user can put in any number.
Length and sign no longer matter, along with the special case '-n'
'''
