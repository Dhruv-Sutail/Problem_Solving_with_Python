# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 20:56:19 2020

@author: Silverxenfx
"""
def fun():


  try:

    filename=input("Enter Name of File with extention")
    with open (filename,"r") as file:
      characters=len(file.read().replace(" ",""))
      words=0
      file.seek(0)

      Lines=file.readlines()
      Lines=[x.strip() for x in Lines]
      #Lines.remove("")
      print(Lines)

      file.seek(0)

      for x in file:
        for word in x.split():
          words+=1



      print("No.Characters: ",characters)
      print("No.Words: ",words)
      print("No.Lines: ",len(Lines))
      file.close()

  except FileNotFoundError:

    print("File Not  Found, " )
    fun()
  except Exception as e:
    print(e)
    fun()

fun()



