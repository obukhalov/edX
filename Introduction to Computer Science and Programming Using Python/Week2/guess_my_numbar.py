# -*- coding: utf-8 -*-

low = 0
high = 100

guess = int((low + high) / 2)

print('Please think of a number between 0 and 100!')

while True:
    print('Is your secret number {}?'.format(guess))    
    answer = input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly. ')
    if answer not in 'hlc':
        print('Sorry, I did not understand your input.')
        continue
    if answer == 'h':
        high = guess
        guess = int((low + high) / 2)
    elif answer == 'l':
        low = guess
        guess = int((low + high) / 2)
    else:
        print('Game over. Your secret number was: {}'.format(guess))
        break
