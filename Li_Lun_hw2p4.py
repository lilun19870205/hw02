# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 09:49:08 2015

@author: lilun
"""
import numpy as np

def decimal_to_binary(x,n):
    integer_part=int(x)
    print integer_part
    s1=""
    if(integer_part==0):
        s1+=str(0)
    else:
        i=int(np.log2(integer_part))
        remain=integer_part-2**i
        s1+=str(1)
        while(i>0):
            if(remain<2**(i-1)):
                 s1+=str(0)
            else:
                 s1+=str(1)
                 remain=remain-2**(i-1)
            i=i-1
            
        
    
    float_part=x-float(integer_part)
    print integer_part,float_part
    s2=""
    for i in xrange(1,n+1):
#        i=float(i)
        print i
        if (float_part<(1/2.**i)):
            s2+=str(0)
        else:
            s2+=str(1)
            float_part=float_part-1/(2.**i)
        print "s2", s2
        print "float_part", float_part
    
    return s1,s2

def binary_to_decimal(i,f):
    m=len(i)
    n=len(f)
    integer_part=0.
    float_part=0.
    for j in xrange(0,m):
        integer_part=integer_part + float(i[j])*2**(m-j-1)
    for j in xrange(0,n):
        float_part=float_part + float(f[j])*(0.5)**(j+1)
    return integer_part+float_part
        

number=input()
precision=input()
#integer_part,float_part=decimal_to_binary(number,precision)
result=decimal_to_binary(number,precision)
print "the binary type of number",number,"is:",result[0],".",result[1]

print " please input the integer part of binary number:"
integer_part=raw_input()
print " please input the float part of binary number:"
float_part=raw_input()
result=binary_to_decimal(integer_part,float_part)
print "the decimal type of the number",integer_part,".",float_part,"is:",result

            
