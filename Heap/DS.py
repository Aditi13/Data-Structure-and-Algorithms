'''
Created on Apr 30, 2016

@author: Aditi
'''

class MinHeap:
    def __init__(self):
        self.Heap = []
        self.size = 0
    def isEmpty(self):
        return self.size == 0
    def percolate_down(self):
        pass
    def compare_swap(self, parent, child):
        if self.Heap[parent] > self.Heap[child]:
            self.Heap[parent] , self.Heap[child] = self.Heap[child] , self.Heap[parent]
    def percolate_up(self, index):
        while True:
            if index%2 == 0:
                parent_index = (index-2)//2
            else:
                parent_index = (index-1)//2
            if parent_index < 0 :
                break 
            self.compare_swap(parent_index,index) 
            index = parent_index
             
    def getMin(self):
        if not self.isEmpty():
            return self.Heap[0]
    def delete(self):
        if not self.isEmpty() :
            val = self.Heap[0]
            self.Heap[0] = self.Heap[-1]
            self.percolate_down()
            self.Heap.pop()
            self.size-=1
            return val
    def insert(self, value):
        self.Heap.append(value)
        self.size+=1
        self.percolate_up(self.size-1)
    def printHeap(self):
        if not self.isEmpty():
            for num in self.Heap:
                print (num , ' ')
h = MinHeap()
h.insert(13)
h.insert(5)
h.insert(27)
h.insert(9)
h.insert(0)
h.insert(-1)
h.insert(-100)
h.printHeap()
