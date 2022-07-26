mylist = [1, 2, 3, 4, 6, 5, 9, 10, 1, 4, 3, 15, 16, 25, 5, 2]
sorted_already = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def bubble_sort(array):
    for i in range(len(array)):
        swapped = False
        
        for j in range(0, len(array)- i - 1):
            print(array[j], "compare", array[j + 1], len(array) - i -1)
            if array[j] > array[j + 1]:
                print(array[j], "compare", array[j + 1])
                t = array[j]
                array[j] = array[j + 1]
                array[j + 1] = t

                swapped = True
        if not swapped:
            break
    return array

print(mylist)
sorted_err = bubble_sort(mylist)
print(sorted_err)