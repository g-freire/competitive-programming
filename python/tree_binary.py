def binaryTree(array, x):
    a = 0
    b = len(array) - 1;
    while (a <= b):
        k = (a+b) // 2 # halting the inmemory structure
        if (array[k] == x):
            print('found at', k)
        if (array[k] > x) :
            b = k-1;
        else:
            a = k+1;
    return