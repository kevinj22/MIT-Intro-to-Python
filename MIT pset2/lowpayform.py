# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 08:20:32 2016

@author: kevin
"""

annualInterestRate=0.2
monthlyrate = annualInterestRate / 12
balance=3329

payment = (monthlyrate*(round(balance,2)))/(1 - (1 + monthlyrate)**(-12))
print round(payment,2)