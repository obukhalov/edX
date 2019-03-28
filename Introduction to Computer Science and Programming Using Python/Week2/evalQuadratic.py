# -*- coding: utf-8 -*-

def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return a*x**2 + b*x + c


print(evalQuadratic(1,2,3,4))
