"""
Name: 09_deep_reverse
Author: Lio Hong
Date: 20180726
Goal:
      Assumes L is a list of lists whose elements are ints.
      Mutates L such that it reverses its elements and also reverses the order of
      the int elements in every element of L. 
      It does not return anything.
      For example, if L = [[1, 2], [3, 4], [5, 6, 7]] then deep_reverse(L)
      mutates L to be [[7, 6, 5], [4, 3], [2, 1]]
"""
L = [[1, 2], [3, 4], [5, 6, 7], [8,9,10,11]]

def deep_reverse(L):
      invL = L[::-1]
      for i in range(len(invL)):
            invL[i] = invL[i][::-1]
            
      print(invL)
