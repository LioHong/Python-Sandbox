"""
Name: ps4a_work
Date: 20181006
Author: Lio Hong
Purpose: Practise modularity by building up a word game.
Comments:
Thought I did this ages ago, but turns out I skipped it.
At least I learend about pseudocode and a lot of other stuff here.
"""

# The 6.00 Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, \
    'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, \
    'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, \
    'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  ", len(wordList), "words loaded.")

    return set(wordList)

    '''
    Apparently conversion to a set greatly reduces the computation time by at least 10x,
    but I can't get it to work. An error about sets being non-subscriptable is thrown up.
    Nvm the final test case is invalid anyway.
    Q: Could you please explain why returning set(wordList) would reduce the computational
    time? I imagine that using set() would help if there were words in wordList that were
    repeated, but since they are all unique, wouldn't wordList == set(wordList)?
    A: It has to do with sets using hashing to identify its contents rather than indices.
    https://stackoverflow.com/questions/17585730/what-does-hash-do-in-python    
    '''
    
def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    #get() returns the value for the key 'x', and default value is 0
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    '''
    #Basic function
    
    score = 0
    word = word.lower()
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter]
        
    score *= len(word)
    if len(word) == n:
        score += 50
        
    return score  
    '''
    
    '''
    Attempt at try-except. Kind of worked? The program didn't crash at least.
    Issue arose when I used ValueError instead of KeyError.
    Probably not needed based on next problem description which shows how to avoid
    KeyError using dict.get(key,default)
    Wanted to loop this but the best I can do is to break.
    Probably can't be helped because the input is fixed and can't be changed.
    '''
    score = 0
    word = word.lower()
    wordLength = len(word)
    
    while True:
        if wordLength > n:
            print('Word is too long!')
            break
        elif wordLength == 0:
            print('No word detected!')
            break
        
        try:
            for letter in word:
                score += SCRABBLE_LETTER_VALUES[letter]
            score *= wordLength
        except KeyError:
            print('Please type letters only.')
            break
        else:        
            if wordLength == n:
                score += 50
            print('"'+word+'"' + ' earned: ' + str(score) + ' points!')
            return score

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
hand = {'t': 2, 'e': 2, 's': 2, 'r': 1}

def updateHand(hand, word):
##Basic code without accounting for any errors.
##The biggest issue was copying the dictionary so that I wouldn't edit the
##original hand dictionary.
##Basic function is only 4 lines long. With all the error handling it grows
##a few times that.
##FOR SOME REASON DOCSTRINGS IN THIS FUNCTION ARE DISLIKED

    handNew = hand.copy()
    for letter in word:
        handNew[letter] -= 1
    return handNew

def updateHand2(handOG, word):
##"""
##Assumes that 'hand' has all the letters in word.
##In other words, this assumes that however many times
##a letter appears in 'word', 'hand' has at least as
##many of that letter in it. 
##
##Updates the hand: uses up the letters in the griven word
##and returns the new hand, without those letters in it.
##
##Has no side effects: does not modify hand.
##
##word: string
##hand: dictionary (string -> int)    
##returns: dictionary (string -> int)
##
##Cases:
##Word length is 0/shorter/longer than hand
##Word contains numbers or symbols --> hand.get(key,default)
##Word contains letters not in hand
##"""
##    
##'''
##Problem now is making a loop for this function. Something like Problem #1
##where the function breaks instead of returning a value.
##'''
    
    hand = handOG
    word = word.lower()
    wordLength = len(word)
    handLength = 0
    for h in hand:
        handLength += hand[h] 
    
    if wordLength > handLength:
        print('Word is too long!')

    elif wordLength == 0:
        print('No word detected!')
    
##    elif hand.get(letter,0) == 0:
##        print('Word contains letters/symbols not in hand!')
##        break
##
##    for letter in word:
##        if letter in hand:
##            hand[letter] -= 1

    for letter in word:
        if hand.get(letter,0) == 0:
            print('Word contains letters/symbols not in hand!')
            break
            
        else: 
            hand[letter] -= 1
            
    return hand

#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
##    handVal = hand.copy()
    wCheck = word in wordList
    hCheck = True
    handCopy = hand.copy()

    for letter in word:
        if handCopy.get(letter,0) == 0:
            hCheck = False
            break
            
        else: 
            handCopy[letter] -= 1
            continue
##    print(wCheck)
##    print(hCheck)
##    print(wCheck and hCheck)
    return (wCheck and hCheck)

#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    handLength = 0
    for h in hand:
        handLength += hand[h]
    return handLength


def playHand1(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed whne the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function;
    # Do your coding within the pseudocode (leaving those comments in-place!)
    
    # Keep track of the total score
    scoreTot = 0
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
    
        # Display the hand
        print('Please type in a word using letters from the hand: ')
        print('Current Hand: ' + str(hand))
        # Ask user for input
        print('If you wish to end, type a period(.)')
        word = input('Your word: ')

        # If the input is a single period:
        if word == '.':
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if isValidWord(word, hand, wordList) == False:
                # Reject invalid word (print a message followed by a blank line)
                print('This word is invalid. Try again.' + '\n')
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                scoreTot += getWordScore(word, n)
                print('Your total score is now: ' + str(scoreTot) + ' points!')
                # Update the hand
                hand = updateHand(hand, word)
                
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if hand[max(hand)] == 0:
        print('Out of letters! ',end='')
    else:
        print('Game Over. ',end='')
    print('Your total score is ' + str(scoreTot) + ' points!')
    
def playHand(hand, wordList, n):
    scoreTot = 0
    while calculateHandlen(hand) > 0:
        print('Please type in a word using letters from the hand: ')
        print('Current Hand: ',end='')
        #Converts the hand to a human-readable format.
        for letter in hand:
            print(letter * hand[letter],end='')
        print('\n' + 'If you wish to end, type a period(.)')
        word = input('Your word: ')

        if word == '.':
            break   
        else:
            if isValidWord(word, hand, wordList) == False:
                print('This word is invalid. Try again.')
            else:
                scoreTot += getWordScore(word, n)
                print('Your total score is now: ' + str(scoreTot) + ' points!')
                hand = updateHand(hand, word)
                
    if calculateHandlen(hand) == 0:
        print('Out of letters! ',end='')
    else:
        print('Round Over. ',end='')
    print('Your total score is ' + str(scoreTot) + ' points!')
#
# Problem #5: Playing a game
#

##wordList = loadWords()
######print(wordList[:100])
##word = 'stng'
##hand = {'s':1,'t':1,'r':0,'i':1,'n':1,'g':1,'o':1}
####isValidWord(word, hand, wordList)
##n = 7

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    
    Ideal length: 15-20 lines
    Mine: 18 lines
    """
    n = 7
    hand = {}
    while True:
        choice = input('Game start. Do you want a new hand (n), a replayed hand (r) or to exit (e)? ')    
        if choice == 'n':
            hand = dealHand(n)
            handRound = hand.copy()
            playHand(handRound, wordList, n)
        elif choice == 'r' and hand == {}:
            print('You have not played a hand yet. Please play a new hand first!')
        elif choice == 'r':
            handRound = hand.copy()
            playHand(handRound, wordList, n)
        elif choice == 'e':
            break
        else:
            print('Invalid input. Try again.')
            
    print('Game Over.')


#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
