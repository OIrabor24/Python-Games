#Return the absolute value of a number: abs(n) 
x = abs(-7.25) 
print(x) 

x = abs(3+5j) 
print(x) 

#all() 	Returns True if all items in an iterable object are true: 
#If the iterable object is empty, the all() function also returns True.
mylist = [True, True, True]
print(all(mylist)) 

print(all({})) 

print(all([0, 1, 1])) 

print(all((0, True, False)))

#any() Returns True if any item in an iterable object is true: If the iterable object is empty, the any() function will return False.
mylist = [False, True, False] 
print(any(mylist)) 

print(any({})) #False 

#ascii() Returns a readable version of an object. Replaces none-ascii characters with escape character
x = ascii("My name is Ståle")  
print(x) 

#bin() Returns the binary version of a number: The result will always start with the prefix 0b.
x = bin(36) 
print(x) 

#bool() Returns the boolean value of the specified object:
#The object will always return True, unless:
# The object is empty, like [], (), {}
# The object is False
# The object is 0
# The object is None
x = bool(1)  
print(x) 

y = bool(0)
print(y)

#bytearray() Returns an array of bytes: It can convert objects into bytearray objects, or create empty bytearray object of the specified size.
x = bytearray(4) 
print(x) 

#bytes() Returns a bytes object: The difference between bytes() and bytearray() is that bytes() returns an object that cannot be modified,
#and bytearray() returns an object that can be modified.

x = bytes(4) 
print(x) 

#callable() Returns True if the specified object is callable, otherwise False:
def x():
    a = 5 

print(callable(x))

#A normal variable is not callable:
x = 5 
print(callable(x)) 

#chr() Returns a character from the specified Unicode code: An integer representing a valid Unicode code point
x = chr(97) 
print(x) 

#classmethod() Converts a method into a class method:
# x = classmethod() 

#compile() Returns the specified source as an object, ready to be executed:
x = compile('print(55)', 'test', 'eval') #Compile text as code, and the execute it:
exec(x) 

#complex() Returns a complex number:
#The complex() function returns a complex number by specifying a real number and an imaginary number.
x = complex(3, 5) 
print(x) 

#delattr() Deletes the specified attribute (property or method) from the specified object:
class Person:
    name = "John"
    age = 36
    country = "Norway"

delattr(Person, 'age') # The Person object will no longer contain an "age" property

#dict() Returns a dictionary (Array):
x = dict(name="John", age=36, country="Norway") 
print(x) 

#dir() Returns a list of the specified object's properties and methods:
class Person:
    name = "John"
    age = 36
    country = "Norway"
print(dir(Person)) 

#divmod() 	Returns the quotient and the remainder when argument1 is divided by argument2:
#The divmod() function returns a tuple containing the quotient  and the remainder when argument1 (dividend) is divided by argument2 (divisor).
x = divmod(5, 2) 
print(x) 

#enumerate() Takes a collection (e.g. a tuple) and returns it as an enumerate object:
#The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
#The enumerate() function adds a counter as the key of the enumerate object.

x = ('apple', 'banana', 'cherry') 
y = enumerate(x)  
print(list(y)) 

#eval() Evaluates and executes an expression:
#The eval() function evaluates the specified expression, if the expression is a legal Python statement, it will be executed.
x = 'print(55)'
print(eval(x)) 

#exec() Executes the specified code (or object):
#The exec() function accepts large blocks of code, unlike the eval() function which only accepts a single expression
x = 'name = "John"\nprint(name)'
exec(x) 

#filter() Use a filter function to exclude items in an iterable object:
#The filter() function returns an iterator were the items are filtered through a function to test if the item is accepted or not.
ages = [5, 12, 17, 18, 24, 32]

def myfunc(x):
    if x < 18:
        return False 
    else:
        return True 

adults = filter(myfunc, ages)

for x in adults:
    print(x) 

#float() Returns a floating point number:
x = float(3) 
print(x) 

#format() Formats a specified value:
#The format() function formats a specified value into a specified format.
x = format(0.5, '%') 
print(x) 

#frozenset() Returns a frozenset object:
#The frozenset() function returns an unchangeable frozenset object (which is like a set object, only unchangeable).
mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
print(x) 

#getattr() Returns the value of the specified attribute (property or method):
#The getattr() function returns the value of the specified attribute from the specified object.
class Person:
    name = "John"
    age = 36
    country = "Norway"

x = getattr(Person, 'age') 
print(x) 

#globals() Returns the current global symbol table as a dictionary:
#A symbol table contains necessary information about the current program
x = globals() 
print(x) 

x = globals()
print(x["__file__"])

#hasattr() Returns True if the specified object has the specified attribute (property/method):
class Person:
  name = "John"
  age = 36
  country = "Norway"

