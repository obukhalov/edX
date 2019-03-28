# -*- coding: utf-8 -*-

def square_root(x):
    '''
        x: int or float.
    '''
    min = 0
    max = x
    epsilon = 0.01
    count = 0

    guess = (min + max)/2

    while abs(guess*guess - x) > epsilon:

        if count >= 1000:
            break

        if guess*guess > x:
            max = guess
        else:
            min = guess
        
        guess = (min + max)/2
        count += 1

    return guess

print(square(72))
