# -*- coding: utf-8 -*-

balance = 46 
annualInterestRate = 0.2 
monthlyPaymentRate = 0.05

for month in range(1,13):

    # Monthly payment
    balance = balance - balance * monthlyPaymentRate
    # Chagring of interest
    balance = balance + (annualInterestRate / 12) * balance

print('Remaining balance: {}'.format(round(balance,2)))
