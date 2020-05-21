# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 11:58:11 2019

@author: Admin
"""


from random import *
user=int(input("enter your number"))
ran=randint(10,99)

if(user==ran):
    print("YOU WON $10000")
elif((user//10==ran%10)and(user%10==ran//10)):
    print("YOU WON $3000")
elif((user%10==ran%10)or(user%10==ran//10)or(ran%10==user//10)or(user//10==ran//10)):
    print("YOU WON $1000")
else :
    print("Try Next Time")
    
    
