from turtle import right


class BinarySearchTreeNode():
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 
    
    def add_child(self, data):
        if data == self.data: #if the data's value already exists
            return 
        if data < self.data: #if the data doesn't exist...
            #add data in left subtree
            if self.left:
                self.left.add_child(data) 
            else:
                self.left = BinarySearchTreeNode(data) 
            #add data in right subtree
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data) 

        def find_min(self):
            if self.left is None:
                return self.data 

            return self.left.find_min() 

    def find_max(self):
        if self.right is None:
            return self.data 

        return self.right.find_max() 

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0 

        return self.data + left_sum + right_sum

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal() 
        
        if self.right:
            elements += self.right.post_order_traversal()
        
        elements.append(self.data)

        return elements 

    def pre_order_traversal(self):
        elements = [] 

        if self.left:
            elements += self.left.pre_order_traversal()

        
        if self.right:
            elements += self.right.pre_order_traversal()
        
        return elements 

    
    def in_order_traversal(self):
        elements = [] 

        #visis left tree 1st
        if self.left:
            elements += self.left.in_order_traversal()
        
        #visit base node
        elements.append(self.data)

        #visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):
        if self.data == val:
            return True 
        
        if val < self.data:
            # val might be in left subtree
            if self.left:
                return self.left.search(val) 
            else:
                return False 
        if val > self.data:
            #val might be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False 

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i]) 
    
    return root 

numbers = [17, 4, 1, 20, 9, 23, 18, 34]
numbers_bst = build_tree(numbers) 
print(numbers_bst.in_order_traversal())  

print(numbers_bst.calculate_sum()) 

class BST():
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 

    def add_child(self, data):
        if data == self.data:
            return 
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BST(data) 

    def Search(self, val):
        if self.data == val:
            return True 
        
        if val < self.data:
            if self.left:
                return self.left.Search(val)
            else:
                return False 
        
        if val > self.data:
            if self.right:
                return self.right.Search(val)
            else:
                return False 
    
    def find_min(self):
        if self.left is None:
            return self.data 

        return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data 
        
        return self.right.find_max()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0 

        return self.data + left_sum + right_sum 

    def PostTraversal(self):
        elements = []

        if self.left:
            elements += self.left.PostTraversal()
        
        if self.right:
            elements += self.right.PostTraversal()
        
        elements.append(self.data)

        return elements
    
    def PreTraversal(self):
        elements = []

        if self.left:
            elements += self.left.PreTraversal()
        
        if self.right:
            elements += self.right.PreTraversal()
        
        return elements
    
    def InOrderTraversal(self):
        elements = []

        if self.left:
            elements += self.left.InOrderTraversal()
        
        elements.append(self.data)

        if self.right:
            elements += self.right.InOrderTraversal()
        
        return elements
    
    def build_tree(elements):
        root = BST(elements[0])

        for i in range(1, len(elements)):
            root.add_child(elements[i])
        
        return root 
            