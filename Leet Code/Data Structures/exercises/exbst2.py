class BSTNode():
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 
    
    def __repr__(self):
        return f"{self.data}"
    
    def add_child(self, data):
        if data == self.data:
            return #
        
        if data < self.data: # add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BSTNode(data)
        else: #add data in right subtree
            if data > self.data:
                if self.right:
                    self.right.add_child(data)
                else:
                    self.right = BSTNode(data) 
    
    def find_min(self):
        if self.left is None:
            return self.data
        
        return self.left.find_min() 
    
    def find_max(self):
        if self.right is None:
            return self.data 
        
        return self.right.find_max() 

    def InorderTraversal(self):
        elements = []

        if self.left: #visit left subtree 1st
            elements += self.left.InorderTraversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.InorderTraversal()
        
        return elements 
    
    def PreorderTraversal(self):
        elements = []

        if self.left:
            elements += self.left.PreorderTraversal()
        
        if self.right:
            elements += self.right.PreorderTraversal()

        return elements 
    
    def PostorderTraversal(self):
        elements = []

        if self.left:
            elements += self.left.PostorderTraversal()

        if self.right:
            elements += self.right.PostorderTraversal()
        
        elements.append(self.data)

        return elements 

    def search(self, val):
        if self.data == val:
            return True 
        
        if val < self.data:
            if self.left:
                self.left.search(val)
            else:
                return False 
        
        if val > self.data:
            if self.right:
                self.right.search(val)
            else:
                return False 

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None 
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left 
            
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val) 

        return self 

def build_tree(elements):
    root = BSTNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i]) 
    
    return root 

numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34]) 
numbers_tree.delete(17)
print(numbers_tree.InorderTraversal()) 

class BST():
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 

    def __repr__(self):
        return f"{self.data}"
    
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
    
    def PostOrderTraversal(self):
        elements = []

        if self.left:
            elements += self.left.PostOrderTraversal()
        
        if self.right:
            elements += self.right.PostOrderTraversal()
        
        elements.append(self.data)

        return elements 

    def PreOrderTraversal(self):
        elements = []

        if self.left:
            elements += self.left.PreOrderTraversal()
        
        if self.right:
            elements += self.right.PreOrderTraversal()
        
        return elements


    def InOrderTraversal(self):
        elements = []

        if self.left:
            elements += self.left.InOrderTraversal()
        
        elements.append(self.data)

        if self.right:
            elements += self.right.InOrderTraversal()
        
        return elements

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
        

    
def build_tree(elements):
    root = BST(data=elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    
    return root 

numbers = [17, 4, 1, 20, 9, 23, 18, 34]
numbers_bst = build_tree(numbers) 
print(numbers_bst.InOrderTraversal())  

print(numbers_bst.calculate_sum()) 

