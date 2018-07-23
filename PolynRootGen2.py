def RootReader():
    print('This function produces a polynomial from roots ' + \
          'of the form (a*n-b).')
    factors = input('Enter your roots: ')
    countf = 0

    for h in range(len(factors)):
        if factors[h] == '(':
            countf += 1

    # Now works to 2 decimal places

    roots = [[0 for i in range(countf)] for i in range(2)]
    counta = 0
    countb = 0

    for i in range(len(factors)):
        if factors[i] == '(':
            for j in range(2, 6):
                print('counta is ' + str(counta))

                if factors[i + 1] == 'n':
                    print(factors[i])
                    print(factors[i + 1])
                    roots[0][counta] = 1
                    counta += 1
                    print('N-d')

                elif factors[i + j] == 'n':
                    print(j)
                    roots[0][counta] = float(factors[(i + 1):(i + j)])
                    counta += 1


        elif factors[i] == ')':
            roots[1][countb] = float(factors[i - 1])
            countb += 1

    print(roots)
