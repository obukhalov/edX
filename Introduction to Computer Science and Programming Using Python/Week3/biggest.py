# -*- coding: utf-8 -*-

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''

    result = False

    for entry in aDict:
        if not result:
            result = entry
        else:
            if len(aDict[entry]) > len(aDict[result]):
                result = entry

    return result

