# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 23:18:27 2020

@author: Silverxenfx
"""
import string
import random
res = ''.join(random.choices(string.ascii_uppercase +
							string.ascii_lowercase, k = 100))
res=str(res)
res1=set(res)
print("String :\n",res)
print("Occurance")
for i in res1:
  print(res.count(i),i,end="  ")




