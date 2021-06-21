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
                countn = 1
                while factors[i + countn] != 'n':
                    countn += 1
                # Rmb that a while loop is used for unknown
                # num of iterations
                print('i is ' + str(i))
                print(countn)
                roots[0][counta] = float(factors[(i + 1):(i + countn)])
                counta += 1

        '''if factors[i] == ')':
              if factors[i+1] == 'n':
                    roots[0][counta] = 1
                    counta += 1

              else:
                    countn = 1
                    while factors[i+countn] != 'n':
                          countn += 1
                    #Rmb that a while loop is used for unknown
                    #num of iterations

                    roots[0][counta] = float(factors[(i+1):(i+countn)])
                    counta += 1'''

    print(roots)
