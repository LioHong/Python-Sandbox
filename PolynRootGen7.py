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
    '''
    roots, countf = RootReader()
    expression = [1 for i in range(countf+1)]
    count_half = int(countf/2)
    coef_a = [1 for i in range(count_half)]
    coef_b = coef_a
    #Temp array for cross-multiplying
    '''
    import random
    countf = random.randint(4, 9)
    roots = [[i for i in range(countf)] for j in range(2)]
    for i in range(countf):
        roots[1][i] = -roots[0][i]

    print(roots)
    count_half = random.randint(2, int(countf / 2))
    print("Half count is: " + str(count_half))

    import itertools
    coef_a = itertools.combinations(roots[0], count_half)
    for i in list(coef_a):
        temp_a = i
        print(temp_a)
        for j in range(count_half):
            for k in range(countf):
                if temp_a[j] != roots[0][k]:
                    for m in range(countf - j):
                        temp_b = [2 for n in range(countf - j)]
                        temp_b[m] = roots[0][k]
                    print(temp_b)


'''
Trying to produce a loop that runs through all a-values for a term
then moves on to the next term and runs through all a-values again
So gen all the possible combinations first.
(Not gen directly, but have the POTENTIAL to gen them)
Then remove the overlapping ones.
'''
