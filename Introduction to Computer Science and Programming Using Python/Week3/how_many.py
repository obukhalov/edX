# -*- coding: utf-8 -*-

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    result = 0
    for entry in aDict:
        result += len(aDict[entry])

    return result

