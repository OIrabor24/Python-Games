class BinarySearchTreeNode():
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 
    
    def PrintData(self):
        print(self.data) 
    
    def add_child(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinarySearchTreeNode(data)
                else:
                    self.left.add_child(data) 
            
            elif data > self.data:
                if self.right is None:
                    self.right = BinarySearchTreeNode(data)
                else:
                    self.right.add_child(data) 
        else:
            self.data = data 

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree() 

    #Traverse Preorder
    def TraversePreOrder(self):
        print(self.data, end=' ')
        if self.left:
            self.left.TraversePreOrder()
        if self.right:
            self.right.TraversePreOrder() 
    
    #Traverse Inorder
    def TraverseInOrder(self):
        if self.left:
            self.left.TraverseInOrder()
        print(self.data, end=' ')
        if self.right:
            self.right.TraverseInOrder() 
    
    #Traverse Postorder
    def TraversePostOrder(self):
        if self.left:
            self.left.TraversePostOrder()
        if self.right:
            self.right.TraversePostOrder() 
        print(self.data, end=' ') 

    def Search(self, node_val):
        if self.data == node_val:
            return True 

        if node_val < self.data:
            #node_val might be in left subtree
            if self.left:
                return self.left.Search(node_val)
            else:
                return False 

        if node_val > self.data:
            #val might be in right subtree
            if self.right:
                return self.right.Search(node_val)
            else:
                return False 

root = BinarySearchTreeNode(27)
root.add_child(14)
root.add_child(35)
root.add_child(31)
root.add_child(10)
root.add_child(19)

root.PrintTree() 
node_val = root.Search(35) 

numbers = [17, 4, 1, 20, 9, 23, 18, 34]


class BinaryTree():
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 
    
    def PrintData(self):
        print(self.data) 
    
    def add_child(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryTree(data)
                else:
                    self.left.add_child(data)
            
            elif data > self.data:
                if self.right is None:
                    self.right = BinaryTree(data)
                else:
                    self.right.add_child(data)
        else:
            self.data = data 
        
    
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
            print(self.data)
        if self.right:
            self.right.PrintTree() 
    
    #Traverse Preorder: visit the root; traverse left, traverse right
    def TraversePreOrder(self): #self can be replaced with root
        print(self.data, end=' ')
        if self.left:
            self.left.TraversePreOrder()
        if self.right:
            self.right.TraversePreOrder() 
    
    #Traverse Inorder:traverse left, visit the root, traverse right
    def TraverseInOrder(self):
        if self.left:
            self.left.TraversePreOrder()
        print(self.data, end=' ')
        if self.right:
            self.right.TraversePreOrder() 

    #Traverse PostOrder: traverse left, traverse right, visit the root
    def TraversePostOrder(self):
        if self.left:
            self.left.TraversePostOrder()
        if self.right:
            self.right.TraversePostOrder()
        print(self.data, end=' ') 

    def Search(self, node_val):
        if self.data == node_val:
            return True 
        
        if node_val < self.data:
            if self.left:
                return self.left.Search(node_val)
            else:
                return False 
        
        if node_val > self.data:
            if self.right:
                return self.right.Search(node_val)
            else:
                return False 

def build_tree(elements):
    root = BinaryTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i]) 
    
    return root 

root = BinaryTree(27)
root.add_child(14)
root.add_child(35)
root.add_child(31)
root.add_child(10)
root.add_child(19)
print(root.build_tree()) 

class BST():
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 
    
    def PrintData(self):
        return self.data 
    
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
        
    def Find_min(self):
        if self.left is None:
            return self.data 

        self.left.Find_min()
    
    def Find_max(self):
        if self.right is None:
            return self.data 
        
        return self.right.Find_max() 
    
    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0 
        right_sum = self.right.calculate_sum() if self.right else 0 

        return self.data + left_sum + right_sum
    
    def TraverseInOrder(self):
        elements = []

        if self.left:
            elements += self.left.TraverseInOrder()

        elements.append(self.data)

        if self.right:
            elements += self.right.TraverseInOrder()

        return elements

    def TraversePostOrder(self):
        elements = []

        if self.left:
            elements += self.left.TraversePostOrder()
        
        if self.right:
            elements += self.right.TraversePostOrder()
        
        elements.append(self.data)

        return elements

    def TraversePreOrder(self):
        elements = []

        if self.left:
            self.left.TraversePreOrder()
        
        if self.right:
            self.right.TraversePreOrder()
        
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

def Build_tree(elements):
    root = BST(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    
    return root 
    

numbers = [17, 4, 1, 20, 9, 23, 18, 34]
numbers_bst = Build_tree(numbers) 
print(numbers_bst.TraverseInOrder())

print(numbers_bst.calculate_sum()) 