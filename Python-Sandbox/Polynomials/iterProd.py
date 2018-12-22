"""
Name: iterProd
Author: Lio Hong
Date: 20180905
Goal: Understand how itertools.product(*args, repeat=n) works and how to print
and sort the results
Description:
Cartesian product of input iterables.

Roughly equivalent to nested for-loops in a generator expression. For example,
product(A, B) returns the same as ((x,y) for x in A for y in B).

The nested loops cycle like an odometer with the rightmost element advancing on every
iteration. This pattern creates a lexicographic ordering so that if the input’s iterables
are sorted, the product tuples are emitted in sorted order.

To compute the product of an iterable with itself, specify the number of repetitions with
the optional repeat keyword argument. For example, product(A, repeat=4) means the same as
product(A, A, A, A).

This function is roughly equivalent to the following code, except that the actual
implementation does not build up intermediate results in memory:


Comments: I keep getting the generator object itself rather than its contents.
"""

def iterProd(*args, repeat=3):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

def listProd():
    lst = [list(i) for i in iterProd([0, 1], repeat=4)]
    return lst

def printProd():
    lst = listProd()
    for combo in lst:
        print(combo)

def sortProd():
    lst = listProd()
       
    sorter = [[] for i in range(len(lst[0])+1)]
    for combo in lst:
        a = combo.count(1)
        sorter[a].append(combo)

    for b in sorter:
        print(b)











        
