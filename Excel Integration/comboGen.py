"""
Name: comboGen
Date: 20181129
Author: Lio Hong
Purpose: Associate sequences of 3 digits with their permutations
Comments: Why am I doing something to do with PnC AGAIN? I'm no good
at this topic.
itertools.permutations(iterable, r=None) is close, but not quite there.
I want to cluster the permutations together.
Currently the sequences are stored as tuples of string(digits), so I have to
join them and convert them before I print them.
"""
from itertools import *

def oneGen():
    listAAA = []
    entry1 = 0
    for i in range(1,10):
        entry1 = [i*100 + i*10 + i]
        listAAA.append(entry1)
    for num in listAAA:
        print(num)
##    return listAAA

def twoGen():
    prelistAAB = []
    entry2 = []

    for i in range(0,10):
        for j in range(0,10):
            if i == j:
                pass
            else:
                seed = str(i)*2 + str(j)
                permSeed = permutations(seed)
                entry2 = dupeRemove(permSeed)
                prelistAAB.append(entry2)
                
    listAAB = listConvert(prelistAAB)

def twoGen01():
    listAAB = []
    entry2 = [0 for i in range(3)]
##    entry2 = []
    for i in range(1,10):
        for j in range(1,10):
            if i == j:
                pass
            else:
##                print(str(i) + ', ' + str(j))
##                entry2[0] = i*100 + i*10 + j
##                entry2 = [i*100 + i*10 + j]
                entry2 = str(i)*2 + str(j)
                perm2 = permutations(entry2)
                perm3 = dupeRemove(perm2)
##                print(entry2)
                listAAB.append(perm3)
##                print(listAAB)
    for perm in listAAB:
        for i in perm:
            print(str(i), end=' ')
        print()
##    return listAAB
        
def twoGen02():
    listAAB = []
    entry2 = []

    for i in range(0,10):
        for j in range(0,10):
            if i == j:
                pass
            else:
                seed = str(i)*2 + str(j)
                permSeed = permutations(seed)
                entry2 = dupeRemove(permSeed)
                listAAB.append(entry2)
    print(len(listAAB))
    for perm in listAAB:
        for i in perm:
            j = ''.join(i)
            print(j, end=', ')
        print()
##    return listAAB
        
def threeGen():
##Basically can generate permutations, but there are many duplicates
##If the number lies within one of the past entries, remove it.
    prelistABC = []
    entry3 = []
    ref = [i for i in range(1000)]
    
    for i in range(0,10):
        for j in range(0,10):
            for k in range(0,10):
                if i == j or i == k or j == k:
                    pass
                else:
                    seed = str(i) + str(j) + str(k)
                    entry3 = [seq for seq in permutations(seed)]
                    flag = 0
                    
                    for seq in entry3:
                        num = int(''.join(seq))
                        if num in ref:
                            ref.remove(num)
                        else:
                            flag += 1
                            break

                    if flag == 0:
                        prelistABC.append(entry3)
                        
    listABC = listConvert(prelistABC)
                        
##    
##    for perm in prelistABC:
##        sublist = []
##        for val in perm:
####            num = ''.join(val)
##            num = int(''.join(val))
##            sublist.append(num)
##        listABC.append(sublist)
##        
##    print(len(prelistABC))
##    for seq in listABC:
##        print(seq)
##    return listAAB
    
def threeGen01():
##Basically can generate permutations, but there are many duplicates
##If the number lies within one of the past entries, remove it.
    listABC = []
    entry3 = []
    ref = [i for i in range(1000)]
    
    for i in range(0,10):
        for j in range(0,10):
            for k in range(0,10):
                if i == j or i == k or j == k:
                    pass
                else:
                    seed = str(i) + str(j) + str(k)
                    entry3 = [seq for seq in permutations(seed)]
                    flag = 0
                    
                    for seq in entry3:
                        num = int(''.join(seq))
                        if num in ref:
                            ref.remove(num)
                        else:
                            flag += 1
                            break

                    if flag == 0:
                        listABC.append(entry3)
                    
    print(len(listABC))
    for perm in listABC:
        for i in perm:
            j = ''.join(i)
            print(j, end=', ')
        print()

def dupeRemove(lst):
    # Create an empty list to store unique elements
    uniqueList = []
    
    # Iterate over the original list and for each element
    # add it to uniqueList, if its not already there.
    for elem in lst:
        if elem not in uniqueList:
            uniqueList.append(elem)
    
    # Return the list of unique elements        
    return uniqueList

def listConvert(preList):
    trueList = []
    for perm in preList:
        subList = []
        for val in perm:
            num = ''.join(val)
##            num = int(''.join(val))
            subList.append(num)
        trueList.append(subList)
        
    print(len(trueList))
    for seq in trueList:
        print(seq)
    return trueList
    
