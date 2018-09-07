"""
Name: 11_applyF_filterG
Author: Lio Hong
Date: 20180726
Goal:
    Assumes L is a list of integers
    Assume functions f and g are defined for you.
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, returns either True or False
        
    Mutates L such that, for each element i originally in L, L contains i
    if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    
    For this question, you will not be able to see the test cases we run.
    This problem will test your ability to come up with your own test cases.
"""
'''
L = [0, -10, 5, 6, -4]
print(applyF_filterG(L, f, g))
print(L)

OUTPUT:
6
[5, 6]
'''

def applyF_filterG(L, f, g):
      mutL = []
      for j in L:
            if g(f(j)) == True:
                  mutL.append(j)

      print(mutL)
      
      if mutL == []:
            return -1
      else:
            return max(L)
      
      
def f(i):
    return i + 2

def g(i):
    return i > 5

def randoListo():
      import random
      L = [random.randint(-20,20) for i in range(random.randint(5,10))]
      return L
L = randoListo()
