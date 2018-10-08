# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

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
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    count = 0
    for char in secretWord:
        if char in lettersGuessed:
            count += 1

    return count == len(secretWord)

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.

    The hint says that the code should be similar to isWordGuessed() but I think I'll
    have to use i instead of char
    Nvm I remembered how to append char to a str.
    '''
    
    guess = ''
    i = 0
    
    for char in secretWord:
        if char not in lettersGuessed:
            guess += '_ '

        else:
            guess += char

    return guess



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.

    OK that was surprisingly simple. Seems like you have to import the whole module
    when within the scope of a function
    '''
    import string
    alphabet = string.ascii_lowercase
    unguessed = ''
    
    for char in alphabet:
        if char not in lettersGuessed:
            unguessed += char
            
    return unguessed
        

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains. X

    * Ask the user to supply one guess (i.e. letter) per round. X

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    countg = 8
    length = len(secretWord)
    lettersGuessed = []
    unguessed = getAvailableLetters(lettersGuessed)
    guessA = '_ ' * length
    lettersTemp = []
    mark = 0
    
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(length) + ' letters long.')
    

    while countg > 0:
        print('-----------')
        
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('Congratulations, you won!')
            mark = 1
            return mark

        else:
            print('You have ' + str(countg) + ' guesses left.')
            print('Available Letters: ' + unguessed)
            letterGuess = input('Please guess a letter: ' )

            letterLC = letterGuess.lower()
            lettersGuessed.append(letterLC)
            unguessed = getAvailableLetters(lettersGuessed)
            guessB = getGuessedWord(secretWord, lettersGuessed)
            
            if letterLC in lettersTemp:
                print("Oops! You've already guessed that letter: " + guessB)

            elif guessA == guessB:
                print('Oops! That letter is not in my word: ' + guessB)
                countg -= 1
            
            else:
                guessA = guessB
                print('Good guess: ' + guessB)

            lettersTemp += letterLC

    if mark != 1:
        print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')


            
    
    
    
def hanggame():
    wordList = loadWords()
    secretWord = chooseWord(wordlist)

    hangman(secretWord)
    

    





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
