# -*- coding: utf-8 -*-
import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
    yet been guessed.
    '''
    _available_letters = ''
    for _letter in string.ascii_lowercase:
        if _letter not in lettersGuessed:
            _available_letters += _letter

    return _available_letters
