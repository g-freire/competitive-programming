def binaryTree(array, x):
    a = 0
    b = len(array) - 1;
    while (a <= b):
        k = (a+b) // 2
        if (array[k] == x):
            print('found at', k)
        if (array[k] > x) :
            b = k-1;
        else:
            a = k+1;
    return



# Python program to find union of
# two sorted arrays
# Function prints union of arr1[] and arr2[]
# m is the number of elements in arr1[]
# n is the number of elements in arr2[]
def printUnion(arr1, arr2, m, n):
    i, j = 0, 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            print(arr1[i])
            i += 1
        elif arr2[j] < arr1[i]:
            print(arr2[j])
            j += 1
        else:
            print(arr2[j])
            j += 1
            i += 1

    # Print remaining elements of the larger array
    while i < m:
        print(arr1[i])
        i += 1

    while j < n:
        print(arr2[j])
        j += 1

if __name__ == '__main__':
    # Driver program to test above function
    arr1 = [1, 2, 4, 5, 6]
    arr2 = [2, 3, 5, 7]
    m = len(arr1)
    n = len(arr2)
    printUnion(arr1, arr2, m, n)

    # This code is contributed by Pratik Chhajer