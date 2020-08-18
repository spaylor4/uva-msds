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
    mid = math.floor(spread/2) + start_ind
    print(F"Mid is: {mid}")
    return mid

def binarySearch(item_list,target):
    #item_list must be sorted list
    search_min = 0
    search_max = len(item_list) - 1
    
    if len(item_list) == 0:
        return False #target can't be in an empty list
    
    while search_max > search_min:
        mid = getMid(search_min, search_max)
        if target == item_list[mid]:
            return True #if target equals mid element, we can stop searching
        elif target < item_list[mid]:
            search_max = mid - 1 #search bottom half in next iteration
        else:
            search_min = mid + 1 #search top half in next iteration
            
    #loop will terminate when search_min = search_max
    #need to check once more at that index
    mid = getMid(search_min, search_max)
    if target == item_list[mid]:
        return True
    else:
        return False  



#tests from assignment
list1 = [1,2,3,5,8]

print("Is 6 in " + str(list1) + "? " + str(binarySearch(list1, 6)))
print("Is 5 in " + str(list1) + "? " + str(binarySearch(list1, 5)))
print("Is 1 in " + str(list1) + "? " + str(binarySearch(list1, 1)))

#a couple more tests
list2 = [1, 2, 4, 6, 7, 9]

print("Is 6 in " + str(list2) + "? " + str(binarySearch(list2, 6)))
print("Is 3 in " + str(list2) + "? " + str(binarySearch(list2, 3)))

binarySearch([], 3) #double check that this returns False as expected

binarySearch(['a', 'c', 'd', 'x', 'z'], 'x') #works with letters too

binarySearch(['a', 'c', 'd', 'x', 'z'], 'b')


