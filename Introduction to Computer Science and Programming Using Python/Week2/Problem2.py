# -*- coding: utf-8 -*-

balance = 3926
annualInterestRate = 0.2 

def year_balance(balance, monthlyPayment):
    ''' The function return an annual balance for particular monthly payment rate '''

    for month in range(1,13):
        # Monthly payment
        balance = balance - monthlyPayment
        # Chagring of interest
        balance = balance + (annualInterestRate / 12) * balance

    return balance

check_payment = 10

while True:
    result = year_balance(balance, check_payment)

    if result <= 0:
        break
    else:
        check_payment += 10


print('Lowest Payment: {}'.format(check_payment))
