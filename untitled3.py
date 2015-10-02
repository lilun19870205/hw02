# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 15:51:49 2015

@author: lilun
"""

import scipy as sp
import scipy.optimize
import matplotlib.pyplot as plt

n=10
x=sp.linspace(0, sp.pi/2,n)
y=sp.sin(x)

def reconstruct(c):
    y_appx=0*x
    for i in range(len(c)):
        y_appx+=c[i]*x**i
        return y_appx

def objective(c):
    y_appx=reconstruct(c)
    e=y_appx-y
    return sp.linalg.norm(e,sp.inf)

c0=[0,1.0/1.6]
sol=sp.optimize.minimize(objective,c0)
c=sol.x
y_appx=reconstruct(c)

plt.plot(x,y, 'k-',x,y_appx,'r--')bi