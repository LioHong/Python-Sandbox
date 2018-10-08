"""
Name: 06_is_list_permutation
Author: Lio Hong
Goal: Checks if two lists are permutations and then returns most common element.
Comments:
      Based on what I see, the function consists of several sub-functions
      I could probably split the sub-functions up as a better measure for defensive
      programming.
      OK, I did it. Now I see that the main function allows an overview of the control flow.
"""

#TEST ARG:
L1 = ['a', 'a', 'b']
L2 = ['a', 'b']
#Returns False
L3 = [1, 'b', 1, 'c', 'c', 1]
L4 = ['c', 1, 'b', 1, 1, 'c']
#Returns (1, 3, <class 'int'>)
L5 = [1, 'b', 1, 'c', 'c', 8]
L6 = ['c', 1, 'b', 1, 1, 'c']
#Returns False

def is_list_permutation(L1, L2):
      '''
      L1 and L2: lists containing integers and strings
      Returns False if L1 and L2 are not permutations of each other.
      A permutation is defined as having the same number of elements,
      and list elements appear the same number of times in both lists.

      If they are permutations of each other, returns a tuple of 3 items
      in this order: 
      the element occurring most, how many times it occurs, and its type

      If both lists are empty return the tuple (None, None, None). If more
      than one element occurs the most number of times, you can return any
      of them.
      '''

      #First check if permutation exists: Length
      if len(L1) != len(L2):
            return False

      #Dict conversions
      D1 = listToDict(L1)
      D2 = listToDict(L2)

      #Second and third checks: Same element with same freq, using the proxy list checkSame
      if checkIfSame(D1, D2) == True:
            #Generating the final answer tuple
            return maxCommonType(D1)
      else:
            return False

def listToDict(L):
      D = {}
      for i in L:
            try:
                  type(D[i])
            except:
                  D[i] = 1
            else:
                  D[i] += 1
      return D

def checkIfSame(D1, D2):
      checkSame = [0 for a in range(len(D1))]
      count = 0
      
      for k in D1:
            if k in D2:
                  if D1[k] == D2[k]:
                        checkSame[count] = 1
                  else:
                        checkSame[count] = 0
                  count += 1
            else:
                  checkSame[count] = 0
                  count += 1

      if 1 in checkSame:
            return True
      else:
            return False

def maxCommonType(D):
      checkMax = [0 for a in range(len(D))]
      count2 = 0

      for m in D:
            checkMax[count2] = D[m]
            count2 += 1
            
      answer = [0, max(checkMax), 0]

      for n in D:
            if D[n] == max(checkMax):
                  answer[0] = n

      answer[2] = type(answer[0])
      return answer
