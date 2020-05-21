# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 15:20:02 2020

@author: Admin
"""

    
    
             

az=set("abcdefghijklmnopqrstuvwxyz")
getstr=input("Enter the String")
getstr=getstr.replace(" ","")
if((len(az)-len(set(getstr)))==0):
    print("The String is Pangrams")
else:
    print("The String is Not Pangrams" )
    

    

    