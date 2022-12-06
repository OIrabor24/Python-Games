#Quicksort = Pivot
#1. pivot is in correct position in final, sorted array
#2. pivot items to the left are smaller
#3. pivot items to the right are larger
#[2, 6, 5, 3, 0, 8, 7, 1]

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

def QuickSort(elements):
    length = len(elements)

    if length <= 1:
        return elements
    else:
        pivot = elements.pop()
    
    items_g = []
    items_l = []

    for item in elements:
        if item > pivot:
            items_g.append(item)
        else:
            items_l.append(item)
    
    return QuickSort(items_l) + [pivot] + QuickSort(items_g)

print(QuickSort([5,7,0,9,4,6,5,1,3,2]))

def QuickSort(elements):
    array = len(elements)

    if array <= 1:
        return elements
    else:
        pivot = elements.pop()
    
    items_g = []
    items_l = []

    for item in elements:
        if item > pivot:
            items_g.append(item)
        else:
            items_l.append(item)
    
    return QuickSort(items_l) + [pivot] + QuickSort(items_g)

print(QuickSort([5,7,0,9,4,6,5,1,3,2]))

from random import randint
def quicksort(array):
    if len(array) < 2:
        return array 
    
    low, same, high = [], [], []

    pivot = array[randint(0, len(array) -1)] 

    for item in array:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        else:
            high.append(item)
    
    return quicksort(low) + same + quicksort(high) 

print(quicksort([5,7,0,9,4,6,5,1,3,2]))

def QuickSort(array):
    if len(array) <= 1:
        return array 
    else:
        pivot = array.pop()
    
    low, high = [], []

    for item in array:
        if item < pivot:
            low.append(item)
        else:
            high.append(item)
    
    return QuickSort(low) + [pivot] + QuickSort(high) 

print(QuickSort([5,7,0,9,4,6,5,1,3,2]))

def Quicksort2(array):
    if len(array) <= 1:
        return array 
    else:
        pivot = array.pop()

    low, high = [], []

    for item in array:
        if item < pivot:
            low.append(item)
        else:
            high.append(item)
    
    return Quicksort2(low) + [pivot] + Quicksort2(high) 

print(Quicksort2([5,7,0,9,4,6,5,1,3,2]))

def QuickSort3(array):
    if len(array) <= 1:
        return array 
    else:
        pivot = array.pop()
    
    low, high = [], []

    for item in array:
        if item < pivot:
            low.append(item)
        else:
            high.append(item)
    
    return QuickSort3(low) + [pivot] + QuickSort3(high) 

print(QuickSort3([5,7,0,9,4,6,5,1,3,2]))

def QuickSort(array):
    if len(array) <= 1:
        return array 
    else:
        pivot = array.pop()
    
    left, right = [], []

    for i in array:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)
    
    return QuickSort(left) + [pivot] + QuickSort(right) 

print(QuickSort([5,7,0,9,4,6,5,1,3,2]))
