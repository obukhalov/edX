# -*- coding: utf-8 -*-

def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a < b:
        gcd = a
    else:
        gcd = b

    while bool(a % gcd) or bool(b % gcd):
        if gcd == 1:
            break
        gcd -= 1

    return gcd 
