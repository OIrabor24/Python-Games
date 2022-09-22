def InsertionSort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1 # one less than the current elements

        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j - 1
        elements[j+1] = anchor 

