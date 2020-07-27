#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module 03: Live Session Exercise: Exception Handling
Shannon Paylor
sep4hy
"""

#goal of this exercise is to write some code using try-except-finally blocks 
#that has the potential to throw a lot of types of errors
#need to figure out the appropriate order so that no "except" block is unreachable
#most specific errors before less specific

try:
    numer = float(input("Enter a numerator: ")) #will throw a ValueError if input is non-numeric
    denom = int(float(input("Enter a denominator: "))) #will throw an OverflowError (another ArithmeticError) if value is too large (like 8E+10000000) 
    quotient = numer / float(denom) #will throw a ZeroDivisionError if the denom is 0
    print(str(numer) + " / " + str(denom) + " = " + str(quotient))
    
    name = input("Enter the name of a file: ")
    file = open(name, 'r')  # will raise a FileNotFoundError if the file doesn't exist
    
    out_name = input("Enter where you'd like to write a file: ")
    with open(out_name, "wb") as f:
        print('Write file')
    #will throw an IsADirectoryError (a different kind of IOError) if out_name is a directory and not a file
    
    #code that could throw a different error
    golf_majors_won = {'Jack Nicklaus': 18, 'Tiger Woods': 15, 'Walter Hagen': 11, 'Ben Hogan': 9, 'Gary Player': 9, 
               'Tom Watson': 8, 'Arnold Palmer': 7, 'Lee Trevino': 6, 'Phil Mickelson': 5, 'Rory McIlroy': 4}

    golfer = input("Enter a golfer's name: ")
    print(golfer + " has won " + str(golf_majors_won[golfer]) + " majors.") 
    #will throw a key error if a name is entered that isn't in the dictionary
    
    #code that could throw a type error
    print(2 + "2")
    
except ZeroDivisionError:
    print("Please enter a non-zero denominator.")
    denom = int(input("Enter a denominator: "))
    quotient = numer / denom #will throw a ZeroDivisionError if the denom is 0
    print(str(numer) + " / " + str(denom) + " = " + str(quotient))
    
except ArithmeticError: #parent of ZeroDivisionError
    print("Whoa there, your numbers caused an arithmetic error. Let's try again.")
    numer = int(input("Enter a numerator: "))
    denom = int(input("Enter a denominator: "))
    quotient = numer / denom
    print(str(numer) + " / " + str(denom) + " = " + str(quotient))
    
except FileNotFoundError:
    print("Hmm, couldn't find that file. Let's try again.")
    name = input("Enter the name of a file: ")
    file = open(name, 'r')
    
except IOError: #parent of FileNotFoundError
    print("There was a problem with one of your files.")
    
except ValueError:
    print("Please make sure to enter a numeric value.")
    numer = int(input("Enter a numerator: "))
    denom = int(input("Enter a denominator: "))
    quotient = numer / denom
    print(str(numer) + " / " + str(denom) + " = " + str(quotient))
    
except TypeError:
    print("Oops. TypeError encountered. Continuing with remaining execution.")
    
except Exception:
    print("Uh-oh. You've reached an error this program hasn't handled. You might need to fix the code.")
    
finally:
    print("Phew! Finally reached the finally block.")