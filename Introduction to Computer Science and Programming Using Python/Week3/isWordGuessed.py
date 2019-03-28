# -*- coding: utf-8 -*-

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    _match = True

    for _letter in secretWord:
        if _letter not in lettersGuessed:
            _match = False

    return _match
