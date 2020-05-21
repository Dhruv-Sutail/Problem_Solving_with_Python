# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 22:59:44 2020

@author: Silverxenfx
"""

from random import randint
count=0
l=list()
for i in range(int(input("Enter number of cages"))):
  l.append(randint(1,200))
print("Lions Room Number")
for i in l:
  if(l.count(i)==1):
    count+=1
    print(i,end=" ")
print("\nTotal Number Of Lion Room",count)
