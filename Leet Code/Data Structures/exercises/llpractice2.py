class Node():
    def __init__(self, data):
        """
        By defining a node’s data and next values, you can create a linked list quite quickly.
        """
        self.data = data 
        self.next = None 
    
    def __repr__(self):
        return self.data 

class LinkedList():
    """
    The only information you need to store for a linked list is where the list starts (the head of the list).
    """
    def __init__(self, nodes=None):
        self.head = None 

        if nodes is not None:
            node = Node(data=nodes.pop(0)) #pop 1st element as head
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
        """
        goes through the list and yields every single node.
        After yielding the current node, you want to move to the next node on the list.
        That’s why you add node = node.next.
        """
        node = self.head 
        while node is not None:
            yield node 
            node = node.next 
    
    def add_first(self, node): #inserting at the beginning
        """
         you’re setting self.head as the next reference of the new node so that the new node points to the old self.head.
        After that, you need to state that the new head of the list is the inserted node.
        """
        node.next = self.head 
        self.head = node 
    
    def add_last(self, node):
        """
        First, you want to traverse the whole list until you reach the end (that is, until the for loop raises a StopIteration exception).
         Next, you want to set the current_node as the last node on the list.
        Finally, you want to add the new node as the next value of that current_node.
        """
        if self.head is None:
            self.head = node # node is our input parameter 
            return 
        for current_node in self:
            pass 
        current_node.next = node 
    
    def add_after(self, target_node_data, new_node):
        """
        you’re traversing the linked list looking for the node with data indicating where you want to insert a new node.
        When you find the node you’re looking for,
        you’ll insert the new node immediately after it and rewire the next reference to maintain the consistency of the list.
        """
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next 
                node.next = new_node 
                return 
        raise Exception("Node with data '%s' not found" % target_node_data) 


