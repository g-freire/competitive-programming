#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

"""
Hash Search simple solution
"""

class HashSearch:
    def Solution(self, input_data, searchValue ):
        print("Starting Solution 1 ")
        start = time.time()
        names = input_data
        # mapping / hashing
        index_by_name = {
                name: index for index, name in enumerate(names)
                }

        if searchValue in index_by_name:
            return index_by_name[searchValue]

        print("Algorithm took: ", time.time() - start, " seconds")
        print("*" * 200)

    # 2) It's unnecessary to continue checking for other possible values of d. Only one could work, since the
if __name__ == '__main__':
    print("*" * 200)
    input_data = ["j","e","d","b","a","f","e"]
    result_index = HashSearch().Solution(input_data,searchValue="a")
    search_result = input_data[result_index]
