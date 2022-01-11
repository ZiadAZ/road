# -*- coding: utf-8 -*-
"""
Ask how many people the user wants to invite to a party.
If they enter a number below10, 
ask for the names and after each name display “[name] has been invited”. 
If they enter a number which is 10 or higher, display the message “Too many people”. 
Upload program to GitHub and write the link?
"""

def enter(msg='How many people the user wants to invite?'):
   print(msg)
   x= input()
   if(x.isnumeric()):
       x=int(x)
       if x<10:
         names=[]
         while x>0:
             x-=1
             print('enter name '+str(len(names)+1))
             names.append(input())
         return names
       
       else:
           return enter(' ““Too many people”')
   else:
       return enter('Erorr!  Enter a number corectly: ')


def start():

  for name in enter():
      print(name+' has been invited')


   

   
start()