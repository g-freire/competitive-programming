#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

"""
INSERT SORT IMPLEMENTATION

Builds the sorted list one element at a time by comparing each item with the rest of the list and inserting it into its correct position. 
Some quicksort implementations even use insertion sort internally if the list is small enough to provide a faster overall implementation. 

ADVANTAGES: simplicity, good for small lists
DISADVANTAGES:    slow for big lists, 0(n^2)
"""


def insertion_sort(array):
    # Loop from the second element of the array until
    # the last element
    for i in range(1, len(array)):
        # This is the element we want to position in its
        # correct place
        key_item = array[i]

        # Initialize the variable that will be used to
        # find the correct position of the element referenced
        # by `key_item`
        j = i - 1

        # Run through the list of items (the left
        # portion of the array) and find the correct position
        # of the element referenced by `key_item`. Do this only
        # if `key_item` is smaller than its adjacent values.
        while j >= 0 and array[j] > key_item:
            # Shift the value one position to the left
            # and reposition j to point to the next element
            # (from right to left)
            array[j + 1] = array[j]
            j -= 1

        # When you finish shifting the elements, you can position
        # `key_item` in its correct location
        array[j + 1] = key_item

    return array

if __name__ == '__main__':
    input_value = [5,1, 5, 9, 3, 8, 12, 2, 120, 130]
    a = insertion_sort(input_value)
    print(*a)



