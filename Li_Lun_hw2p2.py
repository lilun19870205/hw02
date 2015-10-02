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

N=np.linspace(1,10,10)

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
    I1_x=np.linspace(-1,1,i+1)
    I1_xx=np.linspace(0,0,i)
    for j in xrange(0,i):
        I1_xx[j]=(I1_x[j]+I1_x[j+1])/2
    I1_y=I1_x**5
    I1_yy=I1_xx**5
    I1_middlepoint[i-1]=np.trapz(I1_yy,I1_xx)
    I1_simpson[i-1]=sp.integrate.simps(I1_y,I1_x)
    a=np.polynomial.legendre.leggauss(i)
    xi=1*a[0]+0
    I1_gauss[i-1]=np.sum((xi**5*a[1])*1)
    
I1_middlepoint_error=I1_middlepoint-0.
I1_simpson_error=I1_simpson - 0.
I1_gauss_error=I1_gauss-0.


for i in xrange(1,11):
    I2_x=np.linspace(-5,5,i+1)
    I2_xx=np.linspace(0,0,i)
    for j in xrange(0,i):
        I2_xx[j]=(I2_x[j]+I2_x[j+1])/2
    I2_y=1/(I2_x**2+1)
    I2_yy=1/(I2_xx**2+1)
    I2_middlepoint[i-1]=np.trapz(I2_yy,I2_xx)
    I2_simpson[i-1]=sp.integrate.simps(I2_y,I2_x)
    a=np.polynomial.legendre.leggauss(i)
    xi=5*a[0]+0
    I2_gauss[i-1]=np.sum((1/(xi**2+1)*a[1])*5)

    
I2_middlepoint_error=I2_middlepoint-2.7468
I2_simpson_error=I2_simpson - 2.7468
I2_gauss_error=I2_gauss-2.7468
plt.plot(N,np.log10(abs(I2_middlepoint_error)),label="I2_middlepoint")
plt.plot(N,np.log10(abs(I2_simpson_error)),label="I2_simpson")
plt.plot(N,np.log10(abs(I2_gauss_error)),label="I2_gauss")
plt.legend(bbox_to_anchor=(1.05,1),loc=2,borderaxespad=0.)
plt.show()


for i in xrange(1,11):
    I3_x=np.linspace(0,np.pi,i+1)
    I3_xx=np.linspace(0,0,i)
    for j in xrange(0,i):
        I3_xx[j]=(I3_x[j]+I3_x[j+1])/2
    I3_y=I3_x*np.sin(I3_x)/(1+(np.cos(I3_x))**2)
    I3_yy=I3_xx*np.sin(I3_xx)/(1+(np.cos(I3_xx))**2)
    I3_middlepoint[i-1]=np.trapz(I3_yy,I3_xx)
    I3_simpson[i-1]=sp.integrate.simps(I3_y,I3_x)
    a=np.polynomial.legendre.leggauss(i)
    xi=(np.pi/2)*a[0]+np.pi/2
    I3_gauss[i-1]=np.sum(((xi*np.sin(xi)/(1+(np.cos(xi))**2))*a[1])*(np.pi/2))

    
I3_middlepoint_error=I3_middlepoint-(np.pi)**2/4
I3_simpson_error=I3_simpson - (np.pi)**2/4
I3_gauss_error=I3_gauss-(np.pi)**2/4
plt.plot(N,np.log10(abs(I3_middlepoint_error)),label="I3_middlepoint")
plt.plot(N,np.log10(abs(I3_simpson_error)),label="I3_simpson")
plt.plot(N,np.log10(abs(I3_gauss_error)),label="I3_gauss")
plt.legend(bbox_to_anchor=(1.05,1),loc=2,borderaxespad=0.)
plt.show()



