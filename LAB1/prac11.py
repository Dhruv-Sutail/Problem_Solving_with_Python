# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 20:15:54 2019

@author: Admin
"""









import datetime
import calendar
td=datetime.date.today()
dob=datetime.date(2000,12,1)
print(str(((td-dob)//365))+"Years"+"\n"+"Calendar "+"\n"+calendar.month(dob.year,dob.month))

#Another Solution
import calendar
import datetime
b=(datetime.datetime.today())
v=(datetime.datetime(1975,12,19))
a=b-c
print(a)
print(calendar.month(1975,12))
