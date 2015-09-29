# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 09:26:20 2015

@author: lilun
"""
import numpy as np
import matplotlib.pyplot as plt

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

a=0
for i in xrange(1,11):
#    I1_middlepoint[i-1] = 0
    for j in xrange(1,i+1):
        k=j+0.0
        m=i+0.0
        I1_middlepoint[i-1]=I1_middlepoint[i-1]+np.power((-1.+(k-0.5)*(2/m)),5);
        
    abs_error_I1_middlepoint[i-1]=I1_middlepoint[i-1]-0
    
plt.plot(N,np.log(abs_error_I1_middlepoint[,10]))
np.log()