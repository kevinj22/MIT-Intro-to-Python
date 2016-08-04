# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 18:32:40 2016

@author: kevin
"""

def item_order(order):
    wcount=0
    scount=0
    hcount=0    
    splits = order.split(" ")
    for item in splits:
        if item == 'water':
            wcount += 1
        elif item == 'salad':
            scount += 1
        elif item == 'hamburger':
            hcount += 1
        else:
            continue
    return("salad:" + str(scount) + " hamburger:" + str(hcount) + " water:" + str(wcount))
    
print item_order("salad water hamburger salad hamburger")

        