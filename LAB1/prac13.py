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

#Alternate Way
import random
z=random.randrange(1,1000)
print(‘Number :’ + str(z))
sum=0
while (z!=0):
w=z%10
sum=sum+w
z=z//10
print(sum)



