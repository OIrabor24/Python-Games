from collections import deque

queue = deque() #FIFO
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5) 
print(queue) 

class Queue():
    def __init__(self):
        """A list like sequence."""
        self.queue = deque()
    
    def __repr__(self) -> str:
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
    
    def front(self):
        return self.queue[0]
    
    def back(self):
        return self.queue[-1] 

class Queue2():
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

class Queue3():
    def __init__(self):
        self.queue = deque()
    
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


from collections import deque
class Queue4():
    def __init__(self):
        self.queue = deque()
    
    def __repr__(self):
        return f"{self.queue}"
    
    def enqueue(self, val):
        self.queue.append(val)
    
    def dequeue(self):
        if self.queue is None:
            print("Queue is empty")
            return 
        return self.queue.popleft() 
    
    def empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def front(self):
        return self.queue[0]
    
    def back(self):
        return self.queue[-1]
    

queue = Queue4()
queue.enqueue(1)
queue.enqueue(3)
queue.enqueue(5)
print(queue)

