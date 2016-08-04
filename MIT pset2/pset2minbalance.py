# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 18:50:04 2016

@author: kevin
"""

# min = 2%
annualInterestRate=0.2
monthlyrate = annualInterestRate / 12
monthlyPaymentRate = 0.04
balance=4213
totalpaid=0

for i in range(1,13):
        
    MinPay = monthlyPaymentRate * balance
    balance = balance - MinPay
    balance = balance + (balance * monthlyrate)
    totalpaid = totalpaid + MinPay
    print "Month: " + str(i) 
    print "Minimum monthly payment: " + str(round(MinPay,2)) 
    print "Remaining balance: " + str(round(balance,2))
    if i == 12:
        print "Total paid: " + str(round(totalpaid,2))
        print "Remaining balance: " + str(round(balance,2))
    
