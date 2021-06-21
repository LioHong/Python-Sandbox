"""
Name: genPrimes2
Date: 20181005
Author: Lio Hong
Purpose: A generator that returns primes numbers on successive calls to
its method
Comments: Store a list of primes that is used to find whether subsequent
numbers are primes.

//Generators are used for printing out unbounded sequences, or finding a specific
value in a sequence.
Standard functions are more suitable for bounded sequences (though generators
can handle these as well).
Also use standard functions when more than two values have to be stored
in memory.
"""

def genPrimes():
    listPrimes = [2]
    count = 3
    prime = 2 #First prime number

    while True:
        listModulo = []
        for num in listPrimes:
            listModulo.append(count % num)

        if (0 in listModulo) == False:
            yield prime
            prime = count
            listPrimes.append(prime)

        count += 1


'''
A far more elegant example from online. Supposedly is more Pythonic as well.
Perhaps because of how wordy my code is. Apparently Java is also pretty wordy.
'''
def genPrimesANS():
    x = 2
    while True:
        flag = True
        for i in range(2, x):
            if not x % i:
                flag = False
                break
        if flag:
            yield x
        x += 1

#Is a generator still a generator if its yield statement is never reached?
#Yes.

def generator1():
    if True:
        yield 1

def generator2():
    if False:
        yield 1

g1 = generator1()
g2 = generator2()

print(type(g1))
print(type(g2))
print(g1.__next__())
print(g2.__next__())
