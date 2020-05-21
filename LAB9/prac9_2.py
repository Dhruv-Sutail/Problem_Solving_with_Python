# -*- coding: utf-8 -*-
"""
Created on Wed May 13 17:17:30 2020

@author: Silverxenfx
"""

s=[]
class stack:
    def __init__(self,s):
        self.h = s
    def push(self,v):
        if len(s) < self.h:
            s.append(v)
        else:
            print("stack over flow")
    def popv(self):
        if len(s) == 0:
            print("stack under flow")
        else:
            s.pop()
    def peep(self,i):
        if len(s) == 0:
            print("stack under flow")
        else:
            print(s[i])
    def change(self,i,v):
        if len(s) == 0:
            print("stack under flow")
        else:
            s[i] = v
    def dis(self):
        print(s)
sob = stack(4)
while True:
    print("enter 1 for push\nenter 2 for pop\nenter 3 for peep\nenter 4 for change\nenter 5 for display\nenter 6 for close")
    c=int(input(""))
    if c == 1:
        v = int(input("enter value to push"))
        sob.push(v)
    if c == 2:
        sob.popv()
    if c == 3:
        i = int(input("enter index to peep"))
        sob.peep(i)
    if c == 4:
        i = int(input("enter index to change"))
        v = int(input("enter value to change"))
        sob.change(i,v)
    if c == 5:
        sob.dis()
    if c == 6:
        sob.dis()
        break
