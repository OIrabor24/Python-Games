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
                return self.left.search(node_val)
            else:
                return False 

        if node_val > self.data:
            #val might be in right subtree
            if self.right:
                return self.right.search(node_val)
            else:
                return False 

root = BinarySearchTreeNode(27)
root.add_child(14)
root.add_child(35)
root.add_child(31)
root.add_child(10)
root.add_child(19)

root.PrintTree() 
node_val = root.search(35) 

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