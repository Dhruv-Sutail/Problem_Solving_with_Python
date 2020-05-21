# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 21:02:29 2020

@author: Silverxenfx
"""



import sys
class excep(Exception):
    pass
class bank:
    def __init__(self,name,acctype):
        self.setbalance()
        self.name=name
        #self.__bal+=b
        self.__acctype=acctype
        print("Name of Customer is",self.name)
        print("Account Type is ",self.__acctype)
        self.menu()
    def setbalance(self):
            self.__bal=1000


    def menu(self):
            print("Enter 1 for Deposition")
            print("Enter 2 for Withdrawl")
            inp=int(input("Enter your Choice:"))
            if(inp==1):
                self.Deposit()
            elif(inp==2):
                self.withdrawl()


    def Deposit(self):
            self.dep=eval(input("Enter Amount to be Deposited:"))
            self.__bal=self.dep+int(self.__bal)
            print("Updated Amount is ",self.__bal)

    def withdrawl(self):
            self.wit=eval(input("Enter Amount to be Withdrawn:"))

            try:

                if(int(self.__bal)-self.wit<1000):
                    raise excep
            except excep:
                print("Withdrawl is Not Possible as Balance Goes Below 1000")

            else:
                self.__bal=int(self.__bal)-self.wit
                print("Remaining Amount is ",self.__bal)
    def Details(self):
      print("Name:",self.name)
      print("Account-Type",self.__acctype)
      print("Balance",self.__bal)


n=input("Enter Name:")

a=input("Current or Savings")
ob=bank(n,a)
ob.Details()