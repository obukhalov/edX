def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    inc_list = []
    dec_list = []
    _tmp_inc_list = []
    _tmp_dec_list = []


    for i in range(0,len(L)):
        if i == 0:
            _tmp_inc_list.append(L[i])
            _tmp_dec_list.append(L[i])
        else:
            if L[i] == L[i - 1]:
                _tmp_inc_list.append(L[i])
                _tmp_dec_list.append(L[i])
            elif L[i] > L[i - 1]:
                _tmp_inc_list.append(L[i])
                if len(_tmp_dec_list) > len(dec_list):
                    dec_list = _tmp_dec_list.copy()
                    _tmp_dec_list = [L[i]]
                else:
                    _tmp_dec_list = [L[i]]
            else:
                _tmp_dec_list.append(L[i])
                if len(_tmp_inc_list) > len(inc_list):
                    inc_list = _tmp_inc_list.copy()
                    _tmp_inc_list = [L[i]]
                else:
                    _tmp_inc_list = [L[i]]


    if len(_tmp_dec_list) > len(dec_list):
        dec_list = _tmp_dec_list.copy()
    if len(_tmp_inc_list) > len(inc_list):
        inc_list = _tmp_inc_list.copy()
    #print(inc_list)
    #print(dec_list)

    if len(inc_list) > len(dec_list):
        sum = 0
        for val in inc_list:
            sum += val
    elif len(dec_list) > len(inc_list):
        sum = 0
        for val in dec_list:
            sum += val
    elif len(dec_list) == 0 and len(inc_list) == 0:
        sum = 0
    else:
        if L.index(inc_list[0]) < L.index(dec_list[0]):
            sum = 0
            for val in inc_list:
                sum += val
        else:
            sum = 0
            for val in dec_list:
                sum += val
    
    return sum

L = [5,4,3,2,5,6,7]
print(longest_run(L))
