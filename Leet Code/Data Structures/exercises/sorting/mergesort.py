def merge_sort(array):
    if len(array) <=1:
        return 
    
    mid = len(array) // 2 

    left = array[:mid]
    right = array[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, array)

def merge_two_sorted_lists(a,b,array):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0 
    
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            array[k] = a[i]
            i += 1 
        else:
            array[k] = b[j]
            j += 1 
        k += 1 
    
    while i < len_a:
        array[k] = a[i]
        i += 1 
        k += 1 
    
    while j < len_b:
        array[k] = b[j]
        j += 1 
        k += 1 

a = [17,21,29,38,4,9,25,32]

merge_sort(a)
print(a) 

def merge_sort2(array):
    if len(array) <= 1:
        return 
    mid = len(array) // 2 

    left = array[:mid]
    right = array[mid:]

    merge_sort2(left)
    merge_sort2(right)

    merge_sorted_lists(left, right, array) 

    return array 

def merge_sorted_lists(a,b, array):
    list_a = len(a)
    list_b = len(b)

    i = j = k = 0 

    while i < list_a and j < list_b:
        if a[i] <= b[j]:
            array[k] = a[i]
            i += 1 
        else:
            array[k] = b[j] 
            j += 1
        k += 1 
    
    while i < list_a:
        array[k] = a[i]
        i += 1 
        k += 1 
    
    while j < list_b:
        array[k] = b[j]
        j += 1 
        k += 1 

a = [17,21,29,38,4,9,25,32]
print(merge_sort2(a))  

def MergeSort(array):
    if len(array) <= 1:
        return array 
    mid = len(array) // 2 
    left = array[:mid]
    right = array[mid:] 

    MergeSort(left)
    MergeSort(right)

    MergeLists(left, right, array)

    return array 

def MergeLists(a, b, array):
    list_a = len(a)
    list_b = len(b)

    i = j = k = 0

    while i < list_a and j < list_b:
        if a[i] <= b[j]:
            array[k] = a[i]
            i += 1 
        else:
            array[k] = b[j]
            j += 1 
        k += 1 
    
    while i < list_a:
        array[k] = a[i]
        i += 1 
        k += 1 
    
    while j < list_b:
        array[k] = b[j]
        j += 1 
        k += 1 

a = [17,21,29,38,4,9,25,32, 2, 3]
print(MergeSort(a)) 

tests = [
    [10, 3, 15, 7, 8, 23, 98, 29],
    [],
    [-1],
    [3],
    [9,8,7,2],
    [1,2,3,4,5]
]

for test in tests:
    MergeSort(test)
    print(test) 

def MergeSort2(array):
    if len(array) > 1:
        mid = len(array) // 2 
        left = array[:mid]
        right = array[mid:]

        MergeSort2(left)
        MergeSort2(right)

        i = j = k = 0

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

a = [17,21,29,38,4,9,25,32, 2, 3]
print(MergeSort2(a)) 

tests = [
    [10, 3, 15, 7, 8, 23, 98, 29],
    [],
    [-1],
    [3],
    [9,8,7,2],
    [1,2,3,4,5]
]

for test in tests:
    MergeSort2(test)
    print(test) 

def MergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2 
        left = array[:mid]
        right = array[mid:] 

        MergeSort(left)
        MergeSort(right) 

        i = j = k = 0 

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

a = [17,21,29,38,4,9,25,32, 2, 3]
print(MergeSort(a)) 

tests = [
    [10, 3, 15, 7, 8, 23, 98, 29],
    [],
    [-1],
    [3],
    [9,8,7,2],
    [1,2,3,4,5]
]

for test in tests:
    MergeSort(test)
    print(test) 