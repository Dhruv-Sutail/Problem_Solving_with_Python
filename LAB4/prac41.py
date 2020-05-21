# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 11:44:56 2020

@author: Silverxenfx
"""
import uuid
import os
os.system('cls||clear')
l=[]
m=[]

def user():
    id1=str(uuid.uuid1())
    m.append(id1[:8])

    name=input("Enter the name: ")
    name=name.upper()
    name=str1(name)             #name of user
    m.append(name)
    os.system('cls||clear')
    lastname=input("Enter the lastname: ")
    lastname=lastname.upper()
    lastname=str1(lastname)             #last name of user
    m.append(lastname)
    os.system('cls||clear')

    Age=(input("Enter the your age: "))
    Age=age(Age)
    print(Age)

    m.append(Age)
    #os.system('cls||clear')
    sch=schme(Age)
    m.append(sch)
    #os.system('cls||clear')



    con=input("Enter the contact number: ")
    con=cont(con)                            #Contact number
    m.append(con)
    os.system('cls||clear')

    pin=input("Enter the pincode: ")
    pin=pincode(pin)                        #pincode
    m.append(pin)
    os.system('cls||clear')
    address=input("Enter the address: ")
    address=address.upper()
    m.append(address)
    os.system('cls||clear')

    l.append(m)
    print(str("Your UserID: "+id1[:8]))

def str1(strin):                        #validation of name /last name
    if(strin.isalpha()==False):
        strin=input("Enter name again: ")
        strin.upper()
        str1(strin)
    else:

        return strin


def cont(cont1):                          #validation of contact number
    if(len(cont1)!=10):
        cont1=input("Enter contact number: ")
        cont(cont1)

    elif(cont1.isnumeric()==False):
        cont1=input("Enter contact number: ")
        cont(cont1)
    else:
        return cont1


def pincode(pint):                         #validation of Pincode
    if(len(pint)!=6):
        pint=input("Enter the pincode: ")
        pincode(pint)
    elif(pint.isnumeric()==False):
         pint=input("Enter the pincode: ")
         pincode(pint)
    else:
        return pint


def age(age1):
    if(age1.isdigit()==True  and int(age1)<=100):
        print("Tari umar che : ",age1)
        return(age1)
    else:
        age1=input("Enter the Correct age: ")
        print(type(age1))
        return age(age1)




def schme(age1):
    print(age1)

    if(0<=int(age1)<=12):

        print("01.$100 deposit and   discount upto 10%in school fees")
        print("02.$150 deposit and   discount upto 20%in school fees" )
        print("99.for no schems")
        sch=input("enter the schme number: ")

    elif(13<=int(age1)<=26):

        print("11.$100 deposit and   discount upto 10%in higher school fees")
        print("12.$150 deposit and   discount upto 20%in higher school fees" )
        print("99.for no schems")
        sch=input("enter the schme number: ")
    else:

        print("21.$100 deposit and   discount upto 10% in House loans")
        print("22.$150 deposit and   discount upto 20%in House loans" )
        print("99.for no schems")
        sch=input("enter the schme number: ")

    if(sch=="01"):
        return "discount upto 10%in school fees"
    elif(sch=="02"):
        return "discount upto 20%in school fees"
    elif(sch=="11"):
        return "discount upto 20%in higher school fees"
    elif(sch=="12"):
        return "discount upto 20%in higher school fees"
    elif(sch=="21"):
        return "discount upto 20%in House Loans "
    elif(sch=="22"):
        return "discount upto 20%in House Loans"
    elif(sch=="99"):
        return "No Scheme"
    else:
        return "No Scheme"




def display(uid):
    print("-----------------------------------------------------")
    u=["userID","First name","Last name","Age","Scheme","Contact number","Pincode","Address"]
    for i in l:
        if(i[0]==uid):
            for k,j in zip(u,i):
                print(k+": "+str(j))
        else:
            print("\n\n\n\nUserID Doesnot matched\n\n\n\n")





#os.system('cls||clear')
while True:

    print("-----------------------------------------------------")
    print("1.Create a new Account:")
    print("2.View your Profile:")
    print("3.Exit")
    id1=input("Enter your Choice: ")
    if(id1=="1"):
        os.system('cls||clear')
        user()
    elif(id1=="2"):
        os.system('cls||clear')
        id2=input("Enter your UserID: ")
        display(id2)
    elif(id1=="3"):
        break
    else:
        os.system('cls||clear')
        print("Incorrect value  Returning to Main Menu:\n")
























