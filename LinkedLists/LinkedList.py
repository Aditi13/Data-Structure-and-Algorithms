class Link:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class List:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def is_empty(self):
        return not self.head
    
    def get_length(self):
        length =  0
        if not self.is_empty():
            curr = self.head
            while curr:
                curr = curr.next
                length +=1
            return length
        return length
    
    def print_list (self):
        if not self.is_empty():
            curr = self.head
            while curr:
                print(curr.value,'-->', end = '')
                curr = curr.next
        else:
            print ('List empty')
            
    def add_link_front(self, value):
        new_link = Link(value)
        if self.is_empty():
            self.head = new_link
            self.tail = new_link
        else:
            new_link.next = self.head
            self.head = new_link
            
    def add_link_last(self, value):
        new_link = Link(value)
        if self.is_empty():
            self.head = new_link
            self.tail = new_link
        else:
            self.tail.next = new_link
            self.tail = new_link
            
    def add_link_middle(self, value):
        new_link = Link(value)
        if self.is_empty():
            self.tail = new_link
            self.head = new_link
        else:
            slow_ptr = self.head
            fast_ptr = self.head
            while fast_ptr.next and fast_ptr.next.next:
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
            new_link.next = slow_ptr.next
            slow_ptr.next = new_link
            
    def del_link_front(self):
        if self.is_empty():
            return
        elif self.get_length()==1:
            link_value = self.head.value
            self.head = None
            self.tail = None
        else:
            link_value = self.head.value
            self.head = self.head.next
        return link_value
    
    def del_link_last(self):
        if self.is_empty():
            return
        elif self.get_length() == 1:
            link_value = self.head
            self.head = None
            self.tail = None
        else:
            curr = self.head
            prev = self.head
            while curr.next:
                prev = curr
                curr = curr.next
            link_value = curr.value
            prev.next = None
        return link_value
    
    def del_link_middle(self):
        if self.is_empty():
            return
        elif self.get_length() == 1:
            link_value = self.head.value
            self.head = None
            self.tail = None
        else:
            slow_ptr = self.head
            fast_ptr = self.head
            while fast_ptr.next and fast_ptr.next.next:
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
            link_value = slow_ptr.value
            slow_ptr.value = slow_ptr.next.value
            slow_ptr.next = slow_ptr.next.next
        return link_value

    
          

