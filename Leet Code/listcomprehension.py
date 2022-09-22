# creating a list of numbers
num_list = [1,2,3,4,5]

# using list comprehension to create cube_list
cube_list = [num **3 for num in num_list]

print(cube_list)

for num in num_list:
    num ** 3
print(cube_list) 

list_of_strings = ['hello', 'my', 'name', 'a']

len_of_strings = [len(word) for word in list_of_strings]
print(len_of_strings) 

cubes_of_odd = [num ** 3 for num in num_list if num % 2 != 0] 
print(cubes_of_odd) 

cubes_and_squares = [num **3 if num % 2 != 0 else num **2 for num in num_list]
print(cubes_and_squares) 


for num in num_list:
    if num % 2 != 0:
        num **3
    elif num % 2 == 0:
        num ** 2 
print(cubes_and_squares)  

matrix = [[1, 2, 3, 4],
          [1, 2, 3, 4],
          [1, 2, 3, 4],
          [1, 2, 3, 4]]

# make a matrix
matrix = [] 

for y in range(1,5):
    matrix.append([x for x in range(1,5)]) 

#The above code is equivalent to the following nested list comprehension:
matrix = [[x for x in range(1,5)] for y in range(1,5)] 

[x**2 for x in range(10) if x % 2 == 0]

list(map(lambda x:x**2, filter(lambda x:x%2==0, range(10)))) 