'''
Created on Apr 21, 2016

@author: Aditi
'''

def intersection_arrays(arr1, arr2):
    ptr1 = 0
    ptr2 = 0
    output = []
    while ptr1 < len(arr1) and ptr2 < len(arr2):
        if arr1[ptr1] == arr2[ptr2] and (ptr1==0 or arr1[ptr1] != arr1[ptr1-1]):
            output.append(arr1[ptr1])
            ptr1 += 1
            ptr2 += 1
        elif arr1[ptr1] < arr2[ptr2]:
            ptr1+=1
        else:
            ptr2 += 1
    return output


def merge_sorted_arrays(arr1, arr2, ptr1):
    last_index = len(arr1) - 1
    ptr2 = len(arr2) - 1
    while ptr1 >=0 and ptr2 >= 0:
        if arr1[ptr1] > arr2[ptr2]:
            arr1[last_index] = arr1[ptr1]
            ptr1 -= 1
        else:
            arr1[last_index] = arr2[ptr2]
            ptr2 -= 1
        last_index -= 1
    while ptr2 >= 0:
        arr1[last_index] = arr2[ptr2]
        ptr2-=1
    return arr1

def char_length_encoding(input_string):
    s = sorted(list(input_string))
    output = []
    count = 1
    for index in range(0,len(s)-1):
        if s[index] == s[index+1]:
            count+=1
        else:
            output.append(s[index])
            output.append(str(count))
            count = 1
    output.append(s[index+1])
    output.append(str(count))
    return "".join(output)


        
    

    