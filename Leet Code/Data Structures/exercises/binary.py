from itertools import count


def binary_search(array, target):
    sort_list = sorted(array) 
    left = 0
    right = len(array) - 1 

    while left <= right:
        mid = (left + right) // 2 

        if sort_list[mid] == target:
            return mid 
        elif sort_list[mid] < target:
            left = mid + 1 
        else:
            right = mid - 1 
    
    return -1

# 1. When I try to find number 5 in below list using binary search, 
#it doesn't work and returns me -1 index. Why is that?
# Binary search works with a sorted array
numbers = [1,4,6,9,10,5,7]
print(sorted(numbers)) 
target = 5
index = binary_search(numbers, target) 
print(index) 

def find_all_occurances(array, target):
    index = binary_search(array, target)
    indices = [index] 
    #find indices on left hand side
    i = index -1 

    while i >=0:
        if array[i] == target:
            indices.append(i)
        else:
            break 
        i -= 1
    
    #find indice on right hand side
    i = index + 1 

    while i < len(array):
        if array[i] == target:
            indices.append(i)
        else:
            break 
        i += 1 
    
    return sorted(indices) 
   

# 2. Find index of all the occurances of a number from sorted list
numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
target = 15

indices = find_all_occurances(numbers, target) 
print(f"Indices of occurances of {target} are {indices}") 