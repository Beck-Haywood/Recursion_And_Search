def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # Base case 1 Best case O(1)
    #Worst case O(logn)
    if array[index] == item:
        return index
    # Base case 2
    if index == len(array):
        return 'Not Found!'
    else:   # Recursive Case
        return linear_search_recursive(array, item, index + 1)

def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item, 0, len(array) - 1)


def binary_search_iterative(array, item):
    left = 0
    right = len(array) - 1
    while left <= right:
        midpoint = int((left + right) // 2)
        # If item is at midpoint
        if array[midpoint] == item:
            return array.index(item)
        # If item is <, ignore right half
        elif item < array[midpoint]:
            right = midpoint - 1
        # If item is >, ignore left half
        elif item > array[midpoint]:
            left = midpoint + 1
    return None
array = []
def binary_search_recursive(array, item, left, right):
    # Base case
    if left > right:
        return None
    else:
        midpoint = (left + right) // 2
        # If item is at midpoint
        if array[midpoint] == item:
            return array.index(item)
        # If item is <, ignore right half
        elif item < array[midpoint]:
            return binary_search_recursive(array, item, left, midpoint - 1)
        # If item is >, ignore left half
        elif item > array[midpoint]:
            return binary_search_recursive(array, item, midpoint + 1, right)
        
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests

if __name__ == '__main__':
    array = ['a','b','c','d','e']
    item = 'b'
    print(binary_search_recursive(array, item, 0, len(array) - 1))
