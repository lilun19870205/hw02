# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 10:18:14 2015

@author: lilun
"""
import time


n=input('please input number n :')
i=2
t0=time.time()
while(i<=n):
    j=2
    while(j<=(i/j)):
        if not(i%j):break
        j=j+1
    if(j>i/j): print i, " is prime"
    i=i+1

print "all prime number below n is found"
te=time.time()
t=te-t0
print t