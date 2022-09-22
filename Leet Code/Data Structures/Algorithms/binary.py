def linear_search(array, target):
    for index, element in enumerate(array):
        if element == target:
            return index 
    return -1

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