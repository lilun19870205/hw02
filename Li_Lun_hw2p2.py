# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 09:26:20 2015

@author: lilun
"""
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import scipy.integrate

N=np.linspace(1,10,10)

I1_middlepoint=np.linspace(0,0,10)
I1_simpson=np.linspace(0,0,10)
I1_gauss=np.linspace(0,0,10)

I2_middlepoint=np.linspace(0,0,10)
I2_simpson=np.linspace(0,0,10)
I2_gauss=np.linspace(0,0,10)

I3_middlepoint=np.linspace(0,0,10)
I3_simpson=np.linspace(0,0,10)
I3_gauss=np.linspace(0,0,10)

abs_error_I1_middlepoint=np.linspace(0,0,10)


#for i in xrange(1,11):
##    I1_middlepoint[i-1] = 0
#    for j in xrange(1,i+1):
#        k=j+0.0
#        m=i+0.0
#        I1_middlepoint[i-1]=I1_middlepoint[i-1]+np.power((-1.+(k-0.5)*(2/m)),5);
#        
#    abs_error_I1_middlepoint[i-1]=I1_middlepoint[i-1]-0
#    
#plt.plot(N,np.log10(abs_error_I1_middlepoint),'r--')


for i in xrange(1,11):
    f=lambda x:x**5
    I1_quad=sp.integrate.quad(f,-1,1)
    I1_middlepoint[i-1]=I1_quad[0]
    I1_x=np.linspace(-1,1,i)
    I1_y=I1_x**5
    I1_simpson[i-1]=sp.integrate.simps(I1_y,I1_x)
    a=np.polynomial.legendre.leggauss(i)
    xi=-1+(2/2)*(1+a[0])
    for j in xrange(0,i):
        I1_gauss[i-1]=I1_gauss[i-1]+(xi[j]**5)*a[1][j]
    
I1_middlepoint_error=I1_middlepoint-0.
I1_simpson_error=I1_simpson - 0.
I1_gauss_error=I1_gauss-0.

