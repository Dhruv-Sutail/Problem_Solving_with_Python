# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 19:22:49 2020

@author: Admin
"""
import sys
def NO():
  print("NO")
  sys.exit()

n,m=input("enter number the Rows and Columns").split(" ")
n=int(n)
m=int(m)
lis1=list()
lis2=list()


for i in range(n):
    lis1.append([int(input("Enter integers")) for j in range(m)])
for i in lis1:
  for j in i:
    if(j==0 or j==1):
      pass
    else:
     NO()

print("YES")

















