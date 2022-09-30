class Node():
    def __init__(self, data):
        self.data = data 
        self.next = None 
    
    def __repr__(self):
        return self.data 
    

class LinkedList():
    def __init__(self, nodes=None):
        self.head = None 

        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node 
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next 

    def __repr__(self):
        node = self.head 
        nodes = []
        
        while node is not None:
            nodes.append(node.data)
            node = node.next 
        nodes.append("None")
        return ' -> '.join(nodes) 

    def __iter__(self):
        node = self.head 
        while node is not None:
            yield node 
            node = node.next 

    def add_first(self, node): # inserting at the beginning
        node.next = self.head 
        self.head = node 

    def add_last(self, node):
        if self.head is None:
            self.head = node # node is our input parameter
            return 
        for current_node in self: #self@linkedlist
            pass 
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")
        
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next 
                node.next = new_node 
                return 
        raise Exception("Node with data '%s not found" % target_node_data) 

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")
        
        if self.head.data == target_node_data:
            return self.add_first(new_node)
        
        prev_node = self.head 
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node 
                new_node.next = node 
                return 
            prev_node = node 
        raise Exception("Node with data '%s' not found " % target_node_data)

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")
        
        if self.head.data == target_node_data:
            self.head = self.head.next 
            return 
        
        previous_node = self.head 
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next 
                return 
            previous_node = node 
        
        raise Exception("Node with data '%s' not found" % target_node_data) 
        

llist = LinkedList(["a", "b", "c", "d", "e"]) 
print(llist)

for node in llist: #__iter__
    print(node) 

llist = LinkedList() #add_first
llist.add_first(Node("b"))
llist.add_first(Node("a")) 
print(llist)
print('-' * 40)
llist = LinkedList(["a", "b", "c", "d"])
print("before we insert last: ", llist)
llist.add_last(Node("e")) 
print("e added as last elem: ", llist)
llist.add_last(Node("f"))
print("f added as last: ", llist) 
print('-' * 40)
llist = LinkedList(["a", "b", "c", "d"])
llist.add_after("c", Node("cc")) 
print(llist) 

print('-' * 40)
llist = LinkedList(["b", "c"]) # add_before
llist.add_before("b", Node("a"))
print(llist)
llist.add_before("b", Node("aa"))
llist.add_before("c", Node("bb"))
print(llist) 
