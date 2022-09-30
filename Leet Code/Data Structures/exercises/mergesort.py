#left: [3, 5, 4, 1] right: [7, 5, 6, 8]
# K: [1, 3, 4, 5, 5, 6, 7, 8]
def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2 
        left = array[:mid]
        right = array[mid:]  

        #recursive call on each half
        merge_sort(left)
        merge_sort(right) 
        # Two iterators for traversing the two halves
        i = 0 
        j = 0
        # New Iterator for the main array/list
        k = 0 
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1 #Move the iterator forward
            else:
                array[k] = right[j]
                j += 1 
            k += 1 #Move to the next slot

        while i < len(left):
            array[k] = left[i]
            i += 1 
            k += 1 
        
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1 
        # For all the remaining values 
    return array 

array = [54,26,93,17,77,31,44,55,20]
a = merge_sort(array) 
print(a) 

#steps:
#recursive call on each half
#Two iterators for traversing the two halves
#New Iterator for the main array/list
#Move the iterator forward
#Move to the next slot
#For all the remaining values 

def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right) 

        i = 0
        j = 0
        k = 0 

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1 
            else:
                array[k] = right[j]
                j += 1 
            k += 1 
        
        while i < len(left):
            array[k] = left[i]
            i += 1 
            k += 1
        
        while j < len(right):
            array[k] = right[j] 
            j += 1 
            k += 1
    return array 

array = [54,26,93,17,77,31,44,55,20, 99, 1] 
a = merge_sort(array) 
print(a) 




elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]
x = len(elements)
print(elements[0]['name']) 

def mergesort(elements, key, descending=False):
    size = len(elements)

    if size == 1:
        return elements 
    
    left_list = mergesort(elements[0:size//2], key, descending)
    right_list = mergesort(elements[size // 2:], key, descending) 
    sorted_list = merge(left_list, right_list, key, descending) 

    return sorted_list 


def merge(left_list, right_list, key, descending=False):
    merged = [] 
    if descending:
        while len(left_list) > 0 and len(right_list) > 0:
            if left_list[0][key] >= right_list[0][key]:
                merged.append(left_list.pop(0)) 
            else:
                merged.append(right_list.pop(0)) 
    
    else:
        while len(left_list) > 0 and len(right_list) > 0:
            if left_list[0][key] <= right_list[0][key]:
                merged.append(left_list.pop(0))
            else:
                merged.append(right_list.pop(0)) 
    
    merged.extend(left_list)
    merged.extend(right_list)
    return merged 

elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]

sorted_list = mergesort(elements, key='name', descending=True) 
print(sorted_list) 

#steps:
#recursive call on each half
#Two iterators for traversing the two halves
#New Iterator for the main array/list
#Move the iterator forward
#Move to the next slot
#For all the remaining values 

def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2 
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right) 

        i = 0 
        j = 0 
        k = 0 

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i] 
                i += 1 
            else:
                array[k] = right[j]
                j += 1 
            k += 1 
        
        while i < len(left):
            array[k] = left[i]
            i += 1 
            k += 1 
        
        while j < len(right):
            array[k] = right[j]
            j += 1 
            k += 1
    
    return array 

array = [54,26,93,17,77,31,44,55,20]
a = merge_sort(array) 
print(a) 

def mergesort1(array):
    if len(array) > 1:
        mid = len(array) // 2 
        left = array[:mid]
        right = array[mid:] 

        mergesort1(left)
        mergesort1(right) 

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i] 
                i += 1
            else:
                array[k] = right[j]
                j += 1 
            k += 1 
        
        while i < len(left):
            array[k] = left[i]
            i += 1 
            k += 1 
        
        while j < len(right):
            array[k] = right[j] 
            j += 1
            k += 1 

    return array  

array = [54,26,93,17,77,31,44,55,20,1,3,88,64,99]
print(mergesort1(array)) 

tests = [
    [],
    [1, 2, 3, 4, 5,],
    [4, 5, 3, 1, 2, 0, 9, 19, 7, 5, 6],
    [1],
    [-1] 
]

for test in tests:
    mergesort1(test) 
    print(test) 

print('-' * 40)
def mergesort2(array):
    if len(array) > 1:
        mid = len(array) // 2 
        left = array[:mid]
        right = array[mid:]

        mergesort2(left)
        mergesort2(right)

        i = 0
        j = 0 
        k = 0 

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1 
            else:
                array[k] = right[j]
                j += 1
            k += 1 
        
        while i < len(left):
            array[k] = left[i]
            i += 1 
            k += 1 
        
        while j < len(right):
            array[k] = right[j]
            j += 1 
            k += 1 
        
    return array 

array = [54,26,93,17,77,31,44,55,20,1,3,88,64,99]
print(mergesort2(array)) 

tests = [
    [],
    [1, 2, 3, 4, 5,],
    [4, 5, 3, 1, 2, 0, 9, 19, 7, 5, 6],
    [1],
    [-1] 
]

for test in tests:
    mergesort2(test) 
    print(test) 

def mergesort3(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        mergesort3(left)
        mergesort3(right)

        i = 0 
        j = 0
        k = 0 

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    return array 

array = [54,26,93,17,77,31,44,55,20,1,3,88,64,99]
print(mergesort3(array)) 

tests = [
    [],
    [1, 2, 3, 4, 5,],
    [4, 5, 3, 1, 2, 0, 9, 19, 7, 5, 6],
    [1],
    [-1] 
]

for test in tests:
    mergesort3(test) 
    print(test) 


def mergesort4(array):
    if len(array) > 1:
        mid = len(array) // 2 
        left = array[:mid]
        right = array[mid:]

        mergesort4(left)
        mergesort4(right) 

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i] 
                i += 1 
            else:
                array[k] = right[j]
                j += 1 
            k += 1 
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1 
        while j < len(right):
            array[k] = right[j]
            j += 1 
            k += 1 
    return array 

array = [54,26,93,17,77,31,44,55,20,1,3,88,64,99]
print(mergesort4(array)) 

tests = [
    [],
    [1, 2, 3, 4, 5,],
    [4, 5, 3, 1, 2, 0, 9, 19, 7, 5, 6],
    [1],
    [-1] 
]

for test in tests:
    mergesort4(test)
    print(test) 

def mergesort5(array):
    if len(array) > 1:
        mid = len(array) // 2 
        left = array[:mid]
        right = array[mid:] 

        mergesort5(left)
        mergesort5(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j] 
                j += 1 
            k += 1 
        
        while i < len(left):
            array[k] = left[i]
            i += 1 
            k += 1 
        while j < len(right):
            j += 1 
            k += 1 

    return array 

array = [54,26,93,17,77,31,44,55,20,1,3,88,64,99]
print(mergesort5(array)) 