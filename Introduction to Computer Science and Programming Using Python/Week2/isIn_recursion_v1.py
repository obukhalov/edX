# -*- coding: utf-8 -*-

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    min_idx = 0
    max_idx = len(aStr)

    def bisec(min_idx, max_idx):
        if char == aStr[int((min_idx + max_idx)/2) - 1]:
            return True
        elif char == aStr[-1]:
            return True
        elif char < aStr[int((min_idx + max_idx)/2) - 1]:
            if int((min_idx + max_idx)/2) == 0:
                return False
            else:
                return bisec(min_idx, int((min_idx + max_idx)/2))
        else:
            if int((min_idx + max_idx)/2) == len(aStr) - 1:
                return False
            else:
                return bisec(int((min_idx + max_idx)/2), max_idx)

    return bisec(min_idx, max_idx)



        
