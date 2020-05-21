# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 13:05:03 2019

@author: Admin
"""

import random
z=random.randint(0,1000)
print("random number: "+str(z))
sum1=0
while(z>0):
    sum1=sum1+(z%10)
    
    z=z//10
print("Sum is "+str(sum1))    




