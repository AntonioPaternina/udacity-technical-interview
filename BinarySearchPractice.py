"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    # determine center value
    size = len(input_array)
    return binary_search_compute(input_array, value, 0, size - 1)

def binary_search_compute(input_array, value, start, end):
    size = end - start + 1
    current_index = None
    if size % 2 == 0:
        current_index = start + (size / 2) - 1
    else:
        current_index = start + (size / 2)
    # test center value
    if value == input_array[current_index]:
        return current_index
    elif size == 1:
        return -1
    elif size == 2:
        if input_array[start + 1] == value:
            return start + 1
        else:
            return -1
    elif value > input_array[current_index]:
        return binary_search_compute(input_array, value, current_index, end)
    else:
        return binary_search_compute(input_array, value, start, current_index)

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
