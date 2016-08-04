# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 12:52:17 2016

@author: kevin
"""
def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)
    
def radiationExposure(start, stop, step):  
    a = start
    b = stop
    total = 0
    n = (b - a) /step
    steps=[]
    # Need to generate steps manually due
    # To range not handling floats
    # And numpy.linspace not allowed
    for i in range(0,int(n)):
        steps.append(a) 
        a = a + step 
      
    for j in steps:
        area = f(j)
        total += area

    return step*total
    
