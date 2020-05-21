# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 12:30:16 2019

@author: Admin
"""


from random import *
ran=randint(0,100)
print(ran)
while(True):
    x=int(input("enter number"))
    if(x==ran):
        print("Number is "+str(x))
        break
    elif(x>ran):
        print("Number is too High")
    else:
         print("Number is too low")
  

       
