'''
Created on Apr 18, 2016

@author: Aditi
'''

def binary_search(arr, value):
    """
    iterative implementation of binary search
    """
    if not arr:
        return 
    low_index = 0
    high_index = len(arr)-1
    while low_index <= high_index:
        mid_index = low_index + (high_index - low_index)//2
        if arr[mid_index] == value:
            return mid_index
        elif value < arr[mid_index]:
            high_index = mid_index - 1
        else:
            low_index = mid_index + 1
    return -1

def search_sorted_rotated(arr , value):
    """
    binary search in sorted rotated arr
    """
    low_index = 0
    high_index = len(arr)-1
    while low_index <= high_index:
        mid_index = low_index + (high_index - low_index)//2
        if arr[mid_index] == value:
            return mid_index
        elif arr[low_index] <= arr[mid_index]:
            if arr[low_index] <= value < arr[mid_index]:
                high_index = mid_index - 1
            else:
                low_index = mid_index + 1
        else:
            if arr[mid_index] < value <= arr[high_index]:
                low_index = mid_index + 1
            else:
                high_index = mid_index - 1
    return -1 

def first_occurance(arr, key):
    """
    find the first occurance of key in sorted arr
    """
    low_index = 0
    high_index = len(arr) - 1
    while low_index <= high_index:
        mid_index = low_index + (high_index - low_index)//2      
        if arr[mid_index] >= key:
            high_index = mid_index - 1
        else:
            low_index = mid_index + 1
    if arr[low_index] == key:
        return low_index
    return -1

def last_occurance (arr, key):
    """
    find the last occurance of key in sorted arr
    """
    low_index = 0
    high_index = len(arr) - 1
    while low_index <= high_index:
        mid_index = low_index + (high_index - low_index)//2
        if arr[mid_index]<= key:
            low_index = mid_index + 1
        else:
            high_index = mid_index - 1
    if arr[high_index] == key:
        return high_index
    return -1
        

def count_occurances(arr, key):
    """
    In a million sorted numbers, count occurances of key
    """  
    ind_first_occurance = first_occurance(arr, key)
    ind_last_occurance  = last_occurance(arr, key)
    return ind_last_occurance - ind_first_occurance + 1


    


