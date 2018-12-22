def dupeFinder(lst):
    values = []
 
    for i in lst:
        values.append(lst.count(i))

    if max(values) > 1:
        return 'Has duplicates'
    else:
        return 'No duplicate elements'

def dupeFinderTEST():
    lst = randList()
    values = []
 
    for i in lst:
        values.append(lst.count(i))

    if max(values) > 1:
        return 'Has duplicates'
    else:
        return 'No duplicate elements'

def randList():
    import random
    lst = [random.randint(0,20) for i in range(random.randint(3,9))]
    return lst

