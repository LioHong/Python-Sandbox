"""
Name: PolynRootGen8
Date: 24-08-2018
Author: Lio Hong
Purpose: Produce a polynomial from user-inputted roots
Took a break to better understand itertools lib.
Subtasks:
X Process the coefficients and constants from the roots into lists
Generate coef for each n^x term for x in range(i)
      Sort coefs by value of x
      Generate combinations based on number of terms from COEF (and thus from CONST)
      X Select exclusive entries from COEF and CONST lists using itertools.compress()
      Sum sub-coefs together for n^x term
Return final expression in linear form
'' in table form
"""


def RootReader():
    # Converts user-inputted roots into coefficient array COEF and constant array CONST
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
        # Produces COEF from LHS
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

        # Produces CONST from RHS
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


'''
Trying to produce a loop that runs through all a-values for a term
then moves on to the next term and runs through all a-values again
So gen all the possible combinations first.
(Not gen directly, but have the POTENTIAL to gen them)
Then remove the overlapping ones.
'''

listA = [0, 1, 0]


def randList():
    # Simple random list generator
    import random
    a = 5
    dummy = [random.randint(0, 1) for i in range(a)]
    coefff = [random.randint(0, 10) for i in range(a)]
    consttt = [random.randint(0, 10) for i in range(a)]
    return dummy, coefff, consttt


def reflectList():
    # Produces list that has opposite entries of input
    # (1,0,1) -> (0,1,0)
    dum = randList()[0]
    dumRefl = []
    for entry in dum:
        if entry == 1:
            dumRefl.append(0)
        elif entry == 0:
            dumRefl.append(1)

    return dum, dumRefl


def testCompr():
    # Testing how compress() works with both COEF and CONST lists
    # And produce a term from multiplying the entries of the combined list
    # DONE
    coef = randList()[1]
    const = randList()[2]
    ref = reflectList()
    sel_coef = ref[0]
    sel_const = ref[1]
    import itertools

    print(coef)
    print(sel_coef)
    print(const)
    print(sel_const)

    term_coef = itertools.compress(coef, sel_coef)
    term_const = itertools.compress(const, sel_const)
    term = 1
    for i in term_coef:
        term *= i
    for j in term_const:
        term *= j

    return term


def combGen(n, r):
    # Generates combinations in the form C(n,r), where n is # of terms
    # and r is # of choices
    blankList = [0 for i in range(n)]
    flipList = blankList[:]
    # Without the index included, flipList is created as another ref to blankList
    # instead of duplicating blankList
    print(flipList)
    R = r + 1

    for i in range(r):
        if i == 0:
            for j in range(n):
                flipList = blankList[:]
                flipList[j] = 1
                print(flipList)
        else:
            # Increases number of 1s in list
            flipList = blankList[:]
            for k in range(i):
                flipList[k] = 1
            refList = flipList[:]
            print(flipList)

            for l in range(i, n):
                trunList = flipList[l:]
                print(trunList)
                try:
                    trunList.index(1)
                except:
                    print('value')

    '''
        else:
            #Increases number of 1s in list
            flipList = blankList[:]
            for k in range(i):
                flipList[k] = 1
            refList = flipList[:]

            #When r = 2, but only works when 0 comes after 1
            a = flipList.index(0)            
            for j in range(a,n):
                flipList = refList[:]
                flipList[j] = 1
                print(flipList)
    '''

    '''
    for i in range(R):
        if i == 0:
            for j in range(n):
                flipList = blankList[:]
                flipList[j] = 1
                print(flipList)
        else:
            #Increases number of 1s in list
            flipList = blankList[:]
            for k in range(i):
                flipList[k] = 1
            print(flipList)
    '''

    '''
    #When r = 1
    for i in range(n):
        flipList = blankList[:]
        flipList[i] = 1
        print(flipList)
    '''























