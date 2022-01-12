# -*- coding: utf-8 -*-
"""
Set the total to 0 to start with. While the total is 50 or less,
 ask the user to input a number. Add that number to the total and print the message
 “The total is… [total]”. Stop the loop when the total is over 50.
 Upload program to GitHub and past the link.
"""

def enter(msg='Enter a number: '):
   print(msg)
   x= input()
   if(x.isnumeric()):
       return x
   else:
       return enter('Erorr!  Enter a number corectly: ')
    


def start():

    

  total = 0
  while total<=50:
   total+=int(enter())
   print('The total is.. '+str(total))
   
   

   
start()