# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 22:35:36 2020

@author: Silverxenfx
"""

file1=input("Enter Source File:")
f=open(file1,"r")
file2=input("Enter Encryption File:")
fo=open(file2,"w")
text=f.read()
for i in text:
		a=chr(ord(i)+5)
		fo.write(a)
fo.close()
f.close()
f=open(file2,"r")
file3=input("Enter Decrypted File:")
fo=open(file3,"w")
text=f.read()
for i in text:
	a=chr(ord(i)-5)
	fo.write(a)

fo.close()
f.close()

