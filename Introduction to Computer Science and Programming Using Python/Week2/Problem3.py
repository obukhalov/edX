# -*- coding: utf-8 -*-

balance = 999999
annualInterestRate = 0.18 

def year_balance(balance, monthlyPayment):
    ''' The function return an annual balance for particular monthly payment rate '''

    for month in range(1,13):
        # Monthly payment
        balance = balance - monthlyPayment
        # Chagring of interest
        balance = balance + (annualInterestRate / 12) * balance

    return balance

min_month_payment = balance / 12
max_month_payment = balance * (1 + annualInterestRate / 12)**12 / 12
precise = 0.1

while True:
    check_payment = (min_month_payment + max_month_payment) / 2
    result = year_balance(balance, check_payment)
    #print('result: {}, month_payment: {}'.format(result, check_payment))

    if round(result,2) == 0:
        break
    elif result > 0:
        min_month_payment = check_payment
    else:
        max_month_payment = check_payment


print('Lowest Payment: {}'.format(round(check_payment,2)))
