# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 09:57:21 2015

@author: lilun
"""

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,3.14159,100)
dx=x[1]-x[0]
y=np.sin(x)
z=np.gradient(y,dx)
plt.plot(x,y,'k-',x,z,'b-')
plt.show()