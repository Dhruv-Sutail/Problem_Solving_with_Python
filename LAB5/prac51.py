# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 17:02:48 2020

@author: Silverxenfx
"""
import random
l=["Ace",2,3,4,5,6,7,8,9,10,"Jack","King","Queen"]
rank=["Spade","Diamond","Heart","club"]
s=set()
count1=0
while len(s)!=4:
  count1+=1
  rl=random.choice(l)
  rr=random.choice(rank)
  print(str(rl)+" "+str(rr))
  s.add(rr)

print("\n\n\n In {} attempts it became successfull".format(count1 ))

