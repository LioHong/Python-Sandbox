def RootReader():
    print('This function produces a polynomial from roots ' + \
          'of the form (a*n-b).')
    factors = input('Enter your roots: ')
    countf = 0

    for h in range(len(factors)):
        if factors[h] == '(':
            countf += 1

    # Now works to 3 decimal places, or a negative num to 2dp
    # Or any int between -10,000 and 100,000

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
                # Rmb that a while loop is used for unknown
                # num of iterations
                roots[0][counta] = float(factors[(i + 1):(i + countna)])
                counta += 1

        if factors[i] == ')':
            if factors[i - 3] == 'n' and factors[i - 2] == '+':
                roots[1][countb] = float(factors[i - 1])
                countb += 1

            elif factors[i - 3] == 'n' and factors[i - 2] == '-':
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

    return roots


def RootMul():
    roots = RootReader()
