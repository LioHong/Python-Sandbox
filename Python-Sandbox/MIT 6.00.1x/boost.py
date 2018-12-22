'''
Possible application: Increase spawning of a certain colour of slime over
others.
Takes in two types of inputs: int or str with %
Ideally this will take in different colours and their corresponding values.
How do I do that?
I'd also need some data storage for dye colours and maybe their colour codes.

'''


def Boost(val):
    baseline = 1
    dyes = 16

    if type(val) == int or type(val) == float:
    # Boosts slime spawn by a factor of val

    elif '%' in str(val):
# Boosts slime spawn to certain percentage
