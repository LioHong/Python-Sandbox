"""
Name: ps5
Date: 20181006
Author: Lio Hong
Purpose: Practise coding with classes using an encryption exercise.
Comments: Uses the Caesar cipher.
"""

import string
from randCipherer import *

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    files = ["story.txt","skinhorse1.txt","skinhorse2.txt","skinhorse3.txt",\
             "skinhorse4.txt","skinhorse5.txt"]
    f = open(files[5], "r")
    story = str(f.read())
    f.close()
    return story


WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
    
        
    def build_shift_dict1(self, shift):
        '''
        Thought I could compact this but this resulted in case mismatch
        '''
        alphabet = string.ascii_lowercase + string.ascii_uppercase
        encAB = {}
        for letter in alphabet:
            encAB[letter] = alphabet[(alphabet.find(letter) + shift) % 26]
        return encAB
    
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        abLow = string.ascii_lowercase
        abUp = string.ascii_uppercase
        
        encAB = {}
        for letter in abLow:
            encAB[letter] = abLow[(abLow.find(letter) + shift) % 26]
        for letter in abUp:
            encAB[letter] = abUp[(abUp.find(letter) + shift) % 26]

        return encAB

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        encMsg = []
        encAB = self.build_shift_dict(shift)

        for char in self.message_text:
            if char in encAB:
                encMsg.append(encAB[char])
            else:
                encMsg.append(char)

        return ''.join(encMsg)

    def apply_random(self):
        encMsg = []
        encAB = randCiph()

        for char in self.message_text:
            if char in encAB:
                encMsg.append(encAB[char])
            else:
                encMsg.append(char)

        return ''.join(encMsg)

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        Note: Unlike the parent class, this takes 3 parameters instead of 2.
        The extra is 'shift'.

        I had a problem with the __init__() returning the object address instead of text.
        This was because I'd put in the 'self' parameter instead of 'text'.
        '''
##        self.message_text = text
##        self.valid_words = load_words(WORDLIST_FILENAME)
        super().__init__(text)
        self.shift = shift

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        encAB = self.build_shift_dict()
        encAB2 = encAB.copy()
        return encAB2

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        encMsg = self.apply_shift(self.shift)
        return encMsg

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
##        self.encrypting_dict = self.get_encrypting_dict()
##        message_text_encrypted = self.get_message_text_encrypted(self)
        
class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        super().__init__(text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        wordCheck = [0 for i in range(26)]
        validWords = self.get_valid_words()
        maxCorrect = range(len((self.message_text.split())))

        for i in range(26):
            decMsg = self.apply_shift(i)
            decWords = decMsg.split()
            for word in decWords:
                if is_word(validWords, word) == True:
                    wordCheck[i] += 1

        shiftVal = wordCheck.index(max(wordCheck))
        decMsg = self.apply_shift(shiftVal)

        return shiftVal, decMsg

##        if max(wordCheck) == maxCorrect:
##            shiftVal = 26 - wordCheck.index(max(wordCheck))
##            decMsg = self.apply_shift(26)
##        else:
            
def decrypt_story():
#Assembling this was easy, though there was some noticeable lag.
    story = CiphertextMessage(get_story_string())
    answer = story.decrypt_message()
    return answer

#Example test case (Message)
##text = Message('Hello, there.')
##print('Expected Output: Jgnnq, vjgtg.')
##print('Actual Output  :', text.apply_shift(2))

#Example test case (PlaintextMessage)
##plaintext = PlaintextMessage('hello', 2)
##print('Expected Output: jgnnq')
##print('Actual Output  :', plaintext.get_message_text_encrypted())
##print('Shift changed to 7.')
##plaintext.change_shift(7)
##print('Expected Output: olssv')
##print('Actual Output  :', plaintext.get_message_text_encrypted())

#Example test case (CiphertextMessage)
##ciphertext = CiphertextMessage('jgnnq')
##print('Expected Output:', (24, 'hello'))
##print('Actual Output  :', ciphertext.decrypt_message())

'''
Skin Horse tests
Somebody put fan theories about the mysterious benefactors trying to free Virginia from
extirpation. I can safely say that they did not use Caesar ciphers.
It's inspired me to code a function that generates random ciphers.
'''
##hint1 = PlaintextMessage('UDFVQF AQQG RFQ IQHRBQ ROX NRMQ PDHYDTOX QZQG.',2)
##print('Output  :', hint1.get_message_text_encrypted())

##hint2 = PlaintextMessage('\
##2. PNR MISTAMPSM LAPPIR PFEDJ YD PNR AEESKAI YB A CSADP EYLYP LFSIP LH CAKYPPR ADO \
##PSCREISIH, NRE TSDO NRAIRO LH RSPNRE PSV YE CSDDH. PNSJ GYD’P LR A VFERIH TSISPAEH \
##KSMPYEH, LFP CSADP EYLYPJ CYDDA NAVVRD.',4)
##print('Output  :', hint2.get_message_text_encrypted())

#Example test case (PlaintextMessage) with random cipher
scrambled = Message('hello')
print('Original:',scrambled.get_message_text())
print('Output:', scrambled.apply_random())













