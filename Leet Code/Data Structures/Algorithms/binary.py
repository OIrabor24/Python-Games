def linear_search(array, target):
    for index, element in enumerate(array):
        if element == target:
            return index 
    return -1

def LinearSearch(array, target):
    for index, val in enumerate(array):
        if val == target:
            return index 
    return -1 

print(LinearSearch([1,2,3,4,5], 4))


def binary_search(array, target):
    left = 0
    right = len(array) - 1 

    while left <= right:
        mid = (left + right) // 2 

        if array[mid] == target:
            return mid 
        elif array[mid] < target:
            left = mid + 1 
        else:
            right = mid - 1 
    
    return -1

def binary_search_recursive(array, target, left_index, right_index):
    if right_index < left_index:
        return -1
    
    mid = (left_index + right_index) // 2

    if mid >= len(array) or target < 0:
        return -1
    
    if array[mid] == target:
        return mid 
    
    if array[mid] < target:
        left_index = mid + 1 
    else:
        right_index = mid - 1
    
    return binary_search_recursive(array, target, left_index, right_index)


numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
target = 45 

index = linear_search(numbers_list, target) 
print(f"Number found at index {index} using linear search.")

target = 24
array_index = binary_search(numbers_list, target) 
print(f"Number found at index {array_index} using binary search.")

binary_recursive = binary_search_recursive(numbers_list, target, 0, len(numbers_list)) 
print(f"Number was found at index {binary_recursive} using recursion") 

#[1,2,3,4,5]
def BinarySearch(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2 
        if array[mid] == target:
            return mid 
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1 
    
    return -1 

print(BinarySearch([1,2,3,4,5], 5)) 

def BinarySearch2(array, target):
    left = 0 
    right = len(array) 

    while left <= right and target in array:
        mid = (left + right) // 2 

        if array[mid] == target:
            return mid 
        elif array[mid] > target:
            right = mid - 1 
        else:
            left = mid + 1 
    return -1 

print(BinarySearch2([1,2,3,4,5], 8)) 

def BinarySearchAlgo(array, target):
    left = 0 
    right = len(array) - 1 

    while left <= right and target in array:
        mid = (left + right) // 2 

        if array[mid] == target:
            return mid 
        elif array[mid] > target:
            right = mid - 1 
        else:
            left = mid + 1 
    
    return -1 

print(BinarySearchAlgo([1,2,3,4,5], 8)) 