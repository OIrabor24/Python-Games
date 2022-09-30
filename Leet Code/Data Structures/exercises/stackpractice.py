#using Python Lists
my_stack = [] 

my_stack.append('a')
my_stack.append('b')
my_stack.append('c') 
print(my_stack)

a = my_stack.pop() 
print(a) 
b = my_stack.pop()
print(b)
c = my_stack.pop()
print(c) 

print('-' * 60)
#Using collections.deque
from collections import deque
from inspect import stack
from this import d
my_stack = deque()

my_stack.append('a')
my_stack.append('b')
my_stack.append('c')
print(my_stack)

c = my_stack.pop()
print("popped val: ", c) 
b = my_stack.pop()
print("popped val: ", b)
a = my_stack.pop()
print("popped val: ", a) 

#using queue.LifoQueue for multi-threading safety
from queue import LifoQueue
mystack = LifoQueue()

mystack.put('a')
mystack.put('b')
mystack.put('c') 
print(mystack) 

c = mystack.get()
print("popped val: ", c) 
b = mystack.get()
print("popped val: ", b) 
a = mystack.get()
print("popped val: ", a) 

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self, val):
        self.container.append(val)
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def empty(self):
        return len(self.container) == 0 
    
    def size(self):
        return len(self.container)


class Stack:
    def __init__(self):
        self.container = deque() 
    
    def push(self, val):
        self.container.append(val)
    
    def pop(self):
        return self.container.pop() 
    
    def peek(self):
        return self.container[-1]
    
    def empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container) 


class Stack():
    def __init__(self):
        self.container = deque()
    
    def __repr__(self):
        return f"{self.container}"
    
    def push(self, val):
        self.container.append(val)
    
    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container) 

stacked = Stack() 
stacked.push(1)
stacked.push(2)
stacked.push(3)
stacked.push(4)
stacked.push(5) 
print(stacked) 
five = stacked.pop()
print(five) 
four = stacked.pop()
print(four) 
print(stacked.peek())
print(stacked.empty())
print(stacked.size()) 