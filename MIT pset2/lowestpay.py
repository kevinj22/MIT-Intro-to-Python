# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 19:23:59 2016

@author: kevin
"""


# min = 2%
annualInterestRate=0.2
monthlyrate = annualInterestRate / 12
balance=3926
original = balance
payment = 0

while original > 0:
    original = balance
    payment= payment + 10    
    #print(original)    
    for i in range(1,13):
    
        original = original - payment
        original = original + (original * monthlyrate)
    #print "End B: " + str(original)
    
print "Lowest Payment: " + str(payment)