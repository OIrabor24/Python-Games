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

def bubblesort4(array):
    indices = len(array) - 1 
    sorted = False 

    while not sorted:
        sorted = True 
        for i in range(0, indices):
            if array[i] > array[i+1]: #if this hold true then list cant be sorted yet!
                sorted = False 
                array[i], array[i+1] = array[i+1], array[i]
    return array 

elements = [5,9,2,1,67,34,88,34, 80]
print("Bubblesort 4:", bubblesort4(elements)) 

def bubblesort5(array):
    indices = len(array) - 1 
    sorted = False 

    while not sorted:
        sorted = True 
        for i in range(0, indices):
            if array[i] > array[i+1]:
                sorted = False #aka these values are unsorted 38 > 6
                array[i], array[i+1] = array[i+1], array[i]
    
    return array

elements = [5,9,2,1,67,34,88,34, 80]
print("Bubblesort 5:", bubblesort4(elements)) 