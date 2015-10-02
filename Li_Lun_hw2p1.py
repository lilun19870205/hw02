# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:54:02 2015

@author: lilun
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import scipy.optimize

Z=np.loadtxt('atomic_number2.txt')
A=np.loadtxt('mass_number2.txt')
B=np.loadtxt('atomic_mass3.txt')
BB=B/Z

x1=A
x2=A**(0.666)
x3=Z**2/A**(0.333)
x4=((A-2*Z)**2)/A
x5=((-1)**(Z%2)+(-1)**((A-Z)%2))/A**(0.5)
Mt=np.array([x1,x2,x3,x4,x5])
M=Mt.transpose()
MtM=Mt.dot(M)
MtBB=Mt.dot(BB)

c=np.linalg.solve(MtM,MtBB)
xx=np.linspace(1,300,299)

BB_appx=c[0]*x1+c[1]*x2+c[2]*x3+c[3]*x4+c[4]*x5
plt.plot(A,BB,'k',A,BB_appx,'r--')
#plt.plot(A,BB_appx,'r--')
plt.show()

error_avg=np.mean(BB)-np.mean(BB_appx)
max_error=np.max(abs(BB-BB_appx))
print "error_avg =",error_avg
print "max_error =",max_error
print "the coefficient c is:",c






def reconstruct(c):
    y_appx=0*A
    y_appx=c[0]*x1+c[1]*x2+c[2]*x3+c[3]*x4+c[4]*x5
    return y_appx

def objective(c):
    y_appx=reconstruct(c)
    e=y_appx-BB
    return sp.linalg.norm(e,sp.inf)

c0=[1.,1.,1.,1.,1.]
sol=sp.optimize.minimize(objective,c0)
c=sol.x
y_appx=reconstruct(c)

plt.plot(A,BB, 'k-',A,y_appx,'r--')
plt.show()

error_avg=np.mean(BB)-np.mean(y_appx)
max_error=np.max(abs(BB-y_appx))
print "error_avg =",error_avg
print "max_error =",max_error
print "the coefficient c is:",c



