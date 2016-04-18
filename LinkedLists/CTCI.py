
from LinkedList import List, Link


def remove_duplicates(linked_list):
    """
    remove duplicates from linked_list
    """
    if not linked_list.is_empty():
        link_map = {}
        curr_link = linked_list.head
        prev_link = None
        
        while curr_link:
            if curr_link.value in link_map:
                prev_link.next = curr_link.next
            else:
                link_map [curr_link.value] = 1
                prev_link = curr_link
            curr_link = curr_link.next
            
    return linked_list

def find_kth_to_last(linked_list , k):
    """
   remove kth to last from linked_list 
    """
    if not linked_list.is_empty():
        if k > linked_list.get_length():
            k = k % linked_list.get_length()
        if k <= 0:
            return
        slow_ptr = linked_list.head
        fast_ptr = linked_list.head
        
        for loop in range(0, k):
            print ('loop')
            fast_ptr = fast_ptr.next
            
        while fast_ptr:
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next
        return slow_ptr.value
    
def partion_list_aroundX(linked_list, number):
    """
    partition linked_list around a value 
    """
    if not linked_list.is_empty():
        low_value_list = List()
        high_value_list = List()
        curr_link = linked_list.head
        
        while curr_link:
            if curr_link.value < number:
                low_value_list.add_link_last(curr_link.value)
            else:
                high_value_list.add_link_last(curr_link.value)
            curr_link = curr_link.next
            linked_list.del_link_front()
        high_curr_link = high_value_list.head  
          
        while high_curr_link:
            low_value_list.add_link_last(high_curr_link.value)
            high_curr_link = high_curr_link.next
        return low_value_list
    
def is_palindrome(linked_list):
    """
    check if linked_list is a palindrome
    """
    if not linked_list.is_empty():
        stack = []
        slow_ptr = linked_list.head
        fast_ptr = linked_list.head
        
        while fast_ptr.next and fast_ptr.next.next:
            stack.append(slow_ptr.value)
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
            
        if fast_ptr.next:
            stack.append(slow_ptr.value)
        slow_ptr = slow_ptr.next
        
        while slow_ptr:
            value1 = stack.pop()
            value2 = slow_ptr.value
            if value1 != value2:
                return False
            slow_ptr = slow_ptr.next
        if stack:
            return False
        return True
    
def is_cyclic(linked_list):
    """
    check if linked_list is cyclic
    """
    if not linked_list.is_empty():
        slow_ptr = linked_list.head
        fast_ptr = linked_list.head
        
        while fast_ptr.next and fast_ptr.next.next:
            if slow_ptr.value == fast_ptr.value:
                break
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
            
        if not fast_ptr.next or not fast_ptr.next.next:
            return False #list is not cyclic
        
        slow_ptr = linked_list.head
        while slow_ptr.value != fast_ptr.value:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next
        return slow_ptr.value

def add_integers(linked_list1 , linked_list2):
    """
    add two numbers represented by linked_list
    """
    if linked_list1.is_empty():
        return linked_list2
    if linked_list2.is_empty():
        return linked_list1
    
    ans_list = List()
    carry = 0
    sum_value = 0
    
    curr_link1 = linked_list1.head
    curr_link2 = linked_list2.head
    
    while curr_link1 and curr_link2:
        sum_value = carry + curr_link1.value +  curr_link2.value
        carry = 0
        if sum_value >= 10:
            carry = sum_value//10
            sum_value = sum_value%10
        ans_list.add_link_last(sum_value)
        curr_link1 = curr_link1.next
        curr_link2 = curr_link2.next
        
    if curr_link1 or curr_link2:
        curr_link = curr_link1 if curr_link1 else curr_link2
        while curr_link:
            sum_value = carry + curr_link.value
            carry = 0
            if sum_value >= 10:
                carry = sum_value//10
                sum_value = sum_value%10
            ans_list.add_link_last(sum_value)
            curr_link = curr_link.next
            
    if carry > 0:
        ans_list.add_link_last(carry)
    return ans_list


        