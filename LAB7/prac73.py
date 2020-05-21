# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 22:47:44 2020

@author: Silverxenfx
"""

f=open("test.txt","r")
print("PM's Tweet:")
print(f.readline())
f.close()
f=open("test.txt","a")
u=input("Enter your Tweet:")
f.write(u)
f.close()
