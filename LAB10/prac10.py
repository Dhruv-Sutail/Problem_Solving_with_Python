# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 21:18:11 2020

@author: Silverxenfx
"""


import sqlite3
db=sqlite3.connect(':memory:')
db=sqlite3.connect('C:/Users/Admin/Desktop/pythonprac/p10') #Path where You want create Database with DataBase p10
string=db.cursor()
string.execute('''create table student1(sid varchar(10),name varchar(100),C_no varchar(10),Status varchar(100))''')
def insert(sid,name,con,sta):
    string.execute('''insert into student1 values(?,?,?,?)''',(sid,name,con,sta))
    db.commit()
    print('Entry Executed....')
def update(Name,sta):
    string.execute('''update student1 set Status=? where name=?''',(name,sta))
    db.commit()
    print('Entry Updated...')
def dup():
    string.execute('''delete from student1 where name='''),('John')
    db.commit()
    print('Duplicate Entry Removed....')
def pri():
    string.execute('''select * from student1''')
    show1=string.fetchall()
    for i in show1:
        print(i)

while True:
    print("DataBase Entries:")
    print('Enter 1 for Inserting Data')
    print('Enter 2 for Updating Data')
    print('Enter 3 for Duplicate Data')
    print('Enter 4 for Showing Data')
    print('Enter 5 For Exit')
    a=int(input("Enter Your Choice:"))
    if(a==1):
        sid=input("Enter Student Id:")
        name=input("Enter Name:")
        con=input("Enter Contact Number:")
        sta=input("Enter Status:")
        insert(sid,name,con,sta)
    elif(a==2):
        name=input('Enter Name where you want to change the Status:')
        sta=input('Enter Status:')
        update(name,sta)
    elif(a==3):
        dup()
    elif(a==4):
        pri()
    else:
        break
db.commit()
