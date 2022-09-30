from collections import deque
class Node():
    """[data|next ->]"""
    def __init__(self, data):
        self.data = data 
        self.next = None 
    
    def __repr__(self):
        return self.data 

class LinkedList():
    """
    A linked list is a collection of nodes. 1st node is called the head.
    The Last node must have it's next reference pointing to None.    
    """
    def __init__(self, nodes=None):
        self.head = None 
        #quickly create a linked list with some data
        if nodes is not None:
            node = Node(data=nodes.pop(0)) #pop index 0 at beginning 
            self.head = node 
            for element in nodes:
                node.next = Node(data=element)
                node = node.next 

    def __repr__(self):
        node = self.head 
        nodes = [] 
        while node is not None:
            nodes.append(node.data)
            node = node.next 
        nodes.append("None")

        return " -> ".join(nodes)     

    def __iter__(self): #traverse a linked list
        node = self.head 
        while node is not None:
            yield node
            node = node.next
    
    def add_first(self, node):
        node.next = self.head 
        self.head = node 
    
    def add_last(self, node): #inserting at the end
        if self.head is None:
            self.head = node 
            return 
        for added_node in self:
            pass 
        added_node.next = node 

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("list is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next 
                node.next = new_node 
                return 
        
        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")
        
        if self.head.data == target_node_data: #add a new node before the head of the list
            return self.add_first(new_node) #node you’re inserting will be the new head of the list.
        
        prev_node = self.head 
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

#Add before method 
llist = LinkedList(["b", "c"])
llist.add_before("b", Node("a"))
print(llist)

llist.add_before("b", Node("aa"))
llist.add_before("c", Node("bb"))
print(llist) 

#Add after method
llist = LinkedList(["a", "b", "c", "d"])
llist.add_after("c", Node("cc"))
print(llist) 
llist.add_after("f", Node("g"))
print(llist)

# Add last method
llist = LinkedList(["a", "b", "c", "d"])
llist.add_last(Node("e"))
llist.add_last(Node("f"))
print(llist) 


#Add first method
llist = LinkedList()
llist.add_first(Node("b"))
llist.add_first(Node("a")) 
print(llist)

#Traversing with iter iterating method
llist = LinkedList(['a', 'b', 'c', 'd', 'e']) 
print(llist)

for node in llist:
    print(node) 

llist = LinkedList()
first_node = Node("a")
llist.head = first_node
print(llist)

second_node = Node("b")
third_node = Node("c") 
first_node.next = second_node
second_node.next = third_node
print(llist) 


a = deque(['a', 'b', 'c']) 
print(a) 
b = deque([{'data': 'a'}, {'data': 'b'}]) 
print(b) 

llist = deque("abcde") 
llist.append('f')
print(llist) 
llist.pop() 
print(llist)

#adding & removing from the head
llist.appendleft("Z")
print(llist)
llist.popleft() 
print(llist) 

#QUEUES
queue = deque()
queue.append("Mary")
queue.append("John")
queue.append("Susan")
print(queue) 

#Remove from QUEUE
one = queue.popleft()
print(one)
two = queue.popleft()
print(two)
print(queue) 

#STACKS
history = deque()

history.appendleft("https://realpython.com/")
history.appendleft("https://realpython.com/pandas-read-write-files/")
history.appendleft("https://realpython.com/python-csv/")
print(history)

history.popleft()
history.popleft()
print(history) 