# -*- coding: utf-8 -*-
"""
Ask the user to enter their first name and then display the length of their name.
 upload program file to GitHub and past the link.
"""

def enter(msg='Enter Your first name'):
   print(msg)
   return input()


def start():

 
  
   f=enter()
   print('Your name is: '+f+"\n and it's lenth is: "+str(len(f) ))
   

   
start()