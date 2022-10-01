def InsertionSort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1 # one less than the current elements

        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j - 1
        elements[j+1] = anchor 

elements = [11,9,29,7,2,15,28]

InsertionSort(elements)
print(elements) 

def insertion_sort(list_a):
    indexing_length = range(1, len(list_a))
    for i in indexing_length:
        value_to_sort = list_a[i]

        while list_a[i-1] > value_to_sort and i>0:
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i = i -1

    return list_a

def InsertionSort2(elements):
    indices = range(1, len(elements)) 

    for i in indices:
        while elements[i-1] > elements[i] and i > 0:
            elements[i], elements[i-1] = elements[i-1], elements[i]
            i -= 1 
    return elements

tests = [
    [],
    [-1],
    [0],
    [-1, -5, -4, -9, -3, -2, -6],
    [6, 4, 5, 0, 3, 2, 1, 7, 88, 55, 99]
]

for test in tests:
    InsertionSort2(test)
    print(test) 

def insertionsort(elements):
    indices = range(1, len(elements))
    for i in indices:
        while elements[i-1] > elements[i] and i > 0:
            elements[i], elements[i-1] = elements[i-1], elements[i]
            i -= 1 
    return elements

for test in tests:
    insertionsort(test)
    print(test) 

def Insertion3(elements):
    indices = range(1, len(elements))

    for i in indices:
        while elements[i-1] > elements[i] and i > 0:
            elements[i], elements[i-1] = elements[i-1], elements[i]
            i -= 1
    return elements

for test in tests:
    Insertion3(test)
    print(test) 


def InsertionSort(elements):
    indices = range(1, len(elements))

    for i in indices:
        while elements[i-1] > elements[i] and i > 0:
            elements[i], elements[i-1] = elements[i-1], elements[i]
            i -= 1
    return elements

def InsertionSort(elements):
    indices = range(1, len(elements))

    for i in indices:
        while elements[i-1] > elements[i] and i > 0:
            elements[i], elements[i-1] = elements[i-1], elements[i] 
            i -= 1 
    return elements

print(InsertionSort(elements =[11,9,29,7,2,15,28]))

def insertionsort(array):
    indices = range(1, len(array))

    for i in indices:
        while array[i-1] > array[i] and i > 0:
            array[i], array[i-1] = array[i-1], array[i]
            i -= 1 
    return array 

print(insertionsort([11,9,29,7,2,15,28]))  

def InsertionSort4(arr):
    indices = range(1, len(arr))

    for i in indices:
        while arr[i-1] > arr[i] and i > 0:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1 
    return arr 

def InsertionSort5(array):
    indices = range(1, len(array))

    for i in indices:
        while array[i-1] > array[i] and i > 0:
            array[i], array[i-1] = array[i-1], array[i]
            i -= 1 
    return array 

tests = [
    [],
    [-1],
    [0],
    [-1, -5, -4, -9, -3, -2, -6],
    [6, 4, 5, 0, 3, 2, 1, 7, 88, 55, 99]
]
for test in tests:
    InsertionSort5(test)
    print(test) 