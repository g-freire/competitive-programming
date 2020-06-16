from collections import deque


# Data structure to store a Binary Tree node
class Node:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


# Recursive function to insert a key into BST
def insert(root, key):

    # if the root is None, create a node and return it
    if root is None:
        return Node(key)

    # if given key is less than the root node, recur for left subtree
    if key < root.key:
        root.left = insert(root.left, key)

    # if given key is more than the root node, recur for right subtree
    else:
        root.right = insert(root.right, key)

    return root


# Helper function to perform level order traversal of binary tree
def printLevelOrderTraversal(root):

    # base case: empty tree
    if root is None:
        return

    q = deque()
    q.append(root)

    while q:

        n = len(q)
        for _ in range(n):
            front = q.popleft()
            print(front.key, end=' ')

            if front.left:
                q.append(front.left)

            if front.right:
                q.append(front.right)

        print()


# Function to perform inorder traversal of a binary tree and
# push all nodes in a queue (in encountered order)
def inorder(root, keys):

    if root is None:
        return

    inorder(root.left, keys)
    keys.append(root.key)
    inorder(root.right, keys)


# Function to perform preorder traversal of the binary tree
# Assign each encountered node with next key from the queue
def preorder(root, keys):

    # base case: empty tree
    if root is None:
        return

    # replace root's key value with next key from the queue
    root.key = keys.popleft()

    # process left subtree
    preorder(root.left, keys)

    # process right subtree
    preorder(root.right, keys)


# Function to convert a BST to a min heap
def convert(root):

    # maintain a queue to store inorder traversal of the tree
    keys = deque()

    # fill the queue in inorder fashion
    inorder(root, keys)

    # traverse tree in preorder fashion and for each encountered node,
    # dequeue a key from the queue and assign it to the node
    preorder(root, keys)


if __name__ == '__main__':

    root = None

    """ Construct below bst
               5
             /   \
            /     \
           3       8
          / \     / \
         /   \   /   \
        2     4 6    10
    """

    keys = [5, 3, 2, 4, 8, 6, 10]
    for key in keys:
        root = insert(root, key)

    convert(root)
    printLevelOrderTraversal(root)
