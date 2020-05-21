# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 18:24:01 2020

@author: Silverxenfx
"""








import numpy as np
a=np.arange(1,9,1)
print(a)
print(a.shape)
a=a.reshape(4,2)
print("arrangement of plants")
print(a)
n = np.delete(a, [5,6])
print("after removing 2 plants")
print(n)
n = np.append(n,[[1,1]])
y = np.argsort(n)
n=n[y]
n=np.delete(n, [3,4])
n=n.reshape(2,3)
print("After adding 2 new plants")
print(n)