def arrayMerge(lst):
    lenFin = len(lst) * len(lst[0])
    countf = 0
    lst02 = []

    for array in lst:
        for entry in array:
            lst02.append(entry)

    lst02.sort()
    return lst02
    
def arrayMergeTEST():
    lst = rand2D()
    lenFin = len(lst) * len(lst[0])
    countf = 0
    lst02 = []

    for array in lst:
        for entry in array:
            lst02.append(entry)

    lst02.sort()
    return lst02

def rand2D():
    import random
    terms, arrays = random.randint(3,9), random.randint(3,9)
    lst = [[random.randint(0,9) for n in range(terms)] for k in range(arrays)]
    print(lst)
    return lst


##    for k in range(len(lst)):
##        for n in range(len(lst[k])):
##            lst02[countf] = lst[k][n]
##            countf += 1
           

##    for array in lst:
##        for entry in array:
##            if lst02 == []:
##                lst02.append(entry)
##            elif entry >= lst02[-1]:
##                lst02.append(entry)
##            elif entry in lst02:
##                a = lst02.index(entry)
##                lst02.insert(a,entry)
##
##            else:
##                lst02.append(100+entry)

            
                
            
##            if entry == min(lst02):
##                lst02.remove(entry)
##                lst02.insert(0,entry)
##
##            elif entry == max(lst02):
##                lst02.remove(entry)
##                lst02.append(entry)

    
    
