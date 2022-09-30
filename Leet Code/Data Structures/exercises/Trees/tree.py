# class BinaryTreeNode():
#     def __init__(self, data):
#         self.data = data 
#         self.left = None 
#         self.right = None 
    
#     def PrintData(self):
#         print(self.data) 
    
#     def add_child(self, data):
#         if self.data:
#             if data < self.data:
#                 if self.left is None: #if no left child
#                     self.left = BinaryTreeNode(data)
#                 else:
#                     self.left.add_child(data) 
#             elif data > self.data:
#                 if self.right is None:
#                     self.right = BinaryTreeNode(data)
#                 else:
#                     self.right.add_child(data) 
#         else:
#             self.data = data 
        
#     def PrintTree(self):
#         if self.left:
#             self.left.PrintTree()
#             print(self.data)
#         if self.right:
#             self.right.PrintTree() 

#     #Traverse Preorder
#     def TraversePreOrder(self):
#         print(self.data, end=' ')
#         if self.left:
#             self.left.TraversePreOrder()
#         if self.right:
#             self.right.TraversePreOrder()
    
#     #Traverse Inorder
#     def TraverseInOrder(self):
        # if self.left:
        #     self.left.TraverseInOrder()
        # print(self.data, end=' ')
        # if self.right:
        #     self.right.TraverseInOrder() 
    
#     #Traverse PostOrder
#     def TraversePostOrder(self):
#         if self.left:
#             self.left.TraversePostOrder()
#         if self.right:
#             self.right.TraversePostOrder()
#         print(self.data, end=' ')
    
#     def Search(self, node_val):
#         if self.data == node_val:
#             return True 
        
#         if node_val < self.data:
#             #node_val might be in left subtree
#             if self.left:
#                 return self.left.Search(node_val)
#             else:
#                 return False 
        
#         if node_val > self.data:
#             # val might be in right subtree
#             if self.right:
#                 return self.right.Search(node_val)
#             else:
#                 return False 

# def build_tree(elements):
#     root = BinaryTreeNode(elements[0])

#     for i in range(1, len(elements)):
#         root.add_child(elements[i])
    
#     return root 

# root = BinaryTreeNode(27)
# root.add_child(14)
# root.add_child(35)
# root.add_child(31)
# root.add_child(10)
# root.add_child(19)



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