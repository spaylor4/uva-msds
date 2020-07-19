#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module 4 Exercise: Binary Search
Shannon Paylor
sep4hy
"""

import math

def getMid(start_ind, end_ind):
    spread = end_ind - start_ind
    mid = math.floor(spread/2)
    print(F"Mid is: {mid}")
    return mid

def binarySearch(item_list,target):
    search_min = 0
    search_max = len(item_list) - 1
    
    if len(item_list) == 0:
        return False #target can't be in an empty list
    
    while search_max >= search_min:
        mid = getMid(search_min, search_max)
        if target == item_list[mid]:
            return True #if target equals mid element, we can stop searching
        elif target < item_list[mid]:
            search_max = mid - 1 #search bottom half in next iteration
        else:
            search_min = mid + 1 #search top half in next iteration
    
    


item_list = [1, 2, 4, 6, 7, 9]

getMid(0, 0)
