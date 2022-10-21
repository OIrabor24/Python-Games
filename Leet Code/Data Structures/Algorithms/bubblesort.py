def bubble_sort(elements):
    size = len(elements)
    
    for i in range(size - 1):
        swapped = False
        for j in range(size - 1):
            if elements[j] > elements[j + 1]:
                temp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = temp 
                swapped = True 
        if not swapped:
            break 

elements = [5,9,2,1,67,34,88,34]
print(bubble_sort(elements))
print(elements)

def bubble(list_a):
    indexing_length = len(list_a) - 1 #SCan not apply comparision starting with last item of list (No item to right)
    sorted = False #Create variable of sorted and set it equal to false

    while not sorted:  #Repeat until sorted = True
        sorted = True  # Break the while loop whenever we have gone through all the values

        for i in range(0, indexing_length): # For every value in the list
            if list_a[i] > list_a[i+1]: #if value in list is greater than value directly to the right of it,
                sorted = False # These values are unsorted
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i] #Switch these values
    return list_a # Return our list "unsorted_list" which is not sorted.

def bubble_sort2(array):
    idx = len(array) - 1 
    sorted = False 

    while not sorted:
        sorted = True 
        for i in range(0, idx):
            if array[i] > array[i+1]:
                sorted = False 
                array[i], array[i+1] = array[i+1], array[i]
    return array 

elements = [5,9,2,1,67,34,88,34]
print("Bubble sort 2:", bubble_sort2(elements)) 

def BubbleSort(array):
    indices = len(array) - 1 
    sorted = False 

    while not sorted:
        sorted = True 
        for i in range(0, indices):
            if array[i] > array[i+1]:
                sorted = False 
                array[i], array[i+1] = array[i+1], array[i]
    return array 

elements = [5,9,2,1,67,34,88,34, 80]
print("Bubblesort 3:", BubbleSort(elements)) 

def BubbleSort(elements):
    array = len(elements) - 1 
    sorted = False 

    while not sorted:
        sorted = True 
        for i in range(array):
            if elements[i] > elements[i+1]:
                sorted = False 
                elements[i], elements[i+1] = elements[i+1], elements[i]
    return elements

print("BubbleSort:", BubbleSort([5,9,2,1,67,34,88,34, 80]))

def bubble_sort(array):
    n = len(array) - 1 
    sorted_ = False 

    while not sorted_:
        sorted_ = True 
        for i in range(n):
            if array[i] > array[i+1]:
                sorted_ = False 
                array[i], array[i+1] = array[i+1], array[i]
    
    return array 

print("bubble_sort:", bubble_sort([5,9,2,1,67,34,88,34, 80]))


def BubbleSortRP(array): #real python
    n = len(array)

    for i in range(n):
        #create a flag that allows the func to terminate
        #early if there's nothing left to sort
        already_sorted = True 

        for j in range(n - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                already_sorted = False 
        
        if already_sorted:
            break 
    
    return array 

print(BubbleSortRP([5,9,2,1,67,34,88,34, 80]))


rp =  [0.009201999986544251, ]
easy = [0.009011399990413338]

if easy < rp:
    print("use easy implementation.")
else:
    print("good to know, but doesn't really matter.")


def Bubble_Sort(array):
    n = len(array) - 1 
    sorted_val = False 

    while not sorted_val:
        sorted_val = True 
        for i in range(n):
            if array[i] > array[i+1]:
                sorted_val = False 
                array[i], array[i+1] = array[i+1], array[i]

    return array 

print(Bubble_Sort([5,9,2,1,67,34,88,34, 80]))

def BubbleSortCuh(array):
    arr = len(array) - 1 
    sorted_ = False 

    while not sorted_:
        sorted_ = True 
        for i in range(arr):
            if array[i] > array[i+1]:
                sorted_ = False 
                array[i], array[i+1] = array[i+1], array[i]
    
    return array 

print(BubbleSortCuh([5,9,2,1,67,34,88,34, 80]))