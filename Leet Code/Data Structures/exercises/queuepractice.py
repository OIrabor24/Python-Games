#Queue FIFO
from collections import deque

# q = deque()

# q.append(10)
# q.append(5)
# q.append(2)
# q.append(8)
# q.append(1) 
# print(q) 

class Queue():
    def __init__(self):
        """A list like sequence."""
        self.queue = deque() 
    
    def __repr__(self):
        return f"{self.queue}" 

    def enqueue(self, val):
        """add val's to queue."""
        self.queue.append(val)
    
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return exit() 
        
        return self.queue.popleft() 

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

    def is_front(self):
        return self.queue[0]
    def is_back(self):
        return self.queue[-1] 

q = Queue()
q.enqueue(10)
q.enqueue(5)
q.enqueue(2)
q.enqueue(8)
q.enqueue(1) 
print(q) 
q.dequeue() 
print(q) 

print(q.size()) 
print(q.is_empty()) 
print(q.is_front()) 
print(q.is_back())

class Queue2():
    def __init__(self):
        """a faster list like data structure."""
        self.queue = deque()
    
    def __repr__(self):
        return f'{self.queue}'

    def enqueue(self, val):
        """add a val to queue."""
        self.queue.append(val) 
    
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return exit()
        return self.queue.popleft() 
    
    def empty(self):
        return len(self.queue) == 0 
    
    def size(self):
        return len(self.queue) 
    
    def front(self):
        return self.queue[0]
    
    def end(self):
        return self.queue[-1] 

line = Queue2() 
line.enqueue(5)
line.enqueue(4)
line.enqueue(3)
line.enqueue(2)
line.enqueue(1) 
print(line) 
line.dequeue()
print(line) 
print(line.empty()) 
print(line.size()) 
print(line.front()) 
print(line.end())

class Queue3():
    def __init__(self):
        self.queue = deque()
    
    def __str__(self):
        return f"{self.queue}"
    
    def enqueue(self, val):
        self.queue.append(val)
    
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return exit()

        return self.queue.popleft() 
    
    def empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue) 
    
    def front(self):
        return self.queue[0]
    
    def back(self):
        return self.queue[-1] 

class Queue4:
    def __init__(self):
        self.queue = deque() 
    
    def __str__(self):
        return f"{self.queue}" 
    
    def enqueue(self, val):
        self.queue.append(val) 
    
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return exit() 
        
        return self.queue.popleft() 
    
    def empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def front(self):
        return self.queue[0]
    
    def end(self):
        return self.queue[-1] 

class Queue5:
    def __init__(self):
        self.queue = deque() 
    
    def __str__(self):
        return f"{self.queue}"
    
    def enqueue(self, val):
        self.queue.append(val)
    
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
            return exit()
        
        return self.queue.popleft() 
    
    def empty(self):
        return len(self.queue) == 0 
    
    def size(self):
        return len(self.queue)
    
    def front(self):
        return self.queue[0]
    
    def end(self):
        return self.queue[-1] 

print('-' * 40)
q = Queue5()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5) 
print(q) 
q.dequeue()
print(q) 
print(q.empty())
print(q.size()) 
print(q.front())
print(q.end()) 