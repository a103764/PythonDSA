# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 12:55:01 2025

@author: A103764
"""

# %% Binary Search
# 4, 6, 9, 13, 14, 18, 21, 24, 38

def BinarySearch(arr, start, end, key):
    
    # stops when start, end points at key
    while start <= end:
        
        mid = start + round((end - start) / 2)
         
        if arr[mid] == key:
            return mid

        elif arr[mid] > key:
            end = mid - 1
            
        else:
            start = mid + 1
            
    return -1
            
            
            
arr = [4, 6, 9, 13, 14, 18, 21, 24, 38]
ans = BinarySearch(arr, 0, len(arr) - 1, 40)

# %% Merge sort
def Merge(firstsublist, secondsublist):
    
    i = j = 0
    mergedList = []
    
    while i < len(firstsublist) and j < len(secondsublist):
        
        # add the smallest one first
        if firstsublist[i] < secondsublist[j]:
            mergedList.append(firstsublist[i])
            i = i + 1
        else:
            mergedList.append(secondsublist[j])
            j = j + 1
            
            
    # incase, len(sublists) are different: if i or j did not iterate
    # full list yet
    while i < len(firstsublist):
        mergedList.append(firstsublist[i])
        i = i + 1
        
    while j < len(secondsublist):
        mergedList.append(secondsublist[j])
        j = j + 1
            
    return mergedList    
    
    
def MergeSort(unsortedlist):
    
    if len(unsortedlist) == 1: 
        return unsortedlist
    
    midpoint = int(len(unsortedlist)/2) 
    firsthalf = unsortedlist[:midpoint]
    secondhalf = unsortedlist[midpoint:]
    
    print("firsthalf ", firsthalf)
    print("secondhalf ", secondhalf)
    
    half_a = MergeSort(firsthalf)
    half_b = MergeSort(secondhalf)
    
    return Merge(half_a, half_b)
    

arr = [11, 12, 7, 41, 61, 13, 16, 14]
MergeSort(arr)

    
# %% Fibonacci 

def dyna_fib(n): 
    
    if n == 0 :
        return 1
    
    if n == 1:
        return 1 
    
    # check if already calculaed
    if lookup[n] is not None :
        return lookup[n]
        
    # fib(4) = fib(3) + fib(2)    
    lookup[n] = dyna_fib(n-1) + dyna_fib(n-2)
    
    return lookup[n]


# declare emptry array
lookup = [None] * 10

for i in range(6):
    print(dyna_fib(i))

 
# %% 



    
    
    
    
    
            
        