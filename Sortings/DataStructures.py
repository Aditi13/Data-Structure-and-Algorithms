'''
Created on Apr 21, 2016

@author: Aditi
'''

def merge_sort(arr):
    """
    merge sort - O (nlogn)
    stable sort , divide n conquer , 0(n) space
    """
    if len(arr) > 1:
        mid_index = len(arr)//2
        left_arr = arr[:mid_index]
        right_arr = arr[mid_index:]
        merge_sort(left_arr)
        merge_sort(right_arr)        
        i = 0 
        j = 0
        k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr [j]
                j += 1
            k += 1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
        return arr

def counting_sort(arr, k):
    """
    linear sort - runs in 0(n) time 
    the input should be in range 0-->k
    """
    count_arr = [0 for elm in range(k+1)]
    output_arr = [0 for elm in range(len(arr))]
    
    for ind in range(0, len(arr)):
        count_arr [arr[ind]] += 1
    
    for ind in range(len(count_arr)-1):
        count_arr[ind+1] += count_arr[ind]
        
    for ind in range(len(arr)):
        val = count_arr [ arr[ind]] - 1
        output_arr[val] = arr[ind]
        count_arr [ arr[ind]] -= 1
    
    return output_arr

    