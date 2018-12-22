"""
Name: DifferenceEngine5
Date: 20180906
Author: Lio Hong
Purpose: Use the method of differences to find the roots of a polynomial
Polynomial may be randomly generated

"""
from PolynRootGen16 import *

def babbage():
    '''
    Allows the random polynomial generator to provide its output directly to
    the Difference Engine.
    Technically could be directly referenced, but this also provides an output.
    Calculation not necessary, can be compressed to 'return extrap'
    '''
    choice = ''
    while choice != 'OWN' and choice != 'RANDOM':
        print('I can find the roots of a polynomial from its values.')
        choice = input('Do you want a RANDOM polynomial or your OWN? ')

        if choice == 'OWN':
            expression = genPoly()
            num = len(expression[0])
            results = valueGen(expression[1],expression[0])
            
        elif choice == 'RANDOM':        
            import random
##            num = random.randint(3, 10)
            num = 11
            #The TypeError is related to the power with max value = 9
            powerList = [random.randint(0, 9) for x in range(num)]
            coefList = [random.randint(0, 9) for x in range(num)]
            results = valueGen(powerList,coefList)
            

        else:
            print('Please choose RANDOM or OWN.')

##    print(num)        
##    print(results)
##    print('=====')
    
    seq, y, i, j = DiffEng(num,results)
    extrap = 0

    for z in range(j):
        print(seq[z])
    print("\n" + "The difference lies on row: ", end='')
    print(y - 1)

    print("\n" + "Next term in series is: " + "\n")
    for y in range((j - 1), 1, -1):
        for x in range((i - 1), 0, -1):
            if seq[y][x] != 0:
                print(seq[y][x])
                extrap += seq[y][x]
                break

    print(seq[1][i - 1], end='')
    extrap += seq[1][i - 1]
    print('     +')
    print('____________')
    print(extrap)

    return


'''Checking with Excel, the differences are added in a diagonal line
I just got confused about which line to follow.
I've learnt a lot from this.
Defining functions, returning and calling variables, understanding of
loops and logic and abstraction as the core of programming.
Much of this is still crude, but I know how it should function now.
Checked with Excel again, this is indeed correct.
'''

def valueGen(powerList,coefList):
    '''
    This generates a random polynomial, then generates its output
    from f(0) to f(10).
    '''
    num = len(powerList)
    seqPoly = [x for x in range(num)]
    values = [0 for x in range(num)]

    for x in range(num):
        for y in range(num):
            subtotal = coefList[y] * seqPoly[x] ** powerList[y]
            # Value of each x^n term
            values[x] += subtotal

    print('powerList is ' + str(powerList))
    print('coefList is ' + str(coefList))
    print('=====')
    return values

def DiffEng(num,values):
    '''
    Does the heavy lifting using iterative subtraction.
    The overarching array 'seq' is kind of quirky because it contains
    metadata, input as well as output.
    Each output row holds a difference of that level.
    '''
    
    i, j = num, num+1
    seq = [[0 for x in range(i)] for y in range(j)]
    seq[0] = [x for x in range(i)]  # 0th row for Term numbers
    seq[1] = values  # 1st row for Input values
    seq_zero = [0 for x in range(i)]  # For reference purposes
    print(seq)
    
    for y in range(2, j):
        for term in range(i - 1):
            seq[y][term] = seq[y - 1][term + 1] - seq[y - 1][term]
##            print('+++++')
            
            if seq[y] == seq_zero:
                return seq, y, i, j
            # Detects end of array which is a row of zeroes

            elif seq[y][term] < 0:
                seq[y][term] = 0
            # Removes negative values
























