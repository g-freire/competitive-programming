"""
MERGE SORT IMPLEMENTATION
ADVANTAGES: fast, 0(n logn), parallel
DISADVANTAGES:    slow for small inputs, recursion creates copies
"""


from random import randint

def quicksort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    # HERE WE COULD USE THE MEDIAN TO HAVE BEST CASE ->  O(n) + O(n log2n) = O(nlog2n)
    pivot = array[randint(0, len(array) - 1)]

    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quicksort(low) + same + quicksort(high)

if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 100 ,9,7]
    print("Given array is", end="\n")
    print(*arr)
    quicksort(arr)
    print("Sorted array is: ", end="\n")
    print(*arr)