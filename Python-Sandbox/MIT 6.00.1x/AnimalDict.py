animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
animals['b'].append('bear')


def how_many(aDict):
    '''
    aDict: Dict where all the values are lists
    returns: int, num of values in dict
    aDict.values() extracts the values. Then how to count within each entry?
    Count += Length of value

    Alt way is to take aDict.values() and count the length of each value,
    since each list can also be treated as an object.
    '''
    count = 0
    for key in aDict:
        count += len(aDict[key])

    return count


def biggest(aDict):
    '''
    aDict: Dict where all the values are lists
    returns the key with the largest num of values associated with it.
    I had some brief confusion over how to compare the values and keys.

    There's a simpler solution: max(aDict). That returns the key with the
    greatest length, assuming all values are lists. I suspect that's why
    this isn't the model answer.

    In fact you can directly find len(aDict[key]). I think there's something
    quite missing in my thinking that makes my thought process so oddly
    convoluted. Moral of the story is that the key and value are closely linked.
    '''
    temp = []

    for char in aDict.keys():
        if len(aDict[char]) > len(temp):
            temp = aDict[char]

    return temp
