#last In First Out: LIFO
from collections import deque
from threading import stack_size

stack = deque() 
# print(dir(stack))

stack.append("www.google.com")
stack.append("www.playstation.com")
stack.append("www.proportfolio.com") 
stack.append("www.youtube.com")
print(stack) 
print(stack.pop()) 

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)
    
    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

# s = Stack()
# s.push(5) 
# s.push(10)
# s.push(11)
# print(s.peek()) 
# s.pop() 
# print(s.is_empty())
# print(s.size())

# def reverse_string(string):
#     return string[::-1] 

# print(reverse_string("We will conquere COVID-19"))

def reverse_string(s):
    stack = Stack()

    for ch in s:
        stack.push(ch)

    rstr = ''

    while stack.size() != 0:
        rstr += stack.pop()
    
    return rstr 

print(reverse_string("We will conquere COVID-19"))

def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        '{': '}',
        ']': '['
    }

    return match_dict[ch1] == ch2 

def is_balanced(s):
    stack = Stack()

    for ch in s:
        if ch =='(' or ch =='{' or ch == '[':
            stack.push(ch) 
        if ch == ')' or ch == '}' or ch == ']':
            if stack.size() == 0:
                return False 
            if not is_match(ch, stack.pop()):
                return False 
    
    return stack_size() == 0 
        

from collections import deque
history = deque()

history.appendleft("https://www.google.com/")
history.appendleft("https://www.youtube.com/")
history.appendleft("https://www.spotify.com/") 
print(history) 

history.popleft()
history.popleft()
print(history)