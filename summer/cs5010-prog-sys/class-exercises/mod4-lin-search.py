#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module 4 Exercise: Sequential Search
Shannon Paylor
sep4hy
"""

def linearSearch(target,my_list):
    for i in range(len(my_list)):
        if target == my_list[i]:
            return i
        
    return -1

#example test from assignment
zoo = ['lion','tiger','elephant','zebra','bear']

print(linearSearch('tiger', zoo))
print(linearSearch('zebra', zoo))
print(linearSearch('panda', zoo))

#another test
myList = [2, 5, 'a', 'six', 3]

print(linearSearch(6, myList))
print(linearSearch('six', myList))

#another test
fruits = ['apple', 'banana', 'peach', 'watermelon']

print(linearSearch('peach', fruits))
print(linearSearch('blueberry', fruits))
