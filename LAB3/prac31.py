# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 10:00:00 2020

@author: Admin
"""

from random import *
ran=randint(1,52)

rank=ran%13
category=ran//13

if(rank==0):
    s="ACE"
elif(rank==10):
    s="Jack"
elif(rank==11):
    s="Queen"
elif(rank==12):
    s="King"
else:
    s=str(rank+1)
print("The Card you Picked is ",s)





