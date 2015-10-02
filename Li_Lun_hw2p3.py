# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 10:18:14 2015

@author: lilun
"""
#Algorithm is found from the Internet

import time



a=[]


def find_primes(n):
    i=2
    while(i<=n):
        j=2
        while(j<=(i/j)):
             if not(i%j):break
             j=j+1
        if(j>i/j): 
            print i, " is prime"
            a.append(i)
        i=i+1
    return a

n=input('please input number n :')
t0=time.time()
b=find_primes(n)
print b
print "all prime number below n is found"
te=time.time()
t=te-t0
print t