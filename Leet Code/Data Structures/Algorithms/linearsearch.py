def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i 
    return -1

def verify(index):
    if index is not None:
        print("Target is at index: ", index)
    else:
        print("Target not found")

numbers = [1,2,3,4,5,6,7,8,9,10] 

searching = linear_search(numbers, 1) 
print(searching)

verify(searching) 

def LinearSearch(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i 
    return - 1 

def Verify(index):
    if index is not None:
        print("The index is at index:", index)
    else:
        print("Target not found") 
    
numbers = [1,2,3,4,5,6,7,8,9,10] 
print(LinearSearch(numbers, 1)) 

looking = LinearSearch(numbers, 2)
print(looking) 

def LinearSearch2(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i 
    return -1 

numbers = [1,2,3,4,5,6,7,8,9,10] 
print(LinearSearch2(numbers, 5)) 

def LinearSearch(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1 

def LinearSearch(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i 
    return -1 

numbers = [1,2,3,4,5,6,7,8,9,10] 
print(LinearSearch(numbers, 11)) 

def LinearSearch(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i 
    return -1

numbers = [1,2,3,4,5,6,7,8,9,10] 
print(LinearSearch(numbers, 7)) 

def Linearsearch(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i 
    return -1 