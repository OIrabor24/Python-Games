from collections import deque

stack = deque()

stack.append("www.google.com")
stack.append("www.amazon.com")
stack.append("www.bestbuy.com")
stack.append("www.youtube.com")
print(stack)
youtube = stack.pop()
print("Last in first out:", youtube)
print(stack)
bestbuy = stack.pop()
print("pop bestbuy ", bestbuy)

class Stack():
    def __init__(self):
        self.stack = deque()

    def __repr__(self):
        return str(self.stack)

    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1] 
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack) 

s = Stack()
s.push("1")
s.push("2")
s.push("3")
print(s) 
print("Peek -> ", s.peek())
print("Size of stack: ", s.size())
three = s.pop()
print("Pop LIFO: (3) -> ", three)

print(s.peek()) 
print("Is the stack empty?", s.is_empty())

class Stack: # -> LIFO
    def __init__(self):
        self.stack = deque() 
    
    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0 
    
    def size(self):
        return len(self.stack) 

from collections import deque
class Stack:
    def __init__(self):
        self.stack = deque()
    
    def __repr__(self) -> str:
        return f"{self.stack}" 
    
    def push(self, val):
        self.stack.append(val)
    
    def pop(self):
        return self.stack.pop() 
    
    def peek(self):
        return self.stack[-1]
    
    def empty(self):
        return self.stack == 0
    
    def size(self):
        return len(self.stack) 

stack = Stack() 
stack.push("O")
stack.push("S")
stack.push("A")
stack.push("H")
stack.push("O")
stack.push("N") 
print(stack)  
stack1 = Stack()
stack1.push(1)
stack1.push(2)
stack1.push(3)
print(stack1)

a = stack.pop()
print(a) 

b = stack1.pop()
print(b) 
print("stack1: ", stack1.peek())
print("stack: ", stack.peek())