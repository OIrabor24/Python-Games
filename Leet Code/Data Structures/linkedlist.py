class Node:

    def __init__(self, data=None, next=None):
        self.data = data 
        self.next = next 

class LinkedList:

    def __init__(self):
        self.head = None #this is the 1st node

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node 

    def print(self):
        if self.head is None:
            print("LinkedList is empty")
            return 
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next 
        
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None) 
            return 

        itr = self.head 
        while itr.next:
            itr = itr.next 

        itr.next = Node(data, None) 

    def insert_values(self, data_list):
        self.head = None 
        for data in data_list:
            self.insert_at_end(data) 

    def get_length(self):
        count = 0
        itr = self.head 

        while itr:
            count += 1 
            itr = itr.next 

        return count 

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next 
            return 
        
        count = 0 
        itr = self.head 
        
        while itr:
            if count == index - 1:
                itr.next = itr.next.next 
                break
            itr = itr.next 
            count  += 1 

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index") 

        if index == 0:
            self.insert_at_beginning(data)
            return 
        
        count = 0
        itr = self.head 

        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node 
                break 

            itr = itr.next 
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return 
        
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return 
        
        itr = self.head 

        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break 

            itr = itr.next 
    
    def remove_by_value(self, data):
        if self.head is None:
            return 

        if self.head.data == data:
            self.head = self.head.next 
            return 
        
        itr = self.head 

        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next 
                break 
            itr = itr.next 

#1.
ll = LinkedList()
ll.insert_values(["banana","mango","grapes","orange"])
ll.print()
ll.insert_after_value("mango","apple")
ll.print()
ll.remove_by_value("orange")
ll.print()
ll.remove_by_value("figs")
ll.print()
ll.remove_by_value("banana")
ll.remove_by_value("mango")
ll.remove_by_value("apple")
ll.remove_by_value("grapes")
ll.print()
 
ll = LinkedList()
ll.insert_at_beginning(5)
ll.insert_at_beginning(89) 
ll.insert_at_end(79)
ll.insert_values(["banana", 'mango', 'grapes', 'oranges'])
ll.print() 
ll.remove_at(2) 
ll.print()
ll.insert_at(0, "figs") 
ll.insert_at(2, "cherry") 
ll.print()
print("length:", ll.get_length())

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data 
        self.next = next 
        self.prev = prev 


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        llstr = ''
        while itr:
            llstr += itr.data + '-->'
            itr = itr.prev
        print("Link list in reverse: ", llstr)

    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def insert_at_begining(self, data):
        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if node.next:
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1

    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.prev
                break

            itr = itr.next
            count+=1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0,"jackfruit")
    ll.print_forward()
    ll.insert_at(6,"dates")
    ll.print_forward()
    ll.insert_at(2,"kiwi")
    ll.print_forward()