#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 13:16:53 2020

@author: shannon
"""

# guessing game example

answer = "Watson"
print("Here is a guessing game. You get three tries.")
print("What is the name of the computer that played on Jeopardy?")
# response = input()
response = input()
if response == answer:
   print("That is right!")
else:
   response = input("Sorry. Guess again: ")
   if response == answer:
      print("That is right!")
   else:
      response = input("Sorry. One more guess: ")
      if response == answer:
         print("That is right!")
      else:
         print("Sorry. No more guesses. The answer is " + answer + ".")
         
         
# my gre-write of the uessing game example with a while loop
try_num = 1
while try_num < 4:
    response = input("Enter your guess: ")
    if response == answer:
        print("That is right!")
        break
    else:
        print("Sorry, that is incorrect.")
    try_num += 1
    
if try_num == 4:
    print("Sorry. No more guesses. The answer is " + answer + ".")
