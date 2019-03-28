# -*- coding: utf-8 -*-

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''

    _guessed_word = ''

    for _letter in secretWord:
        if _letter in lettersGuessed:
            _guessed_word += _letter
        else:
            _guessed_word += '_ '

    return _guessed_word

        
