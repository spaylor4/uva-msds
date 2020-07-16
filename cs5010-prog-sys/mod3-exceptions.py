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
    #some code
except ZeroDivisionError:
    
except ArithmeticError: #parent of ZeroDivisionError
    
except FileNotFoundError:
    
except IOError: #parent of FileNotFoundError
    
except ValueError:
    
except TypeError:
    
except Exception:
    
finally: