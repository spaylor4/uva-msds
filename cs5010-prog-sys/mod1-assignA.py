#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 09:28:54 2020

@author: shannon
"""


def getUserInfo():
    fname = input("Please type your first name: ")
    lname = input("Please type your last name: ")
    age = input("Please type your age: ")
    
    fname = fname.strip()
    lname = lname.strip()
    age = int(age.strip())
    
    full_name = lname + "-" + fname
    user_dict = {full_name: age}
    return user_dict



for i in range(4):
    print(i)

