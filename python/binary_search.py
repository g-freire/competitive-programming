#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

"""
Binary Search simple solution
"""

class BinarySearch:


    def Solution1(self, searchValue ):
        print("Starting Solution 1 - Brute Force Solution - O(n^4)")
        start = time.time()
        sortedArray = [2, 4, 8, 9, 22, 28, 29, 33, 35, 44, 49, 88, 105, 255, 664, 888, 1111]
        low = 0;
        high = len(sortedArray) - 1
        while low <= high:
            mid = (low + high//2)
            a = sortedArray[mid]
            b = searchValue
            if sortedArray[mid] == searchValue:
                return mid
            elif sortedArray[mid] < searchValue:  # increase the minimum - left to right
                low = mid + 1
            elif sortedArray[mid] > searchValue: # decrease the max - right to left
                high = mid - 1









        print("Algorithm took: ", time.time() - start, " seconds")
        print("*" * 200)

    # 2) It's unnecessary to continue checking for other possible values of d. Only one could work, since the
if __name__ == '__main__':
    print("*" * 200)
    BinarySearch().Solution1(searchValue=22)

