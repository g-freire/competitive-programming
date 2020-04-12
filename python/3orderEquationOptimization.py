#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

"""
Optimization example from the Crack the Coding Interview.

The solutions goes to O(n'4) to a Parallel O(n^2)

Problem - Print all positive integer solutions to the equation a3 + b3 = c3 + d3
where a,b,c,d are integers between 1 and 1000.

"""

class PositiveSolutionsToPowerOf3Equation:

    # 1) Brute Force Solution - O(n^4)
    def Solution1(self, range_of_solution=1000):
        print("Starting Solution 1 - Brute Force Solution - O(n^4)")
        start = time.time()
        solution = []
        for a in range(1, range_of_solution):
            for b in range(1, range_of_solution):
                for c in range(1, range_of_solution):
                    for d in range(1, range_of_solution):
                        if pow(a, 3) + pow(b, 3) == pow(c, 3) + pow(d, 3):
                            solution.append(1)
                            # print(" Solution :", a, b, c, d)

        print("Solution len: ", len(solution))
        print("Algorithm took: ", time.time() - start, " seconds")
        print("*" * 200)


    # 2) It's unnecessary to continue checking for other possible values of d. Only one could work, since the
    # combination is unique, so we add a break at line 38
    def Solution2(self, range_of_solution=1000):
        print("Starting  ", "Solution 2 - Break Unique Value")
        start = time.time()
        solution = []
        for a in range(1, range_of_solution):
            for b in range(1, range_of_solution):
                for c in range(1, range_of_solution):
                    for d in range(1, range_of_solution):
                        if pow(a, 3) + pow(b, 3) == pow(c, 3) + pow(d, 3):
                            solution.append(1);
                            # print(" Solution :", a, b, c, d)
                            break

        print("Solution len: ", len(solution))
        print("Algorithm took: ", time.time() - start, " seconds")
        print("*" * 200)

    #TODO - 19883 != 19863 - more result than n^4 solution 
    # 3) If there's only one valid d value for each (a, b, c), then we can just compute it, instead of
    # partially traversing the array - isolating the terms we have d = (a^3 + b^3 - c^3) ^ 1/3. This will
    # avoid the d loop, making it O(n^3)
    def Solution3(self, range_of_solution=1000):
        print("Starting  ", "Solution 3 - Isolating the d value")
        start = time.time()
        solution = []
        for a in range(1, range_of_solution):
            for b in range(1, range_of_solution):
                for c in range(1, range_of_solution):
                    # d = int(abs(pow(pow(a, 3) + pow(b, 3) - pow(c, 3), 1/3))) # BEWARE!! casting to int will truncate the values
                    d = round(abs(pow(pow(a, 3) + pow(b, 3) - pow(c, 3), 1/3)))
                    if pow(a, 3) + pow(b, 3) == pow(c, 3) + pow((d), 3):
                            solution.append(1);
                            # print(" Solution :", a, b, c, (d))

        print("Solution len: ", len(solution))
        print("Algorithm took: ", time.time() - start, " seconds")
        print("*" * 200)

    # Parallel Choice
    # 4) Why do we keep on computing all (c, d) pairs for each (a, b) pair? We should just create the list of ( c,
    # d) pairs once. Then, when we have an (a, b) pair, find the matches within the ( c, d) list. We can quickly
    # locate the matches by inserting each (c, d) pair into a hash table that maps from the sum to the pair (or,
    # rather, the list of pairs that have that sum).
    def Solution4(self, range_of_solution=1000):
        print("Starting  ", "Solution 4 - Divide in pairs and hashtable the search match")
        start = time.time()
        solution = []
        hash_table = {}

        # Creating the hash table  -  O(n^2)  - schema: {"9":[ (1,2), (2,1)] , ...]
        for a in range(1, range_of_solution):
            for b in range(1, range_of_solution):
                result = pow(a, 3) + pow(b, 3)
                if result not in hash_table: # could also use collections.defaultdict(list) instead of the if/else solution
                    hash_table[result] = [(a, b)]
                else:
                    hash_table[result].append((a, b))

        # Mathing w/ the hash table  -  O(n^2)
        for c in range(1, range_of_solution):
            for d in range(1, range_of_solution):
                result = pow(c,3) + pow(d,3)
                list_result = hash_table[result]
                for pair in list_result: # this for loop is not relevant, since only iterates after the hashtable lookup
                    # print(c, d, *pair)
                    solution.append(1)
        print("Solution len: ", len(solution))
        print("Algorithm took: ", time.time() - start, " seconds")
        print("*" * 200)

    #TODO - fix 19323 != 19863 - less result than n^4 solution 
    # 5) Actually, once we have the map of all the (c, d) pairs, we can just use that directly. We don't need to
    # generate the (a, b) pairs. Each (a, b) will already be in the map.
    def Solution5(self, range_of_solution=1000):
        print("Starting  ", "Solution 5 - Generate only one pair")
        start = time.time()
        solution = []
        hash_table = {}

        # Creating the hash table  -  O(n^2)  - schema: {"9":[ (1,2), (2,1)] , ...]
        for a in range(1, range_of_solution):
            for b in range(1, range_of_solution):
                result = pow(a, 3) + pow(b, 3)
                if result not in hash_table:
                    hash_table[result] = [(a, b)]
                else:
                    hash_table[result].append((a, b))

        # Making a loop of nesting the combination of c,d with hash results
        # for pair in hash_table:
        #     if len(hash_table[pair]) > 1:
        #         for i in range(len(hash_table[pair])):
        #             print(*hash_table[pair][0], *hash_table[pair][i])
        #             print(*hash_table[pair][1], *hash_table[pair][i])
        #             solution.append(1)
        #     else:
        #         print(*hash_table[pair][0], *hash_table[pair][0])
        #         solution.append(1)

        # Hardcoding  the loop with the possible range of results (2)
        for pair in hash_table:  # this for loop is not relevant, since only iterates after the hashtable lookup
            if len(hash_table[pair]) > 1:
                # print(*hash_table[pair][0], *hash_table[pair][0])
                solution.append(1)
                # print(*hash_table[pair][0], *hash_table[pair][1])
                solution.append(1)
                # print(*hash_table[pair][1], *hash_table[pair][1])
                solution.append(1)
                # print(*hash_table[pair][1], *hash_table[pair][0])
                solution.append(1)
            else:
                # print(*hash_table[pair][0], *hash_table[pair][0])
                solution.append(1)

        print("Solution len: ", len(solution))
        print("Algorithm took: ", time.time() - start, " seconds")
        print("*" * 200)

    # 5) Actually, once we have the map of all the (c, d) pairs, we can just use that directly. We don't need to
    # generate the (a, b) pairs. Each (a, b) will already be in the map.
    def Solution6(self, range_of_solution=1000):
        print("Starting  ", "Solution 5 - Generate only one pair")
        start = time.time()
        solution = []
        hash_table = {}

        # Creating the hash table  -  O(n^2)  - schema: {"9":[ (1,2), (2,1)] , ...]
        for a in range(1, range_of_solution):
            for b in range(1, range_of_solution):
                result = pow(a, 3) + pow(b, 3)
                if result not in hash_table:
                    hash_table[result] = [(a, b)]
                else:
                    hash_table[result].append((a, b))

        # Making a loop of nesting the combination of c,d with hash results
        # for pair in hash_table:
        #     if len(hash_table[pair]) > 1:
        #         for i in range(len(hash_table[pair])):
        #             print(*hash_table[pair][0], *hash_table[pair][i])
        #             print(*hash_table[pair][1], *hash_table[pair][i])
        #             solution.append(1)
        #     else:
        #         print(*hash_table[pair][0], *hash_table[pair][0])
        #         solution.append(1)

        # Hardcoding  the loop with the possible range of results (2)
        for pair in hash_table:  # this for loop is not relevant, since only iterates after the hashtable lookup
            if len(hash_table[pair]) > 1:
                # print(*hash_table[pair][0], *hash_table[pair][0])
                solution.append(1)
                # print(*hash_table[pair][0], *hash_table[pair][1])
                solution.append(1)
                # print(*hash_table[pair][1], *hash_table[pair][1])
                solution.append(1)
                # print(*hash_table[pair][1], *hash_table[pair][0])
                solution.append(1)
            else:
                # print(*hash_table[pair][0], *hash_table[pair][0])
                solution.append(1)

        print("Solution len: ", len(solution))
        print("Algorithm took: ", time.time() - start, " seconds")
        print("*" * 200)

    def functionCallFactory(self, rangeValue):
        func_list = [
                      self.Solution1,
                      self.Solution2,
                      self.Solution3,
                      self.Solution4,
                      self.Solution5,
                    ]

        for func in func_list:
            func(rangeValue)

if __name__ == '__main__':
    print("*" * 200)
    PositiveSolutionsToPowerOf3Equation().functionCallFactory(rangeValue=100)

