#Author: Youngjoo Lee
#Date: 02/19/2022
#Purpose: Create the sorting function and its components

#Purpose: function that compares two integers or floats
def compare_ints_floats(a, b):
    return a <= b

#Purpose: function that compares two strings
def compare_strings(a, b):
    return a.lower() <= b.lower()


#Purpose: returns a list in which the chosen pivot number is placed in the list so that numbers <= are in front
# and numbers > are after in the list
def partition(the_list, p, r, compare_func):

    i = p - 1
    j = p
    pivot = the_list[r] #inclusive of r

    while j < r:
        if compare_func(the_list[j], pivot):
            i += 1
            temp = the_list[i]
            the_list[i] = the_list[j]
            the_list[j] = temp
            j += 1
        else:
            j += 1 #case where the_list[j] > pivot

    temp = the_list[i+1]
    the_list[i+1] = pivot
    the_list[r] = temp

    return i + 1


#DRIVER
# list = [0, 9, 4, 8, 10, 2, 5, 440, -100, 300, 234, 1, 54, 10]
#
# print(partition(list, 0, 9, compare_ints_floats))
# print(list)

#Purpose: Given the_list with length > 1, return sorted list
def quicksort(the_list, p, r, compare_func):
    if p < r:
        q = partition(the_list, p, r, compare_func)

        quicksort(the_list, p, q - 1, compare_func) #quicksort is inclusive of the r parameter
        quicksort(the_list, q, r, compare_func)



#Purpose: makes a call to the quicksort function to sort the entire list referenced by the_list
def sort(the_list, compare_func):
    quicksort(the_list, 0, len(the_list) - 1, compare_func)
