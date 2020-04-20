"""
    Heap Tree is a Binary tree with the follow properties:
    1) Complete binary thee, filled except bottom and from left to right
    2) Heap Order - each node is greater than child node A[parent] > A[leaf childs]

    Aplications: text search, text couting words frequency,
                 balancing the tree to heap order can be used at priority queues,
                 jobs scheduling

    Implementations:
    
    We could implement heaps using a linked list like strucutre,
    like we did with binary trees, but in this instasce it is actually 
    easier to implement heaps using arrays
    
    Ex: 
        Root - Array[0]
        Child left1 - Array[1]
        Child rigth1 - Array[2]  
        etc.. filling the arrays layers from left to right
        [16,14,10,8,7]

        methods: insert, get_max_min, delete, sort O(n log n)
        sorting basic idea: test/swap the node values if child < parent

        Acessing:   
                    parent:return i/2
                    child-left: 2i
                    child-rigth: 2i + 1
        
        this math will generate an alternated truncated even or odd 
        for parents. Also the childs left term (2n) make it always even from 0 to infinity
        [0,2,4,6 ...n] and rigth term (2i +1 ) make it always odd [1,3,5,7...n]

        heigth = max-deepth - from root to deepest leaf


        Heapify =  convertion of binary tree to heap
                   To heapify a tree we need that property 2 are follow,
                   so we need to reorder the tree. We do the inverse acess process,
                   from last inserted leaf to root, testing for parent > leaf and promoting 
                   until reaching the root 


        Priority queue(aplication) = queue that dynamicaly organizes the items by large key size(the priority)
        ex: [6,6,6,6,5,5,4,3]
        add key 7
        ex: [7, 6,6,6,6,5,5,4,3]
        add key 2
        ex: [7, 6,6,6,6,5,5,4,3,2]
        remove/pop highest priority
        ex: [6,6,6,6,5,5,4,3,2]


        references: https://www.slideshare.net/pratmash/heaps
"""