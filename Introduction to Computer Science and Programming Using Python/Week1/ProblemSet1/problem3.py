# -*- coding: utf-8 -*-

s = 'azcbobobegghakl'
s = 'abcbcd'

alphabet = 'abcdefghijklmnopqrstuvwxyz'

_start = 0
_end = len(s)
_substr = ''
_result_str = ''

while _start < _end:

    for _idx in range(_start,_end):
        _substr += s[_idx]

        try:
            if alphabet.find(s[_idx+1]) >= alphabet.find(s[_idx]):
                pass
            else:
                _start += 1
                if len(_substr) > len(_result_str):
                    _result_str = _substr
                _substr = ''
                break
        except:
            _start += 1
            if len(_substr) > len(_result_str):
                _result_str = _substr
            _substr = ''
            break


print('Longest substring in alphabetical order is: ', _result_str)



