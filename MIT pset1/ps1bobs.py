# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 17:51:13 2016

@author: kevin
"""

count=0
s = 'azcbobobegghakl'
szip =zip(s[:len(s)],s[1:],s[2:])

print szip
print type(szip)
s2= []
for i in range(len(szip)):
    s2.append(''.join(szip[i]))
    
count = 0
for item in s2:
    if 'bob' in item:
        count += 1
    
print count

# More compact method using list compreshension

list2 = [i+j+k for i,j,k in zip(s[:len(s)], s[1:],s[2:])]

count2 = 0
for item in list2:
    if 'bob' in item:
        count2+=1
        
print count2