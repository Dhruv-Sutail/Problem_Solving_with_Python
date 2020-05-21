# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 11:03:00 2020
#if(((usery%4==0)and (usery%100!=0))or(usery%400==0)):
@author: Admin
"""


cur_offset=0
usery=int(input("Enter the year"))
userd=int(input("Enter the day number start from monday=0 "))
l=[31,28,31,30,31,30,31,31,30,31,30,31]
l2=[31,29,31,30,31,30,31,31,30,31,30,31]
month=["Jan","Feb","March","April","May","June","July","Aug","Sep","Oct","Nov","Dec"]
day=["MON","TUE","WED","THRU","FRI","SAT","SUN"]

for i in range(0,12):
    cur_offset=cur_offset+l[i]
    rem=cur_offset%7
    userd1=userd+rem
    print(month[i]+",1,"+str(usery)+" "+day[userd1%7])

