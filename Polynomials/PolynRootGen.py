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
                for j in range(2, 7):
                    if factors[i + j] == 'n':
                        roots[0][counta] = float(factors[(i + 1):(i + j)])
                        counta += 1
            # This loop traverse the entire string,
            # so when it reaches the end it exceeds the index


        elif factors[i] == ')':
            roots[1][countb] = float(factors[i - 1])
            countb += 1

    print(roots)
