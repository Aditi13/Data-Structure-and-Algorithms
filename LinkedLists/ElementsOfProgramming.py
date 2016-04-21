'''
Created on Apr 16, 2016

@author: Aditi
''' 

from LinkedList import  List


def merge_sorted_linkedlists(linked_list1 , linked_list2):
    """
    @param: two sorted linked lists
    @return: merged linkedlist
    T(n) = linear, Space complexity = 1
    """
    merged_list = List()
    curr_link1 = linked_list1.head
    curr_link2 = linked_list2.head
    while curr_link1 and curr_link2:
        if curr_link1.value < curr_link2.value:
            merged_list.add_link_last(curr_link1.value)
            curr_link1 = curr_link1.next
            linked_list1.del_link_front()
        else:
            merged_list.add_link_last(curr_link2.value)
            curr_link2 = curr_link2.next
            linked_list1.del_link_front()
    if curr_link1:
        while curr_link1:
            merged_list.add_link_last(curr_link1.value)
            curr_link1 = curr_link1.next
    elif curr_link2:
        while curr_link2:
            merged_list.add_link_last(curr_link2.value)
            curr_link2 = curr_link2.next
    return merged_list

def reverse_linkedlist(linked_list):
    """
    @param: linked_list
    @return:reversed LinkedList 
    T(n) = linear, Space complexity = 1
    """
    if linked_list.is_empty() or linked_list.get_length() == 1:
        return linked_list
    curr_link = linked_list.head
    prev_link = None
    while curr_link:
        next_link = curr_link.next
        curr_link.next = prev_link
        prev_link = curr_link 
        curr_link = next_link
    linked_list.head = prev_link
    
def reverse_sublist(linked_list , value1 , value2):
    """
    @param linked_list: linked_list
    @param value1, value2: reverse sublist between value1 and value 2
    index starts at 1  
    T(n) = linear, Space complexity = 1
    """
    if linked_list.is_empty() or linked_list.get_length() == 1:
        return linked_list
    elif  value1 > linked_list.get_length() or value2 > linked_list.get_length():
        return linked_list
    else:
        diff = abs(value1-value2)
        value1_link = linked_list.head
        for loop in range(1,value1):
            start_reverse_link = value1_link
            value1_link = value1_link.next
        prev = start_reverse_link.next 
        prev_link = None
        while diff>-1:
            next_link = value1_link.next
            value1_link.next = prev_link
            prev_link = value1_link
            value1_link = next_link
            diff -= 1
        start_reverse_link.next = prev_link
        prev.next = next_link
    return linked_list

def delete_node(linked_list, value):
    if not linked_list.is_empty():
        curr_link = linked_list.head
        node_found = False
        while curr_link:
            if curr_link.value == value:
                node_found = True
                break
            prev_link = curr_link
            curr_link = curr_link.next
        if not node_found:
            return False
        elif not curr_link.next:
            linked_list.del_link_last()
        elif not prev_link:
            linked_list.del_link_front()
        else:
            prev_link.value = curr_link.value
            prev_link.next = curr_link.next
        return True
    

    
            

        
        
        
            
        