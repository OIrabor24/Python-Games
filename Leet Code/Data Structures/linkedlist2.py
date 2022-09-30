class Node():
    """Node (e.g. data|next)."""
    def __init__(self, data):
        self.data = data 
        self.next = None 

    def __repr__(self) -> str:
        return self.data 

class LinkedList():
    """LinkedList head"""
    def __init__(self, nodes=None):
        self.head = None 

        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node 
            
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next 

    def __repr__(self) -> str:
        node = self.head 
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next 
        nodes.append("None")
        return " -> ".join(nodes) 

    def __iter__(self):
        node = self.head 
        while node is not None:
            yield node 
            node = node.next 

    def add_first(self, node):
        node.next = self.head 
        self.head = node 

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return 
        for current_node in self:
            pass 
        current_node.next = node 

    def add_after(self, target_node_data, new_node):
        """add a node after an existing node with a specific data value"""
        if self.head is None:
            raise Exception("List is empty")
        
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next 
                node.next = new_node
                return 

        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")
        
        if self.head.data == target_node_data:
            return self.add_first(new_node)
        
        prev_node = self.head  #keep track of the last-checked node using the prev_node variable
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node 
                new_node.next = node 
                return 
            prev_node = node 
        
        raise Exception("Node with data '%s' not found" % target_node_data)

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


linked_list = LinkedList()
first_node = Node("a")
linked_list.head = first_node
print(linked_list) 

second_node = Node("b")
first_node.next = second_node
print(linked_list)

third_node = Node("c")
second_node.next = third_node
print(linked_list)

#traversing a random list & printing each node:
linked_list = LinkedList(["a", "b", "c", "d", "e"])

for node in linked_list:
    print(node) 

#add first method
linked_list = LinkedList()
linked_list.add_first(Node("b"))
print(linked_list)

linked_list.add_first(Node("a"))
print(linked_list) 

#add last method
linked_list = LinkedList(["a", "b", "c", "d"])
print(linked_list)
linked_list.add_last(Node("e"))
print(linked_list)
linked_list.add_last(Node("f"))
print(linked_list)

#inserting between two nodes: add after method
# linked_list = LinkedList()
# linked_list.add_after("a", Node("b"))
# print(linked_list) Exception: List is empty

linked_list = LinkedList(["a", "b", "c", "d"])
print(linked_list) 

linked_list.add_after("c", Node("cc"))
print(linked_list)

# linked_list.add_after("f", Node("g")) Exception: Node with data 'f' not found

# add before method:
# linked_list = LinkedList()
# linked_list.add_before("a", Node("a")) Exception: List is empty

linked_list = LinkedList(["b", "c"])
print(linked_list)

linked_list.add_before("b", Node("a"))
print(linked_list) 

linked_list.add_before("b", Node("aa"))
linked_list.add_before("c", Node("bb"))
print(linked_list) 
# linked_list.add_before("n", Node("m")) Exception: Node with data 'n' not found

#remove node method:
# linked_list = LinkedList()
# linked_list.remove_node("a") 
# print(linked_list) Exception: List is empty

linked_list = LinkedList(["a", "b", "c", "d", "e"]) 
print(linked_list) 

linked_list.remove_node("a")
print(linked_list) 

linked_list.remove_node("e")
print(linked_list)

linked_list.remove_node("c")
print(linked_list)

