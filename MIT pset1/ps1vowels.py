# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 17:48:49 2016

@author: kevin
"""
count=0
s = 'azcbobobegghakl'
for l in s:
    if l in 'aeiou':
        count += 1
    else:
        continue

print 'Number of vowels: ' + str(count)