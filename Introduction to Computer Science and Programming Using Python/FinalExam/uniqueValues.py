def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    # Your code here
    unique_list = []

    for _key in aDict:
        if list(aDict.values()).count(aDict[_key]) == 1:
            unique_list.append(_key)

    unique_list.sort()

    return unique_list

aDict = {3:3 , 2:2 , 1:1}
print(uniqueValues(aDict))
