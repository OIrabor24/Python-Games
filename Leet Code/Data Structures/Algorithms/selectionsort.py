
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
    indices = range(0, len(elements) -1)

    for i in indices:
        min_val = i 

        for j in range(i+1, len(elements)):
            if elements[j] < elements[min_val]:
                min_val = j 
        
        if min_val != i:
            elements[min_val], elements[i] = elements[i], elements[min_val]
    
    return elements

def selectionsort(elements):
    indices = range(0, len(elements) -1)

    for i in indices:
        min_val = i 

        for j in range(i+1, len(elements)):
            if elements[j] < elements[min_val]:
                min_val = j 
        
        if min_val != i:
            elements[min_val], elements[i] = elements[i], elements[min_val] 

    return elements


def Selection_sort(elements):
    indices = range(0,len(elements) - 1)

    for i in indices:
        min_val = i 

        for j in range(i+1, len(elements)):
            if elements[j] < elements[min_val]:
                min_val = j 
        
        if min_val != i:
            elements[min_val], elements[i] = elements[i], elements[min_val]
    
    return elements 

def selectionsort(elements):
    indices = range(0, len(elements) -1)

    for i in indices:
        min_val = i

        for j in range(i+1, len(elements)):
            if elements[j] < elements[min_val]:
                min_val = j 
        
        if min_val != i:
            elements[min_val], elements[i] = elements[i], elements[min_val] 
    
    return elements 

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