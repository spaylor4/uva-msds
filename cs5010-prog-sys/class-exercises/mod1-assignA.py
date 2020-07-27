#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
In-Class Assignment 1: Python
Shannon Paylor
sep4hy
"""
import sys

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


users_dict = dict()
for i in range(4):
    new_user = getUserInfo()
    users_dict.update(new_user)

original = sys.stdout

# Redirect stdout (by default it goes to the screen) to the file
sys.stdout = open('inClassAssign1Output.txt', 'a')

print(users_dict)

sys.stdout = original