#Quicksort = Pivot
#1. pivot is in correct position in final, sorted array
#2. pivot items to the left are smaller
#3. pivot items to the right are larger
#[2, 6, 5, 3, 0, 8, 7, 1]
from operator import le


def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item) 
        
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater) 

print(quick_sort([5,7,0,9,4,6,5,1,3,2]))

def quicksort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
    
    items_greater = []
    items_lower = [] 

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return quicksort(items_lower) + [pivot] + quicksort(items_greater)

print('-' * 30)
print(quicksort([5,7,0,9,4,6,5,1,3,2]))


def quicksort3(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop() 
    
    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item) 
    
    return quicksort3(items_lower) + [pivot] + quicksort3(items_greater) 

print('-' * 30)
print(quicksort3([5,7,0,9,4,6,5,1,3,2]))

def quicksort4(elements):
    length = len(elements)

    if length <= 1:
        return elements
    else:
        pivot = elements.pop()
    
    items_greater = []
    items_lower = []

    for item in elements:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    
    return quicksort4(items_lower) + [pivot] + quicksort4(items_greater)

print(quicksort4([5,7,0,9,4,6,5,1,3,2]))