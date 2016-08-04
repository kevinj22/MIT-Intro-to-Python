# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 19:23:59 2016

@author: kevin
"""


# min = 2%
annualInterestRate=0.18
monthlyrate = annualInterestRate / 12
balance=999999
original = balance
paymentlower = original / 12.0
paymentupper = (original * (1 + monthlyrate)**12)/12.0
payment = round((paymentlower + paymentupper)/2,2)

while round(original,5) != 0:
    original = balance
    for i in range(1,13):
        original = original - payment
        original = original + (original * monthlyrate)
        #print "End B: " + str(original)
    if original < 0:
        paymentupper = payment
        payment= (paymentlower + paymentupper)/2
    elif original > 0:
        paymentlower= payment
        payment= (paymentlower + paymentupper)/2
    else:
        break
        
print "Lowest Payment: " + str(round(payment,2))