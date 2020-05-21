# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 18:31:24 2020

@author: Silverxenfx
"""

import numpy as np
from matplotlib import pyplot as plt
a=np.array([20,18,30,22,15])
b=np.array([19,22,33,30,19])
c=np.arange(1,6,1)
plt.title("ploted By Silverxenfx CS-6")
plt.xlabel("student")
plt.ylabel("sem")
plt.plot(c,a,"--")
plt.plot(c,b,"-")
plt.show()