"""
Name: randCipherer
Date: 20181006
Author: Lio Hong
Purpose: Generates random ciphers.
Comments: Inspired by a commenter on the Skin Horse webcomic who recently
posted some fan theories in a cipher to prevent spoiling others at first glance.
These ciphers proved not to be Caesar ciphers, which I'd just covered in
MIT 6.00.1x.
So this could come in handy for generating problems for a decipherer to tackle.
But that would be much harder to achieve.
Looks like it'll be through letter frequencies.
"""

import string, random
def randCiph():
    abLow = [char for char in string.ascii_lowercase]
    abLow2 = abLow[:]
    abUp = [char for char in string.ascii_uppercase]
    abUp2 = abUp[:]
    encAB = {}
    
    for letter in abLow:
        letterShift = random.choice(abLow2)
        while letter == letterShift:
            letterShift = random.choice(abLow2)
        encAB[letter] = letterShift
        abLow2.remove(letterShift)
        
    for letter in abUp:
        letterShift = random.choice(abUp2)
        while letter == letterShift:
            letterShift = random.choice(abUp2)
        encAB[letter] = letterShift
        abUp2.remove(letterShift)
        
    return encAB


