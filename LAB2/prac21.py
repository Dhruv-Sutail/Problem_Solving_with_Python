# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 11:47:31 2019

@author: Admin
"""


user=eval(input("Enter Ammount"))
user=user*100
dollars=user//100
r=user%100


qua=r//25
r=r%25

dimes=r//10
r=r%10

nickels=r//5
cents=r%5
print("AMOUNT Dollars "+str(dollars)+"\nQuards :"+str(qua)+"\nDimes "+str(dimes)+"\nNickels "+str(nickels)+"\nCents "+str(cents))