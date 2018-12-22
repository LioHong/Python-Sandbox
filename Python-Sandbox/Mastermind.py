"""
Name: Mastermind00
Date: 20181003
Author: Lio Hong
Purpose: Recreate the game 'Mastermind' with Python. Inspired by EthosLab
who is doing this in Minecraft
Rules:
1. Player 2 generates a combination of coloured beads -> CPU randomly generates
a sequence
2. Player 1 makes a guess
3. [P2] Check for beads with same colour and same position -> BLACK peg
4. Check for other beads with same colour only --> WHITE peg
#WHITE = #sameValue - #BLACK
Comments: COMPLETE
All you need to know are the rules to create a game. You don't have to
know how to beat it. I'm sure this is something profound for game design.

I found a pretty reliable approach to beat this game for 4 terms + 6 colours
First start with all same colours.
This identifies those terms that match.
Keep changing the colour for non-B terms, and position for non-W terms.
Usually the answer will be found within 6 tries.
"""

def comboGen():
    import random
##    numHoles = random.randint(4,9)
    numHoles = 4
    ansCombo = [random.randint(1,6) for i in range(numHoles)]
    print('Length of target sequence is ' + str(numHoles))

    return ansCombo

def guesser():
    ans = comboGen()
    numHoles = len(ans)
    guess = []
    pegs = [0,0]
    countg = 0
    countMax = 8

    print("I have a sequence of " + str(numHoles) + " terms, each from 1 to 6.")
    while guess != ans and countg < countMax:
##        print('Please make a guess of ' + str(numHoles) + ' terms: ')
##        guess = [int(x) for x in input().split()]

        guess = []
        g = input('Please make a guess: ')
        #Cheat code to show answer and break
        if g == 'answer':
            print(ans)
            break

        #Converts string input into list
        g1 = g.split()
        for term in g1:
            guess.append(int(term))

        if type(guess) != list:
            print('Input must be of type list!')

        elif len(guess) != numHoles:
            print('Input must have ' + str(numHoles) + ' terms.')

        else:
            pegs = pegChecker(guess,ans)
            print('Guess #' + str(countg + 1) + ': ' + str(guess) + ' || ' + \
                  str(pegs[0]) + 'B ' + str(pegs[1]) + 'W')
            countg += 1

    print('Game Over. Answer is ' + str(ans))
    
def pegChecker(guess,ans):
    guessCopy = guess[:]
    ansCopy = ans[:]
    numHoles = len(guess)
    pegBlack = 0
    pegWhite = 0
    listBlack = []

    #Find which terms are identical
    for i in range(numHoles):
        if guess[i] == ans[i]:
            pegBlack += 1
            listBlack.append(i)

    #Remove identical terms in reverse order
    listBlack.reverse()
    for index in listBlack:
        guessCopy.pop(index)
        ansCopy.pop(index)

    #Find terms with identical values
    for bead in guessCopy:
        if bead in ansCopy:
            pegWhite += 1
            ansCopy.remove(bead)

    return pegBlack, pegWhite

def pegChecker1():
##    guess and ans should be the parameter
    guess = comboGen()
    guessCopy = guess[:]
    ans = comboGen()
    ansCopy = ans[:]
    numHoles = len(guess)
    pegBlack = 0
    pegWhite = 0
    listBlack = []
    
    for i in range(numHoles):
        if guess[i] == ans[i]:
            pegBlack += 1
            listBlack.append(i)
            #Etho exploits item stacking to automatically execute this removal.
            #How to remove the term properly?

    listBlack.reverse()
    for index in listBlack:
        guessCopy.pop(index)
        ansCopy.pop(index)
    
    print(guess)
    print(ans)
    print('Indexes: ' + str(listBlack))
    print(guessCopy)
    print(ansCopy)

    for bead in guessCopy:
        if bead in ansCopy:
            pegWhite += 1
            ansCopy.remove(bead)

    print('=====')
    print(guessCopy)
    print(ansCopy)

    return pegBlack, pegWhite
    
##    guessCDict = {}
##    ansCDict = {}

##    for bead in guessCopy:
##        if bead in guessCDict:
##            guessCDict[bead] += 1
##        else:
##            guessCDict[bead] = 1
##
##    for bead in ansCopy:
##        if bead in ansCDict:
##            ansCDict[bead] += 1
##        else:
##            ansCDict[bead] = 1
            
##    print(guessCDict)
##    print(ansCDict) 

##    for bead in guessCDict:
##        if bead in ans


   








        
