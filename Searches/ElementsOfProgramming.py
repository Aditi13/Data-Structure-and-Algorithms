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
    if low_index > len(arr)-1:
        return -1
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
    if high_index > len(arr)-1:
        return -1
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

def index_equalto_value(arr, key):
    """
    find index A[i]=i
    """
    low_index = 0 
    high_index = len(arr)-1
    while low_index <= high_index:
        mid_index = low_index + (high_index - low_index)//2
        if arr[mid_index] == mid_index:
            return mid_index
        elif arr[mid_index] < mid_index:
            low_index = mid_index + 1
        else:
            high_index = mid_index - 1
    return -1

def first_elem_greaterthan_k(arr, key):
    """
    find index of first element in arr greater than given key
    else return -1
    """
    low_index = 0
    high_index = len(arr) - 1
    while low_index <= high_index:
        mid_index = low_index + (high_index - low_index)//2
        if arr[mid_index] > key:
            high_index = mid_index - 1
        else:
            low_index = mid_index + 1
    if low_index > len(arr)-1:
        return -1
    if arr[low_index] > key:
        return low_index
    return -1

def smallest_elem_rotated_arr(arr):
    """
    find the smalles element in rotated arr
    """
    low_index = 0
    high_index = len(arr)-1
    while low_index <= high_index:
        mid_index = low_index + (high_index - low_index)//2
        if (arr[mid_index] > arr[high_index]):
            mid_index = low_index + 1
        else:
            high_index = mid_index
    return low_index


def largest_integar_lessthan_k(k):
    """
    return the largest number s, such that s^2 <= k
    """
    low_bound = 0
    high_bound = k
    while low_bound < high_bound:
        mid_value = low_bound + (high_bound - low_bound)//2
        mid_sq = mid_value * mid_value
        if mid_sq == k:
            return mid_sq
        elif mid_sq < k:
            low_bound = mid_value
        else:
            high_bound = mid_value - 1
        if high_bound * high_bound <= k:
            return high_bound
    return low_bound  

# k = 16
# print (largest_integar_lessthan_k(300))    


def search_k_2D (arr, key):
    """
    search for key in a 2D space
    """
    row_count = len(arr)
    col_count = len(arr[0])
    curr_row = 0
    curr_col = col_count -1
    while curr_col >= 0 and curr_row < row_count:
        elem = arr[curr_row][curr_col]
        if key == elem:
            return curr_row, curr_col
        if key >  elem:
            curr_row += 1
        else:
            curr_col -= 1
    return -1

          
          

    


