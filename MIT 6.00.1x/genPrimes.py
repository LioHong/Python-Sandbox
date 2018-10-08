"""
Name: genPrimes
Date: 20181005
Author: Lio Hong
Purpose: A generator that returns primes numbers on successive calls to
its method
Comments: Store a list of primes that is used to find whether subsequent
numbers are primes. 
"""

def genPrimes():
    listPrimes = [2]
    count = 3
    prime = count
    
    while True:
        listModulo = []
        for num in listPrimes:
            listModulo.append(count % num)

        if (0 in listModulo) == False:
            print('in')
            prime = count
            listPrimes.append(prime)
            yield prime
            
        print(count) 
        print(listPrimes)
        print(listModulo)
        
            
        count += 1



            
##            if count % num != 0 and count % 2 == 1:
##                print(num)
##                print(count % num != 0)
##                prime = count
##                listPrimes.append(prime)
##                print(listPrimes)
##                yield prime                      

##        count += 1
