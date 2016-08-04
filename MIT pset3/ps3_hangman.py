# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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
    show = []
    for let in secretWord:
        if let in lettersGuessed:
            show.append(str(let))
        else:
            show.append('_')
    guesses=''.join(show)
    
    if guesses == secretWord:
        return True    
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    show = []
    for let in secretWord:
        if let in lettersGuessed:
            show.append(str(let))
        else:
            show.append('_')
    return ' '.join(show)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    allLetters=string.ascii_lowercase
    avail = []
    for let in allLetters:
        if let in lettersGuessed:
            continue
        else:
            avail.append(let)
    return ''.join(avail)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed=[] 
    mistakesMade=0
    print "Welcome to the game Hangman!"
    print "I am thinking of a word that is " + str(len(secretWord)) + " letters long."
    while (mistakesMade < 8) & (isWordGuessed(secretWord, lettersGuessed) == False):
        availableLetters = getAvailableLetters(lettersGuessed)        
        print "-------------"
        print "You have " + str(8-mistakesMade) + " guesses left"        
        print "Available letters: ",
        print availableLetters
        guess = raw_input("Please guess a letter: ")
        
        if (len(guess) != 1) | (guess.isdigit() == True):
            print "Oops! Single letters only!: "
            continue
        
        if guess.lower() in lettersGuessed:
            print "Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed))
            continue            
                        
        guessLower=guess.lower()
        lettersGuessed.append(guessLower)
        if guessLower not in secretWord:
            mistakesMade += 1
            print "Oops! That letter is not in my word: " + str(getGuessedWord(secretWord, lettersGuessed))
        else:
            print "Good guess: " + str(getGuessedWord(secretWord, lettersGuessed))
    if (mistakesMade == 8):
        print "-------------"        
        print 'Sorry you ran out of guesses, the word was: ' + secretWord
    else:
        print "-------------"
        print "Congratulations, you won!"
        return None    
        






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = 'apple' #chooseWord(wordlist).lower()
hangman(secretWord)
