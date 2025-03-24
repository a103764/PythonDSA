# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 13:17:26 2025

@author: A103764
"""

# check if element is in given list
def linearSearch(input_list, element):
    
    for index,value in enumerate(input_list):
        if value == element: 
            return index      
        
    return -1

input_list = [3, 4, 1, 6, 14]

ans = linearSearch(input_list, 6)




for i in range(5):
    
    for j in range(5):
        print("see how many print")
    break 