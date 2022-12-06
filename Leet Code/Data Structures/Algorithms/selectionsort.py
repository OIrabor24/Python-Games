#Selection Sort Algorithm
def selection_sort(elements):
    indices = range(0, len(elements) -1)

    for i in indices:
        min_val = i 
    
        for j in range(i+1, len(elements)):
            if elements[j] < elements[min_val]:
                min_val = j 

        if min_val != i:
            elements[min_val], elements[i] = elements[i], elements[min_val]
    
    return elements

print(selection_sort([7,8,9,8,7,6,5,6,7,8,0])) 

def SelectionSort(elements):
    indices = range(0, len(elements) - 1)

    for i in indices:
        min_value = i 

        for j in range(i+1, len(elements)):
            if elements[j] < elements[min_value]:
                min_value = j 
        
        if min_value != i:
            elements[min_value], elements[i] = elements[i], elements[min_value]
    
    return elements

print(SelectionSort([7,8,9,8,7,6,5,6,7,8,0]))

def SelectionSort(elements):
    indices = range(0, len(elements) - 1)

    for i in indices:
        min_val = i

        for j in range(i+1, len(elements)):
            if elements[j] < elements[min_val]:
                min_val = j 

        if min_val != i:
            elements[min_val], elements[i] = elements[i], elements[min_val]
    
    return elements

print(SelectionSort([7,8,9,8,7,6,5,6,7,8,0]))

def selectionsort1(elements):
    indices = range(0, len(elements) - 1)

    for i in indices:
        min_val = i 

        for j in range(i + 1, len(elements)):
            if elements[j] < elements[min_val]:
                min_val = j
        
        if min_val != i:
            elements[min_val], elements[i] = elements[i], elements[min_val]
    
    return elements

print(selectionsort1([7,8,9,8,7,6,5,6,7,8,0]))

def SelectionSort(elements):
    indices = range(0, len(elements))

    for i in indices:
        min_val = i

        for j in range(i+1, len(elements)):
            if elements[j] < elements[min_val]:
                min_val = j 
        
        if min_val != i:
            elements[min_val], elements[i] = elements[i], elements[min_val]

    return elements 

def selection_sort(elements):
    array = len(elements)

    for i in range(array-1):
        min_val = i 

        for j in range(i+1, array):
            if elements[j] < elements[min_val]:
                min_val = j 
        
        if min_val != i:
            elements[min_val], elements[i] = elements[i], elements[min_val]
    
    return elements

print(selection_sort([7,8,9,8,7,6,5,6,7,8,0]))

def SelectionSort(elements):
    array = len(elements)

    for i in range(array):
        min_val = i 

        for j in range(i+1, array):
            if elements[j] < elements[min_val]:
                min_val = j 
        
        if min_val != i:
            elements[min_val], elements[i] = elements[i], elements[min_val]
    
    return elements

print(SelectionSort([7,8,9,8,7,6,5,6,7,8,0]))

def SelectionSort(elements):
    array = len(elements)

    for i in range(array):
        min_val = i 

        for j in range(i+1, array):
            if elements[j] < elements[min_val]:
                min_val = j 
        
        if min_val != i:
            elements[min_val], elements[i] = elements[i], elements[min_val]
    
    return elements

def SelectionSort(elements):
    array = len(elements)

    for i in range(array):
        min_val = i

        for j in range(i+1, array):
            if elements[j] < elements[min_val]:
                min_val = j 
        
        if min_val != i: 
            elements[min_val], elements[i] = elements[i], elements[min_val]
    
    return elements

def SelectionSort(elements):
    array = len(elements)

    for i in range(array):
        min_val = i

        for j in range(i+1, array):
            if elements[j] < elements[min_val]:
                min_val = j 
        
        if min_val != i:
            elements[i], elements[min_val] = elements[min_val], elements[i]
    
    return elements

print(SelectionSort([7,8,9,8,7,6,5,6,7,8,0]))

def SelectionSort(elements):
    array = len(elements)

    for i in range(array):
        min_val = i 

        for j in range(i+1, array):
            if elements[j] < elements[min_val]:
                min_val = j 
        
        if min_val != i:
            elements[i], elements[min_val] = elements[min_val], elements[i]
    
    return elements