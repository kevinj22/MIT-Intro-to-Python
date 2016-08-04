# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
a = 0
b = 100

print "Please think of a number between 0 and 100!"

while True:
    guess=(a+b)/2
    print 'Is your secret number: ' + str(guess)    
    HorL = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if HorL == 'h':
        b = guess
    elif HorL == 'l':
        a = guess
    elif HorL == 'c':
        break
    else:
        print 'Sorry, I did not understand your input.\n'

print 'Game over. Your secret number was: ' + str(guess)