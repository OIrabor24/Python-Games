#Tuples
import this


x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi" 
x = tuple(y) 

print(x) 

print() 
# add items 
thistuple = ("apple", "banana", "cherry")
x = list(thistuple)
x.append("orange")
x.append("strawberry")  
thistuple = tuple(x) 
print(thistuple)

print()
#Add tuple to a tuple 
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y 
print(thistuple) 

#Remove items 
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple") 
thistuple = tuple(y) 
print(thistuple) 

# delete tuple
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)  #this will raise an error because the tuple no longer exists

# Loop through a Tuple 
thistuple = ("apple", "banana", "cherry")

for x in thistuple:
    print(x) 

#Loop through the index numbers
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])   

#using a while loop
thistuple = ("apple", "banana", "cherry")
i = 0 
while i < len(thistuple):
    print(thistuple[i])
    i += 1 

# Join two tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3) 

#multiply tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2 
print(mytuple) 