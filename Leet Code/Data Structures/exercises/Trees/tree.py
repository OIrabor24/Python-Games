class BinarySearchTree():
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 
    
    def __repr__(self):
        return f"{self.data}"
    
    def PrintData(self):
        print(self.data) 

    def add_child(self, data):
        if data == self.data:
            return #node already exists
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)
    
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
        right_sum = self.right.calculate_sum if self.right else 0 

        return self.data + left_sum + right_sum
    
    def PostOrderTraversal(self):
        elements = []

        if self.left:
            elements += self.left.PostOrderTraversal()
        
        if self.right:
            elements += self.right.PostOrderTraversal()
        
        elements.append(self.data)

        return elements 
    
    def InOrderTraversal(self):
        elements = []

        if self.left:
           elements += self.left.InOrderTraversal()
        
        elements.append(self.data)

        if self.right:
            elements += self.right.InOrderTraversal()
        
        return elements
    
    def PreOrderTraversal(self):
        elements = []

        if self.left:
            elements += self.left.PreOrderTraversal()
        
        if self.right:
            elements += self.right.PreOrderTraversal()
        
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

    def Build_Tree(elements):
        root = BinarySearchTree(elements[0])

        for i in range(1, len(elements)):
            root.add_child(elements[i])
        
        return root 



class BinarySearchTree():
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 
    
    def __repr__(self):
        return f"{self.data}" 
    
    def PrintData(self):
        print(self.data) 
    
    def add_child(self, data):
        if data == self.data:
            return #node already exists
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data) 
        
    
    #Traverse PreOrder
    def TraversePreOrder(self):
        print(self.data, end=' ')
        if self.left:
            self.left.TraversePreOrder()
        if self.right:
            self.right.TraversePreOrder() 
    
    #Traverse InOrder
    def TraverseInOrder(self):
        if self.left:
            self.left.TraverseInOrder()
        print(self.data, end=' ')
        if self.right:
            self.right.TraverseInOrder() 
    
    #Traverse PostOrder
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
    
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree() 

#inorder
def printInorder(self):
    if self:
        printInorder(self.left)

        print(self.data),

        printInorder(self.right) 
#preorder
def printPreorder(self):
 
    if self:
 
        # First print the data of node
        print(self.data),
 
        # Then recur on left child
        printPreorder(self.left)
 
        # Finally recur on right child
        printPreorder(self.right)

#postorder
def printPostorder(self):
 
    if self:
 
        # First recur on left child
        printPostorder(self.left)
 
        # the recur on right child
        printPostorder(self.right)
 
        # now print the data of node
        print(self.data), 
    

def build_tree(elements):
    root = BinarySearchTree(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    
    return root 

root = BinarySearchTree(1)
root.left = BinarySearchTree(2)
root.right = BinarySearchTree(3)
root.left.left = BinarySearchTree(4)
root.left.right = BinarySearchTree(5) 

print("Traverse Pre order is:")
root.TraversePreOrder() 
print('-' * 40) 
print("Traverse In order is:")
root.TraverseInOrder()
print('-' * 40) 
print("Traverse Post order:")
root.TraversePostOrder()
# print("Postorder:")
# printPostorder(root) 
# numbers = [17, 4, 1, 20, 9, 23, 18, 34]

# numbers_tree = build_tree(numbers) 


# print(numbers_tree.TraverseInOrder()) 
# print('-' * 40) 
# print(printInorder(numbers_tree)) 

# print(numbers_tree.Search(20)) 
# print(numbers_tree.Search(24)) 

# countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
# country_tree = build_tree(countries)
# print(country_tree.TraverseInOrder()) 

# print("Is USA in our list? ", country_tree.Search("USA")) 