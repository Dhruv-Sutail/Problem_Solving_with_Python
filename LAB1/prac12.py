# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 12:45:31 2019

@author: Admin
"""


import datetime
name=input("enter your name")
age=input("enter age")
num=int(input("enter number"))
subtime=((datetime.datetime.today()).ctime())
print(name +"\n age:"+str(age)+"\n Number:"+str(num)+"\n"+"Last from edited on "+str(subtime))




