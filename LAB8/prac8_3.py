# -*- coding: utf-8 -*-
"""
Created on Wed May 13 17:03:10 2020

@author: Silverxenfx
"""

def menu():
    print("1) Add two complex numbers")
    print("2) Subtract two complex numbers")
    print("3) Multiply two complex numbers")
    print("4) Exit the Calculator")
    print(" ")
    return int(input("Choose your option: "))
class Calculator:
    def __init__(self,numberOne=None,numberTwo=None,i1=3):
        pass
    def gettheNumbers(self):
        print("Enter the real and imaginary part of the first number\n")
        self._r1=eval(input("Real part="))
        self._i1=eval(input("Imaginary part="))
        self._numberOne=complex(self._r1,self._i1)
        print(type(self._numberOne))
        print("Enter the real and imaginary part of the second number:=")
        self._r2=eval(input("Real part="))
        self._i2=eval(input("Imaginary part="))
        self._numberTwo=complex(self._r2,self._i2)
        print("The first complex number is =",self._numberOne)
        print("The second complex number is =",self._numberTwo)
    def add(self):
        a=(self._numberOne)+(self._numberTwo)
        print("The addition of two complex numbers is =",a)
    def sub(self):
        s=(self._numberOne)-(self._numberTwo)
        print("The subtraction of two complex numbers is =",s)
    def mul(self):
        m=(self._numberOne)*(self._numberTwo)
        reall=int(m.real)
        imagg=int(m.imag)
        if(imagg>0 or reall>0):
            print("The multiplication of two complex numbers is =",m)
        else:
            print("Multiplication of two numbers cannot be zero")
obj=Calculator()
obj.gettheNumbers()
loop = 1
choice = 0
while loop == 1:
    choice = menu()
    if choice == 1:
        obj.add()
    elif choice == 2:
        obj.sub()
    elif choice == 3:
        obj.mul()
    elif choice == 4:
        loop = 0

