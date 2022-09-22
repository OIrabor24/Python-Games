#Queue FIFO
from collections import deque
import time 
import threading

q = deque()

q.appendleft(5)
q.appendleft(6)
q.appendleft(7)
print(q) #[7, 6, 5]
q.pop() 
print(q) 
q.pop() 
print(q)

class Queue:
    def __init__(self):
        """a list like sequence."""
        self.queue = deque()

    def enqueue(self, val):
        """append item left."""
        self.queue.appendleft(val)
    
    def dequeue(self):
        """pop next item at [-1]."""
        if len(self.queue) == 0:
            print("Queue is empty")
            return exit()

        return self.queue.pop()

    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue) 

    def front(self):
        """part of tutorial exercise. returns arg [-1]"""
        return self.queue[-1] 

pq = Queue()

pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
print(pq.queue)
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})
print(pq.queue)
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})

print(pq.queue)

print(pq.dequeue()) 


#Design a food ordering system where your python program will run two threads:



food_order = Queue()

def place_order(orders):
    for order in orders:
        print("Placing order: ", order)
        food_order.enqueue(order)
        time.sleep(0.5) 

def serve_order():
    time.sleep(1)
    
    while True:
        order = food_order.dequeue()
        print("Serving:", order) 
        time.sleep(2) 
        

orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']



t1 = threading.Thread(target=place_order, args=(orders,))
t2 = threading.Thread(target=serve_order) 

t1.start()
t2.start()

# binary_nums = [1, 10, 11, 100, 101, 110, 111, 1000, 1001, 1010]
#2. Write a program to print binary numbers from 1 to 10 using Queue.


def print_binary(numbers):
    numbers_queue = Queue()
    numbers_queue.enqueue("1")

    for i in range(numbers):
        print(i)
        front = numbers_queue.front()
        print(" ", front) 
        numbers_queue.enqueue(front + "0")
        numbers_queue.enqueue(front + "1")
        numbers_queue.dequeue()

print(print_binary(10))  

from collections import deque

a = deque(['a', 'b', 'c']) 
print(a) 

b = deque('abc')

c = deque([{'data': 'a'}, {'data': 'b'}, {'data': 'c'}])
print(c) 

linked_list = deque('abcde')
print(linked_list)

linked_list.append('f')
print(linked_list) 

print(linked_list.pop())
print(linked_list)

linked_list.appendleft("z") 
print(linked_list)
print(linked_list.popleft())
print(linked_list)

from collections import deque
queue = deque()

queue.append("Mary")
queue.append("John")
queue.append("Susan")
print(queue) 

queue.popleft()
print(queue)
queue.popleft() 
print(queue)
