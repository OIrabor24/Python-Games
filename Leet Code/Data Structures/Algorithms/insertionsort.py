def InsertionSort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1 # one less than the current elements

        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j - 1
        elements[j+1] = anchor 
    
    return elements

elements = [11,9,29,7,2,15,28]

InsertionSort(elements)
print(elements) 

def InsertionSort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        
        while elements[i-1] > anchor and i > 0:
            elements[i], elements[i-1] = elements[i-1], elements[i]
            i -= 1 
    return elements

print(InsertionSort(elements))


def insertion_sort(list_a):
    indexing_length = range(1, len(list_a))
    for i in indexing_length:
        value_to_sort = list_a[i]

        while list_a[i-1] > value_to_sort and i > 0:
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i = i -1

    return list_a

def InsertionSort2(elements):
    indices = range(1, len(elements))

    for i in indices:
        sort_val = elements[i]
        while elements[i-1] > sort_val and i > 0:
            elements[i], elements[i-1] = elements[i-1], elements[i]
            i -= 1 
    return elements

print(InsertionSort2([11,9,29,7,2,15,28]))

def InsertionSort3(elements):
    indices = range(1, len(elements))

    for i in indices:
        sort_val = elements[i]
        while elements[i-1] > sort_val and i > 0:
            elements[i-1], elements[i] = elements[i], elements[i-1]
            i -= 1 
    return elements
print(InsertionSort3([11,9,29,7,2,15,28,1,5,0]))


tests = [
    [],
    [-1],
    [0],
    [-1, -5, -4, -9, -3, -2, -6],
    [6, 4, 5, 0, 3, 2, 1, 7, 88, 55, 99]
]


def InsertionSort(array):
    for i in range(1, len(array)):
        value_to_sort = array[i]

        while array[i-1] > value_to_sort and i > 0:
            array[i-1], array[i] = array[i], array[i-1]
            i -= 1 
    
    return array 

for test in tests:
    print(InsertionSort(test))

def InsertionSort(elements):
    for i in range(1, len(elements)):
        val_sort = elements[i] 

        while elements[i-1] > val_sort and i > 0:
            elements[i-1], elements[i] = elements[i], elements[i-1]
            i -= 1 
    
    return elements

print(InsertionSort([11,9,29,7,2,15,28,1,5,0])) 

def InsertionSort(array):
    for i in range(1, len(array)):
        sort_val = array[i]

        while array[i-1] > sort_val and i > 0:
            array[i-1], array[i] = array[i], array[i-1]
            i -= 1 
    
    return array 

def InsertionSort(elements):
    indices = len(elements)

    for i in range(1, indices):
        sorted_val = elements[i]

        while elements[i-1] > sorted_val and i > 0:
            elements[i], elements[i-1] = elements[i-1], elements[i]
            i -= 1 
    
    return elements

