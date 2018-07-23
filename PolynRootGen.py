def RootReader():
    print('This function produces a polynomial from roots ' + \
          'of the form (a*n-b).')
    factors = input('Enter your roots: ')
    print(factors + 'a')

    # Currently only works with single digits

    roots = [[0 for i in range(len(factors))] for i in range(2)]
    counta = 0
    countb = 0

    for i in range(len(factors)):
        if factors[i] == '(':
            if factors[i + 1] == 'n':
                roots[0][counta] = 1
                counta += 1
            else:
                roots[0][counta] = int(factors[i + 1])
                counta += 1
        elif factors[i] == '+':
            roots[1][countb] = int(factors[i + 1])
            countb += 1

    print(roots)
