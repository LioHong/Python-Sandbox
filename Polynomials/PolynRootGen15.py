"""
Name: PolynRootGen13
Date: 20180905
Author: Lio Hong
Purpose: Produce a polynomial from user-inputted roots
Took a break to better understand itertools lib.
Subtasks:
X Process the coefficients and constants from the roots into lists
Generate coef for each n^x term for x in range(i)
      Sort coefs by value of x
      X Generate combinations based on number of terms from COEF
      (and thus from CONST), using itertools.product()
      X Select exclusive entries from COEF and CONST lists using
      itertools.compress()
      Sum sub-coefs together for n^x term
Return final expression in linear form
'' in table form

Comments: It's finally done. It took two months exactly to finish this.
Maybe a week of actual coding in total.

"""
import itertools

def genPoly():
    factors = rootReader()
    roots = factors[0] #COEF and CONST
    terms = factors[1] + 1 #Number of terms
    sorter = comboSort(terms-1)
    sorterRflk = [[] for i in range(terms)]
    products = [0 for i in range(terms)]
    
    #I actually wanted to generate this dynamically, but figured that it would be
    #more effort than it was worth, especially now I'm so close to getting this functional.
    for i in range(terms):
        for j in sorter[i]:
            sorterRflk[i].append(reflectList(j))

    for i in range(terms):
        for j in range(len(sorter[i])):
            products[i] += crossMult(roots,sorter[i][j],sorterRflk[i][j])

    printPoly(products)

def rootReader():
#02
#Converts user-inputted roots into coefficient array COEF and constant array CONST
    print('This function produces a polynomial from roots ' + \
          'of the form (a*n-b).')
    factors = input('Enter your roots: ')
    countf = 0
    #Number of factors
    
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

    return roots, countf

def randList():
#03
#Simple random list generator
    import random
    a = 5
    dummy = [random.randint(0,1) for i in range(a)]
    coefff = [random.randint(0,10) for i in range(a)]
    consttt = [random.randint(0,10) for i in range(a)]
    return dummy, coefff, consttt


def reflectList(lst):
#04
#Produces list that has opposite entries of input
# (1,0,1) -> (0,1,0)
    reflect = []
    for entry in lst:
        if entry == 1:
            reflect.append(0)
        elif entry == 0:
            reflect.append(1)

    return reflect

def crossMult(lst,lstMul,lstMulR):
#05
#Testing how compress() works with both COEF and CONST lists
#And produce a term from multiplying the entries of the combined list
    #Reversing terms to counteract itertools.product()
    #NVM it's needed like this for polyPrint()
    coef = lst[0]
    const = lst[1]
    sel_coef = lstMul
    sel_const = lstMulR

    term_coef = itertools.compress(coef, sel_coef)
    term_const = itertools.compress(const, sel_const)
    
    term = 1
    for i in term_coef:
        term *= i
    for j in term_const:
        term *= j

    return term

def comboSort(r):
#06
#Produces the number of combinations based on r
    lst = [list(i) for i in itertools.product([0, 1], repeat=r)]

    sorter = [[] for i in range(len(lst[0])+1)]
    for combo in lst:
        a = combo.count(1)
        sorter[a].append(combo)

    return sorter

def printPoly(lst):
#Prodces human-readable polynomial format from coef
    termMax = len(lst)
    result = []
    resultInv = [0 for i in range(termMax)]

    #i refers to power
    #lst[i] refers to coef
    for i in range(termMax):
        if i == 0:
            result.append(str(lst[i]))

        elif i == 1 and lst[i] == 1:
            result.append('n')

        elif i == 1:
            result.append(str(lst[i])+'n')

        elif lst[i] == 1:
            result.append('n^'+str(i))

        elif i == -1 and lst[i] == 1:
            result.append('-n')

        elif lst[i] == -1:
            result.append('-n^'+str(i))
            
        else:
            result.append(str(lst[i])+'n^'+str(i))

    for j in range(termMax):
        resultInv[j] = result[-j-1]
        
    print('Result: ' + ' + '.join(resultInv))
    













