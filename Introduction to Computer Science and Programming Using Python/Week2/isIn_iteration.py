# -*- coding: utf-8 -*-

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    min_idx = 0
    max_idx = len(aStr)

    while abs(min_idx - max_idx) != 1:
        if char == aStr[int((min_idx + max_idx)/2) - 1]:
            return True
        elif char == aStr[-1]:
            return True
        elif char < aStr[int((min_idx + max_idx)/2) - 1]:
            max_idx = int((min_idx + max_idx)/2)
        else:
            min_idx = int((min_idx + max_idx)/2)

    return False


        
