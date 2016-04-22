'''
Created on Apr 21, 2016

@author: Aditi
'''
from locale import currency

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


def countint_votes(arr):
    sorted_arr = merge_sort(arr)
    max_votes = 0
    curr_count = 1
    curr_votes = 1
    for index in range(0,len(sorted_arr)-1):
        if sorted_arr[index] == sorted_arr[index+1]:
            curr_count += 1
            curr_votes += 1
        else:
            curr_count = 1
            curr_votes = 1
        if max_votes < curr_votes:
            max_votes = curr_votes
            winner = sorted_arr[index]
    return winner

def counting_sort_base(arr, n , exp):
    output = [0 for elm in range(len(arr))]
    count = [0 for elm in range(n+1)]
    
    for index in range(len(arr)):
        count[(arr[index]//exp)%n] += 1
    
    for index in range (1,len(count)):
        count[index] += count[index-1]
        
    for index in range(len(arr)):
        val = count[(arr[index]//exp)%n] - 1
        output [val] = arr[index]
        count[(arr[index]//exp)%n] -= 1
    return output
arr = [1,2,5,2]
arr =  (counting_sort_base(arr,5,1))
print ((counting_sort_base(arr,5,5)))
        

            
    

    