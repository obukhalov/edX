# -*- coding: utf-8 -*-

from getAvailableLetters import getAvailableLetters
from isWordGuessed import isWordGuessed
from getGuessedWord import getGuessedWord

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

    lettersGuessed = []
    mistakesMade = 8

    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is {} letters long.'.format(len(secretWord)))

    while mistakesMade > 0:

        availableLetters = getAvailableLetters(lettersGuessed)

        print('-------------')
        print('You have {} guesses left.'.format(mistakesMade))
        print('Available letters: {}'.format(availableLetters))
        
        guess = input('Please guess a letter: ').lower()
        if not guess.isalpha():
            print('Only aplphabet characters is allowed to be entered!')
            continue
        elif len(guess) != 1:
            print('You should enter one characted at a time!')
            continue

        if guess not in availableLetters:
            print('Oops! You\'ve already guessed that letter: {}'.format(getGuessedWord(secretWord, lettersGuessed)))
            continue
        elif guess in secretWord:
            lettersGuessed.append(guess)
            print('Good guess: {}'.format(getGuessedWord(secretWord, lettersGuessed)))
            if isWordGuessed(secretWord, lettersGuessed):
                print('-------------')
                print('Congratulations, you won!')
                quit()
        else:
            lettersGuessed.append(guess)
            print('Oops! That letter is not in my word: {}'.format(getGuessedWord(secretWord, lettersGuessed)))
            mistakesMade -= 1


    print('-------------')
    print('Sorry, you ran out of guesses. The word was {}.'.format(secretWord))

if  __name__ == '__main__':

    secretWord = 'secret'
    hangman(secretWord)
