# -*- coding: utf-8 -*-

test = ('I', 'am', 'a', 'test', 'tuple')

def oddTuples(aTup):
    '''
    aTup: a tuple
                
    returns: tuple, every other element of aTup. 
    '''

    _oddTuples = ()
    for _idx in range(0,len(aTup)):
        if not _idx % 2:
            _oddTuples += (aTup[_idx],)

    return _oddTuples

print(oddTuples(test))


