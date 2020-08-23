"""
Name: letter_freq_counter
Date: 20181008
Author: Lio Hong
Purpose: Counts letter frequencies.
Comments:
I actually found code examples online but couldn't make sense of it.
I can check my results against online databases at least, but I still
have to code this to use on encrypted texts.
There's a lot of patterns:
 - Single letter           - 26
 - Two-letter              - 26^2
 - Three-letter            - 26^3
 - Start of word           - 26. > at start. Find symbol and take next char.
 - End of word             - 26. < at end. Find symbol and take prev char
 - Followed by apostrophe  - Potentially 26 but more like 6 (stdrlv)
                             Find symbol and take next char.
 - Doubles                 - 26. Subset of two-letter techincally.
The hints are actually not that suitable because of how short they are, so
running a statistical analysis on them would be difficult because of the high
likelihood of random error.
Personally, it might be possible for me to find these letter frequencies myself.
Once I have the function setup, it's just a matter of finding data to crunch.
I could also search online for the figures, and make sure I get it from a
reliable source.
Regardless, I'll still have to crunch the numbers so as to handle encrypted
texts.

In the end though, I know there are other, more complex ciphers. The pendulum
one, the reverse, the space-less.
Very fitting entry into data analytics.
"""
import string
import operator

def get_passage():
    """
    Returns: A passage in plain text

    """
    files = ['laudato-si1-6.txt','laudato-si.txt','1m.txt','1m2.txt','1m3.txt',\
             'bible2.txt']
    print('Files available: ', files)
    num = int(input('Which file do you want to open? '))
    f = open(files[num], "r")
    story = removeNonAscii(str(f.read()))
    f.close()
    return story

def removeNonAscii(s):
    return "".join(i for i in s if ord(i)<128)

def word_Lister(text):
    # Returns a list of words
    textSplit = text.split()
    textWords = []
    numList = ['0','1','2','3','4','5','6','7','8,','9']
    for word in textSplit:
        word = word.lower()
        word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
        word = word.strip('""')
        if word in numList:
            pass
        else:
            textWords.append(word)
    return textWords

def wordFreq(text):
    # Returns a dict for word:freq
    textWords = word_Lister(text)
    textDict = {}
    for word in textWords:
        if word not in textDict:
            textDict[word] = 1
        else:
            textDict[word] += 1
    return textDict

def letterFreq(text):
    # Counts frequency 
    textWords = word_Lister(text)
    letterDict = {}
    for char in string.ascii_lowercase:
        letterDict[char] = 0
    
    for word in textWords:
        for letter in word:
            if letter in letterDict:
                letterDict[letter] += 1
            else:
                pass

    return letterDict

def rankLF(text):
    # Really janky stuff. But I managed to make it functional.
    letterDict = letterFreq(text)
    letterTot = 0
##    letterDictRanked = sorted(letterDict.items(), key=operator.itemgetter(0),reverse=True)
    letterDictRanked = sorted(letterDict.items() , reverse=True, key=lambda x: x[1])
    
    for pair in letterDictRanked:
        letterTot += pair[1]
        print(pair)
##        print(pair[0],end='')

    letterDict2 = letterDict.copy()
##    letterDictPerc = sorted(letterDict2.items() , reverse=True, key=lambda x: x[1])
    for key in letterDict:
        letterDict2[key] = round(letterDict2[key]/letterTot*100,3)
    letterDictPerc = sorted(letterDict2.items() , reverse=True, key=lambda x: x[1])

    for pair in letterDictPerc:
        print(pair,end='%\n')

    for pair in letterDictRanked:
        print(pair[0],end='')























