'''
Created on Apr 20, 2016

@author: Aditi
'''
import sys
max_value = -sys.maxsize

class Tree():
    
    def __init__(self, root_value):
        self.left = None
        self.right = None
        self.root = root_value
        
    def insert_value(self, value):
        new_node = Tree(value)
        if value > self.root:
            if not self.right:
                self.right = new_node
            else:
                self.right.insert_value(value)
        else:
            if not self.left:
                self.left = new_node
            else:
                self.left.insert_value(value)
                
    def pre_order_traversal(self):
        print (self.root, ' ' , end = '')
        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()
            
    def post_order_traversal(self):
        if self.left:
            self.left.post_order_traversal()
        if self.right:
            self.right.post_order_traversal()
        print (self.root, ' ' , end = '')
        
    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print (self.root, ' ' , end = '')
        if self.right:
            self.right.inorder_traversal()
            
    def pre_order_interative(self):
        stack = [self]
        while stack:
            curr_node = stack.pop()
            print (curr_node.root, ' ' , end = '')
            if curr_node.right:
                stack.append(curr_node.right)
            if curr_node.left:
                stack.append(curr_node.left)
                
    def inorder_iterative(self):
        done = False
        stack = []
        curr_node = self
        while not done:
            if curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left
            else:
                if stack:
                    curr_node = stack.pop()
                    print (curr_node.root, ' ' ,end = '')
                    curr_node = curr_node.right
                else:
                    done = True
                    
    def post_order_iterative(self):
        stack = []
        curr_node = self
        set_value = set()
        while stack or curr_node:
            if curr_node:
                stack.append(curr_node)
                curr_node = curr_node.left
            else:
                curr_node = stack.pop()
                if curr_node.right and not curr_node.right in set_value:
                    stack.append(curr_node)
                    curr_node = curr_node.right
                else:
                    print (curr_node.root, ' ' , end = '')
                    set_value.add(curr_node)
                    curr_node = None
    
    def breadth_first_search(self):
        queue = [self]
        while queue:
            curr_node = queue.pop(0)
            print (curr_node.root , ' ',end = '')
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
    
    def find_max_element_recur(t, self):
        global max_value
        if not t:
            return max_value
        if t.root > max_value:
            max_value = t.root
        return self.find_max_element_recur(t.left) or self.find_max_element_recur(t.right)
    
    def find_max_element_iterative(self):
        queue = [self]
        max_value = -sys.maxsize
        while queue:
            curr_node = queue.pop(0)
            if curr_node.root > max_value:
                max_value = curr_node.root
            if curr_node.right:
                queue.append(curr_node.right)
            if curr_node.left:
                queue.append(curr_node.left)
        return max_value
    
    def get_size(self, t):
        if not t:
            return 0
        return self.get_size(t.left) + self.get_size(t.right) + 1
    
    def get_height(self, t):
        if not t:
            return 0
        return max(self.get_height(t.left), self.get_height(t.right) ) + 1
    
    def get_diameter(self, t):
        """
        print diameter of binary tree
        """
        if not t:
            return 0
        left_diam = self.get_diameter(t.left)
        right_diam = self.get_diameter(t.right)
        left_ht = self.get_height(t.left)
        right_ht = self.get_height(t.right)
        return max(max(left_diam , right_diam) , left_ht+right_ht+1)
    
    def level_order_traversal(self):
        """
        print nodes level wise/ BFS
        """
        level_queue = [self]
        next_level_queue = []
        curr_level = 0
        print (self.root)
        while level_queue:
            curr_node = level_queue.pop(0)
            if curr_node.left:
                next_level_queue.append(curr_node.left)
            if curr_node.right:
                next_level_queue.append(curr_node.right)
            if not level_queue:
                for nodes in next_level_queue:
                    print (nodes.root , ' ' , end = '')
                print ()
                curr_level += 1
                level_queue = next_level_queue[:]
                next_level_queue = []
    
    def find_level_maxsum (self):
        """
        find the level with max sum
        """
        level_queue = [self]
        next_level_queue = []
        curr_level = 0
        max_sum = -sys.maxsize
        while level_queue:
            curr_node = level_queue.pop(0)
            if curr_node.left:
                next_level_queue.append(curr_node.left)
            if curr_node.right:
                next_level_queue.append(curr_node.right)
            if not level_queue:
                sum_value = 0
                for nodes in next_level_queue:
                    sum_value += nodes.root
                if sum_value > max_sum:
                    max_sum = sum_value
                curr_level += 1
                level_queue = next_level_queue[:]
                next_level_queue = []
        if self.root> max_sum:
            max_sum = self.root
        return max_sum
    
    def reverse_level_order(self):
        """
        print reverse level order
        """
        stack = []
        queue = [self]
        while queue:
            curr_node = queue.pop(0)
            stack.append(curr_node.root)
            if curr_node.right:
                queue.append(curr_node.right)
            if curr_node.left:
                queue.append(curr_node.left)
        while stack:
            print (stack.pop(), '' , end= '')
    
    def is_identical(self, tree1, tree2):
        """
        check if two trees are structurally identical
        """
        if not tree1 and not tree2:
            return True
        elif tree1 and tree2:
            return (tree1.root == tree2.root and self.is_identical(tree1.left,tree2.left) and self.is_identical(tree1.right, tree2.right))
        else:
            return False
    
    def count_half_nodes(self):
        """
        count no of half nodes via level order traversal
        """
        queue = [self]
        half_nodes = 0
        half = False
        while queue:
            curr_node = queue.pop(0)
            if curr_node.left:
                queue.append(curr_node.left)
                half = not half
            if curr_node.right:
                queue.append(curr_node.right)
                half = not half
            if half:
                half_nodes += 1
                half = not half 
        return half_nodes
                
                

