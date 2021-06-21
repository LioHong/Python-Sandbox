"""
Name: PolynRootGen9
Date: 20180903
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
#Converts user-inputted roots into coefficient array COEF and constant array CONST
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
        #Produces COEF from LHS
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

        #Produces CONST from RHS
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
#Simple random list generator
    import random
    a = 5
    dummy = [random.randint(0,1) for i in range(a)]
    coefff = [random.randint(0,10) for i in range(a)]
    consttt = [random.randint(0,10) for i in range(a)]
    return dummy, coefff, consttt

def reflectList():
#Produces list that has opposite entries of input
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
#Testing how compress() works with both COEF and CONST lists
#And produce a term from multiplying the entries of the combined list
#DONE
    coef = randList()[1]
    const = randList()[2]
    ref = reflectList()
    sel_coef = ref[0]
    sel_const = ref[1]
    import itertools



    term_coef = itertools.compress(coef, sel_coef)
    term_const = itertools.compress(const, sel_const)
    term = 1
    for i in term_coef:
        print(i)
        term *= i
    for j in term_const:
        print(j)
        term *= j

    print(coef)
    print(sel_coef)
##    for i in term_coef:
##        print(i)
    print(const)
    print(sel_const)
##    for i in term_const:
##        print(i)

    return term

def twoGen(n):
#Generates combinations in the form C(n,r), where n is # of terms
#and r is # of choices
#I simplified this this by setting r = 2
    blankList = [0 for a in range(n)]
    #Without the index included, flipList is created as another ref to blankList
    #instead of duplicating blankList

    for b in range(2):
        if b == 0:
            onesList = walker(blankList)
            for i in onesList:
                print(i)
            print('=====')

        else:
            for jList in onesList:
                for e in range(1,len(i)):
                    trunList = jList[e:]

                    try:
                        trunList.index(1)

                    except:
                        twosList = walker(trunList)
                        for d in range(len(twosList)):
                            twosList[d] = jList[:e] + twosList[d]
                        for i in twosList:
                            print(i)
                        print('=====')
                        break
                        #This took so long to realise

                    finally:
                        #I just want to continue the loop
                        dummy = 0

def walker(testList):
#Where testList is a list full of 0s

    flipList = testList[:]
    p = len(testList)
    nestedList = []

    for j in range(p):
        flipList = testList[:]
        flipList[j] = 1
        nestedList.append(flipList)
    return nestedList

def walkerOne(testList):
#Where testList is a list such that [1,0,...,0]

    testList[0] = 0
    flipList = testList[:]
    p = len(testList)
    nestedList = []

    for j in range(p):
        flipList = testList[:]
        flipList[j] = 1
        nestedList.append(flipList)
    return nestedList

def wunners(n,r):
#Generates a list of n entries and r ones
    wunList = [0 for i in range(n)]
    for j in range(r):
        wunList[j] = 1

    print(wunList)
    return wunList

def wunSlicer(n,r):
#Preparation for multiple truncation through slicing
    ingredient = wunners(n,r)
    score = ingredient.index(0)
    count = 0
    length = n
    strips = [0 for i in range(r)]

    while count < r:
        strips[count] = [1] + [0 for i in range(length-1)]
        count += 1
        length -= 1

    for i in strips:
        print(i)

    return strips

def threeGen(n):
#Testing the clocks
    a = wunSlicer(n,3)
    print('===')

    indexLoc = 0

    for i in range(1,len(a)+1):
        b = walkerOne(a[-i])

        try:
            for j in b:
                j = [a[-i-1][indexLoc]] + j
                print(j)
        except:
            print('value')
            break
        finally:
            print('===')


















