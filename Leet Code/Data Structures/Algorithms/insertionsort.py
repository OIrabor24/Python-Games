
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

def insertion_sort(elements):
    indices = range(1, len(elements))

    for i in indices:
        value_to_sort = elements[i]

        while elements[i-1] > value_to_sort and i > 0:
            elements[i], elements[i -1] = elements[i -1], elements[i]
            i = i - 1 
    return elements

print(insertion_sort([3, 2, 5, 7, 4]))



def insertion_sort3(elements):
    indices = range(1, len(elements))

    for i in indices:
        value_to_sort = elements[i]

        while elements[i-1] > value_to_sort and i > 0:
            elements[i-1], elements[i] = elements[i], elements[i-1]
            i -= 1 
    return elements

 
print(insertion_sort3([3, 2, 5, 7, 4]))
            

def insertion_sort4(elements):
    indices = range(1, len(elements))

    for i in indices:
        value_to_sort = elements[i]
        while elements[i-1] > value_to_sort and i > 0:
            elements[i], elements[i-1] = elements[i-1], elements[i]
            i -= 1 
    return elements

print(insertion_sort4([3, 2, 5, 7, 4])) 

def insertion_sort5(elements):
    indices = range(1, len(elements))

    for i in indices:
        value_to_sort = elements[i]
        while elements[i-1] > value_to_sort and i > 0:
            elements[i], elements[i-1] = elements[i-1], elements[i]
            i -= 1 
    return elements
print(insertion_sort5([3, 2, 5, 7, 4]))

def insertion_sort6(elements):
    indices = range(1, len(elements))

    for i in indices:
        value_to_sort = elements[i]
        while elements[i-1] > value_to_sort and i > 0:
            elements[i], elements[i-1] = elements[i-1], elements[i]
            i -= 1 
    return elements
print(insertion_sort6([3, 2, 5, 7, 4]))

def insertion_sort7(elements):
    indices = range(1, len(elements))
    for i in indices:
        value_to_sort = elements[i]
        while elements[i-1] > value_to_sort and i > 0:
            elements[i], elements[i-1] = elements[i-1], elements[i]
            i-= 1 
    return elements

print(insertion_sort7([3, 2, 5, 7, 4]))