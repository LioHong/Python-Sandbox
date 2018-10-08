def Perm():
    import random
    countf = random.randint(4, 9)
    roots = [[i for i in range(countf)] for j in range(2)]
    for i in range(countf):
        roots[1][i] = -roots[0][i]

    print(roots)
    a = random.randint(2, int(countf / 2))
    print(a)

    import itertools
    coef_a = itertools.combinations(roots[0], a)
    for i in list(coef_a):
        print(i)
    '''
    count_half = int(countf/2)
    coef_a = [1 for i in range(count_half)]
    coef_b = coef_a
    #Temp array for cross-multiplying

    for dog in range(count_half):
          for bul in range(countf):
                coef_b[dog] = roots[1][bul]
                
                print(coef_b)
    '''


'''
Perm()

For a list of (a1, a2, ..., ax)
I want to generate a list of variable length c
(c1, c2, ..., cx/2)

Output:
For c = 1,
(a1)
...
(ax)

For c = 2,
(a1, a2)
...
(a1, ax)
(a2, a3)
...
(a2, ax)
...
...
(a(x-1), ax)

For c = x/2
(a1, a2, ..., ax/2)
...
(a1, a2, ..., a(x/2-1), ax)
(a1, a2, ..., ax/2, a(x/2+1))
...
...
(a(x/2), a(x/2+1), ..., ax)
















'''
