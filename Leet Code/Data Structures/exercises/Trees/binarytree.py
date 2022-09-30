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
    #Traverse Preorder
    def traversePreOrder(self):
        print(self.data, end=' ')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder() 

    #Traverse Inorder
    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.data, end=' ')
        if self.right:
            self.right.traverseInOrder()

    #Traverse Postorder
    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.data, end=' ') 

    def search(self, node_val):
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

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree() 

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i]) 
    
    return root 

root = BinarySearchTreeNode(27)
root.add_child(14)
root.add_child(35)
root.add_child(31)
root.add_child(10)
root.add_child(19)

root.PrintTree() 
node_val = root.search(35) 

numbers = [17, 4, 1, 20, 9, 23, 18, 34]


numbers_tree = build_tree(numbers)

print(numbers_tree.search(20)) 