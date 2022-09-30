#Version 1
def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, arr)

def merge_two_sorted_lists(a,b,arr):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1

    while i < len_a:
        arr[k] = a[i]
        i+=1
        k+=1

    while j < len_b:
        arr[k] = b[j]
        j+=1
        k+=1



#Version 2
def mergesort(array):
    if len(array) > 1:
        mid = len(array) // 2 
        left = array[:mid]
        right = array[mid:] 

        #recursive call on each half
        mergesort(left)
        mergesort(right) 

        # Two iterators for traversing the two halves
        i = 0 
        j = 0 

        # Iterator for the main array/list
        k = 0 

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                #The value from the left half has been used
                array[k] = left[i] 
                #Move the iterator forward
                i += 1 
            else:
                array[k] = right[j] 
                j += 1 
            #Move to the next slot
            k += 1 

        # For all the remaining values 
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
a = mergesort(array) 
print(a) 
    


# test_cases = [
#     [10, 3, 15, 7, 8, 23, 98, 29],
#     [],
#     [9, 8, 7, 2],
#     [1, 2, 3, 4, 5] 
# ]

# for arr in test_cases:
#     merge_sort(arr)
#     print(arr) 