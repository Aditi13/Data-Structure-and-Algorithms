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
    def get_min(self):
        if not self.isEmpty():
            return self.Heap[0]
    def compare_swap(self, parent_index, child_index):
        if self.Heap[parent_index] > self.Heap[child_index]:
            self.Heap[parent_index] , self.Heap[child_index] = self.Heap[child_index] , self.Heap[parent_index] 
    def percolate_up(self, index):
        while True:
            if index%2 == 0:
                parent_index = (index-2)//2
            else:
                parent_index = (index-1)//2
            if parent_index < 0 :
                break
            self.compare_swap(parent_index, index)
            index = parent_index
    def get_min_child(self, index):
        left_child = index*2 + 1
        right_child = index*2 + 2
        if right_child >= self.size:
            if self.Heap[left_child] < self.Heap[index]:
                return left_child
            else:
                return -1
        if self.Heap[left_child] < self.Heap[right_child]:
            return left_child
        else:
            return right_child
     
    def percolate_down(self, index):
        if self.isEmpty() or self.size== 1:
            return
        while index*2 + 1 < self.size:
            min_child_index = self.get_min_child(index)
            if min_child_index == -1:
                break
            self.Heap[min_child_index] , self.Heap[index] = self.Heap[index] , self.Heap[min_child_index]
            index = min_child_index
    def insert(self, value):
        self.Heap.append(value)
        self.size+=1
        self.percolate_up(self.size - 1) 
    def delete(self):
        if not self.isEmpty():
            val = self.Heap[0]
            self.Heap[0] = self.Heap[-1]
            self.Heap.pop()
            self.size -= 1
            self.percolate_down(0)
            return val
    def printHeap(self):
        if not self.isEmpty():
            for node in self.Heap:
                print (node, ' ' ,end = '')


