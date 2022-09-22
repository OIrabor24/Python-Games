    #if num is an integer then
    # add the integers 0 through num and return sum 
    # if num is not an integer then return 0

def add(num):
    if type(num) == int:
        total = 0 
        for x in range(num + 1):
            print(x) 
            total += x 
        return total 
    else:
        return 0 

def add1(num):
    total = 0
    if not type(num) == int:
        return 0 
    else:
        for x in range(num + 1):
            print(x) 
            total += x 
        return total 

# using reduce function 
import enum
from functools import reduce
from re import sub
def add2(num):
    if type(num) == int:
        return reduce(lambda x,y: x+y, range(num+1))
    else:
        return 0 

print(add2(5))
print(add2('e'))

#using Ternary Operators
def add3(num):
    return reduce(lambda x,y: x+y, range(num + 1)) if type(num) == int else 0

#sum() function 
def add4(num):
    return sum(range(num+1)) if type(num) == int else 0 


# input: int ex. 5 output: sum(input)
# add int input values +
#return the sum of int from 0-num
# return 0 if a non-int value is passed in 

#pseudocode
# if num is an integer:
    # iterate over num and add 0 through num to total and return the sum
    # if num is not an integer then return 0 

def add(num):
    if type(num) == int: # if input is an int, continue
        total = 0 
        for x in range(num + 1):
            print(x) 
            total += x 
        return total 
    else:
        return 0 

print(add(5)) 
print(add('d')) 

def add1(num):
    if not type(num) == int:
        return 0 
    else:
        total = 0
        for x in range(num + 1):
            total += x 
        return total 

print(add1(5)) 
print(add1('r'))

#lambda
num = 3
square = lambda num: num ** 2
print(square(num))  

two_params = lambda num1, num2: num1 + num2 
print(two_params(4,8)) 

conditions = lambda num1, num2: num1 if num1 > num2 else num2
print(conditions(11,9))  

num1 = 7
num2 = 5

if num1 > num2:
    print("num1:",num1)
else:
    print("num2:", num2)  

#Map function map(function, iterable)
#For example, we have a list of numbers (the iterable object), 
#and we want to create a new list that contains the squares of those numbers.
num_list = [1, 2, 3, 4, 5]

squared_list = list(map(lambda x:x**2, num_list))

print(squared_list) 

arrays = [2, 4, 6, 8, 10]

divided = list(map(lambda x: x//2, arrays))

print(divided) 

arrays = [2, 4, 6, 8, 10]

subtract = tuple(map(lambda x: x - 2 , arrays))

print(subtract)

# abc = 'abcdefghijklmnopqrstuvwxyz' or 

import string 
abc = string.ascii_lowercase
print(abc) 

def encrypt(msg, n):
    return ''.join(map(lambda x:abc[(abc.index(x)+n)% 26] if x in abc else x, msg)) 

print(encrypt('how are you?', 2)) 

#Filter Function
# Simply put, the filter function will “filter out” an iterable object based on a specified condition.
#This condition will be decided by the function that we pass in.
num_list = [1, 2, 3, 4, 5, 6]

list_of_even_nums = list(filter(lambda x:x%2==1, num_list)) 

print(list_of_even_nums) 

# List Comprehension
lists = [x**2 for x in range(10) if x % 2==0]
print(lists) 

for x in range(10): # list comp, same as
    if x % 2 == 0:
        print(x**2) 

list(map(lambda x:x**2, filter(lambda x:x%2==0, range(10)))) 

#Reduce Function 
#the reduce function takes an iterable, such as a list, and reduces 
#it down to a single cumulative value. The reduce function can take in three arguments, 
#two of which are required. The two required arguments are: a function (that itself
# takes in two arguments), and an iterable (such as a list). The third argument,
# which is an initializer, is optional.
from functools import reduce 
num_list = [1,2,3,4,5]

product = reduce(lambda x,y:x*y, num_list)

print(product) # the x arg get updated with the accumulated val, y gets updated from the iterable

#Enumerate function: gives you back two loop variables
#You shoulde use enumerate() anytime you need to use the count and an item in a loop!
values = ["a", "b", "c"]
index = 0 
for value in values:
    print(index, value)
    index += 1 

for index in range(len(values)):
    value = values[index] 
    print(index, value) 

for count, value in enumerate(values):
    print(count, value) 

for count, value in enumerate(values, start=1):
    print(count, value) 

#Conditional Statements to Skip items
users = ["Test User", "Real User 1", "Real User 2"]

for index, user in enumerate(users):
    if index == 0:
        print("Extra verbose output for:", user)
    print(user) 

arrays = [1, 2, 3, 4, 5,6]

def even_items(iterable):
    """Return items from 'iterable' when their index is even."""
    values = [] 
    for index, value in enumerate(iterable, start=1):
        if not index % 2:
            values.append(value)
    return values 

def alphabet():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for a in alpha:
        yield a 
print(even_items(alphabet())) 

print(even_items(arrays)) 

def even_item(iterable):
    return [v for i, v in enumerate(iterable, start=1) if not i % 2]

def unpack(iterable):
    values = []
    for index, value in enumerate(iterable, start=1):
        if not index % 2:
            values.append(value) 
    return values 

seasons = ["Spring", "Summer", "Fall", "Winter"]
def my_enumerate(sequence, start=0):
    n = start 
    for elem in sequence:
        yield n, elem 
        n += 1 

print(list(my_enumerate(seasons, start=0))) 
print(tuple(my_enumerate(seasons, start=0))) 

#Zip(): Allows you to iterate through two or more sequences at the same time.
first = ["a", "b", "c"]
second = ["d", "e", "f"]
third = ["g", "h", "i"]

for one, two, three in zip(first, second, third):
    print(one, two, three) 

#You can combine zip() and enumerate() by using nested argument unpacking:
for count, (one, two, three) in enumerate(zip(first, second, third)):
    print(count, one, two, three) 

def isAnagram(self, s: str, t: str) -> bool:
         # terminating condition to check if strings are equal in length
            if len(s) != len(t):
                return False 
            
            if set(s) == set(t):
                pass

dictionary = {'Bruno': "fernandes",
            'Cristiano': "Ronaldo",
            'Marcus': 'Rashford',
            'Kylian': 'Mbappe',
            'Anthony': 'Martial'
}

table = {}
print(dict.copy(dictionary)) 

x = {'lionel', 'wayne', 'Jadon', 'Zidane'}
y = 10

thisdict = dict.fromkeys(x, y) 
print(thisdict) 

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items() 
car["year"] = 2022
print(x)

y = car.keys()
print(y) 

car.pop("year") 
print(car) 

z = car.popitem()
print(z) 

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
}

a = car.setdefault("color", "white")
print(a) 

car.update({"color": "red"}) 
print(car) 

b = car.values()
print(b) 

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

n = car.popitem()
print(n) 

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

a = car.setdefault("color", "pink")
print(a) 
print(car) 