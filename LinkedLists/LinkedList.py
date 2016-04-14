class Link:
    def __init__(self,value):
        self.value = value
        self.next = None
class List:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return not self.head
    def addNodeFront(self,newValue):
        newLink  = Link (newValue)
        if self.isEmpty():
            self.head = newLink
            self.tail = newLink
        else:
            newLink.next = self.head
            self.head = newLink
    def addNodeLast(self,newValue):
        newLink = Link (newValue)
        if self.isEmpty():
            self.head = newLink
            self.tail = newLink
        else:
            self.tail.next = newLink
            self.tail = newLink
    def printList(self):
        if not self.isEmpty():
            currLink = self.head
            while currLink:
                print (currLink.value , '--> ' , end ='')
                currLink = currLink.next
        
        
        