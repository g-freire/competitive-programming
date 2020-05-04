#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

"""
BUBBLE SORT IMPLEMENTATION
ADVANTAGES: simplicity, didatic
DESADVANTAGES:    slow, 0(n^2)
"""


def bubble_sort(array):
    n = len(array)

    for i in range(n):
        # Create a flag that will allow the function to
        # terminate early if there's nothing left to sort
        already_sorted = True

        # Start looking at each item of the list one by one,
        # comparing it with its adjacent value. With each
        # iteration, the portion of the array that you look at
        # shrinks because the remaining items have already been
        # sorted.
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                # If the item you're looking at is greater than its
                # adjacent value, then swap them
                array[j], array[j + 1] = array[j + 1], array[j]

                # Since you had to swap two elements,
                # set the `already_sorted` flag to `False` so the
                # algorithm doesn't finish prematurely
                already_sorted = False

        # If there were no swaps during the last iteration,
        # the array is already sorted, and you can terminate
        if already_sorted:
            break

    return array

if __name__ == '__main__':
    input_value = [5,1, 5, 9, 3, 8, 12, 2, 120, 130]
    a = bubble_sort(input_value)
    print(*a)



