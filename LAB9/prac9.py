# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 13:03:39 2020

@author: Silverxenfx
"""
class exc(Exception):
  pass
class book:


  __title=None
  __Author=None
  __type=None
  __format=None
  __track=None
  __page=None


  def _Ebook(self,title,Author,format_,pages):
    self.__title=title
    self.__Author=Author
    self.__format=format_
    self.__page=pages

  def _Audio(self,title,Author,format_,Track):
    self.__title=title
    self.__Author=Author
    self.__format=format_
    self.__track=Track
  def _DisEbook(obj):
    print("Title: ",obj.__title)
    print("Author: ",obj.__Author)
    print("Format: ",obj.__format)
    print("Pages: ",obj.__page)
  def _DisAudio(obj):

    print("Title: ",obj.__title)
    print("Author: ",obj.__Author)
    print("Format: ",obj.__format)
    print("Track Length : ",obj.__track)





class Ebook(book):
  __Efor=["PDF", "EPUB", "MOBI", "AZW"]

  def regisE(self):
    self.__title=input("Enter Book Title")
    self.__Author=input("Enter Author Name")
    self.__pages=input("Enter number of pages")
    try:
      self.__format=input("Enter the format")
      if(self.__format not in self.__Efor):
        raise exc
      else:

        book._Ebook(self,self.__title,self.__Author,self.__format,self.__pages)
        print("Registered Successfully")
    except exc:
      print("Invalid Format")

  def disE(self,obj):
     book._DisEbook(obj)







class Audio(book):

  __Afor=["MP3"," WMA", "WAV"]
  def regisA(self):
    self.__title=input("Enter Book Title")
    self.__Author=input("Enter Author Name")
    self.__track=input("Enter track length in minutes")
    try:
      self.__format=input("Enter the format")
      if(self.__format not in self.__Afor):
        raise exc
      else:

        book._Audio(self,self.__title,self.__Author,self.__format,self.__track)
        print("Registered Successfully")
    except exc:
      print("Invalid Format")
  def disA(self,obj):
    book._DisAudio(obj)



Ei=0
Ai=0
Eobj1=list()
Aobj1=list()


while(True):

  choice=input("Enter:\n1.Register Ebook\n2.Register Audio\n3.Display Ebook\n4.Display Audio\5.All Ebook\n6.All Audio\nEnter Choice: ")

  if(choice=="1"or choice=="Ebook" ):
    Eobj1.append(Ebook())
    Eobj1[Ei].regisE()
    Ei+=1




  elif(choice=="2"or choice=="Audio" ):
    Aobj1.append(Audio())
    Aobj1[Ai].regisA()
    Ai+=1



  elif(choice=="3"):

    try:
      intput=int(input("Enter book number"))
      if(intput >len(Eobj1)):
        raise exc
      else:
        temp=Ebook()

        temp.disE(Eobj1[intput-1])

    except exc:
      print("not such record exixt")


  elif(choice=="4"):

    try:
      intput=int(input("Enter book number"))
      if(intput >len(Aobj1)):
        raise exc
      else:
        temp=Audio()

        temp.disA(Aobj1[intput-1])
    except exc:
      print("not such record exixt")
  elif(choice=="5"):
    for i in Eobj1:
      temp=Ebook()
      temp.disE(i)
      print("----------------")
  elif(choice=="6"):
    try:
      if(not Aobj1):
        raise exc
      else:

        for i in Aobj1:

          temp=Audio()
          temp.disA(i)
          print("----------------")
    except exc:
        print("No Record")
  else:
     break