x = hasattr(Person, 'age') 
print(x) 

#hash() Returns the hash value of a specified object:
# a = hash() 

#help() Executes the built-in help system:
help() 

#hex() Converts a number into a hexadecimal value:
# The hex() function converts the specified number into a hexadecimal value.
# The returned string always starts with the prefix 0x.
x = hex(255) 
print(x) 

#id() Returns the id of an object:
x = ('apple', 'banana', 'cherry')
y = id(x) # This value is the memory address of the object and will be different every time you run the program

#input() Allowing user input
print('Enter your name: ')
x = input()
print('Hello, ' + x) 

#int() Returns an integer number
x = int("12")  
print(x) 

#isinstance() Returns True if a specified object is an instance of a specified object:
x = isinstance(5, int) 

#issubclass() Returns True if a specified class is a subclass of a specified object:
class myAge:
    age = 36

class myObj(myAge):
    name = "John"
    age = myAge

x = issubclass(myObj, myAge) 
print(x) 

#iter() Returns an iterator object:
x = iter(["apple", "banana", "cherry"])
print(next(x))
print(next(x))
print(next(x)) 

#len() Returns the length of an object:
mylist = ["apple", "banana", "cherry"]
x = len(mylist) 

#list() Returns a list
x = list(('apple', 'banana', 'cherry'))

#locals() Returns an updated dictionary of the current local symbol table:
x = locals()
print(x)

#map() 	Returns the specified iterator with the specified function applied to each item:
def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))

#max() Returns the largest item in an iterable:
x = max(5, 10)

#memoryview() Returns a memory view object:
x = memoryview(b"Hello")

print(x)

#return the Unicode of the first character
print(x[0])

#return the Unicode of the second character
print(x[1])

#min() 	Returns the smallest item in an iterable:
x = min(5, 10)

#next() Returns the next item in an iterable:
mylist = iter(["apple", "banana", "cherry"])
x = next(mylist)
print(x)
x = next(mylist)
print(x)
x = next(mylist)
print(x)

#object() Returns a new object:
# You cannot add new properties or methods to this object.
# This object is the base for all classes, it holds the built-in properties
# and methods which are default for all classes.
x = object()

#oct() Converts a number into an octal:
x = oct(12)
print(x) 

#open() Opens a file and returns a file object: open(file, mode)
f = open("demofile.txt", "r")
print(f.read()) 

#ord() Convert an integer representing the Unicode of the specified character:
x = ord("h") 
print(x) 

#pow() returns the value of x to the power of y:
x = pow(4, 3) 
print(x) 

#print() 	Prints to the standard output device:
print("Hello World")

#property() Gets, sets, deletes a property:
property() 

#range() Returns a sequence of numbers, starting from 0 and increments by 1 (by default):
x = range(6)
for n in x:
  print(n)

# repr() Returns a readable version of an object:
repr() 

#reversed() Returns a reversed iterator:
alph = ["a", "b", "c", "d"]
ralph = reversed(alph)
for x in ralph:
  print(x)

#round() Rounds a numbers:
x = round(5.76543, 2) #round(number, digits)
print(x)

#set() Returns a new set object: The items in a set list are unordered, so it will appear in random order.
x = set(('apple', 'banana', 'cherry'))

#setattr() Sets an attribute (property/method) of an object:
class Person:
  name = "John"
  age = 36
  country = "Norway"

setattr(Person, 'age', 40)

#slice() Returns a slice object:
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(2) #slice(start, end, step)
print(a[x])

#sorted() Returns a sorted list:
a = ("b", "g", "a", "d", "f", "c", "h", "e")
x = sorted(a)
print(x)

#staticmethod()	Converts a method into a static method

#str() Returns a string object: str(object, encoding=encoding, errors=errors)
x = str(3.5) 
print(x) 

#sum() Sums the items of an iterator:
a = (1, 2, 3, 4, 5)
x = sum(a)

#super() Returns an object that represents the parent class:
class Parent:
  def __init__(self, txt):
    self.message = txt

  def printmessage(self):
    print(self.message)

class Child(Parent):
  def __init__(self, txt):
    super().__init__(txt)

x = Child("Hello, and welcome!")

x.printmessage()

#tuple() Returns a tuple:
x = tuple(('apple', 'banana', 'cherry'))

#type() Returns the type of an object:
a = ('apple', 'banana', 'cherry')
b = "Hello World"
c = 33

x = type(a)
y = type(b)
z = type(c)

#vars() Returns the __dict__ property of an object:
class Person:
  name = "John"
  age = 36
  country = "norway"

x = vars(Person)
print(x) 

#zip() Returns an iterator, from two or more iterators: zip(iterator1, iterator2, iterator3 ...)
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)
print(list(x)) 