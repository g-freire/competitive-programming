###############################################
# LINKED LIST
###############################################
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"{self.data}"

class LinkedList:
    def insert_head(self):
        self.head = None

    def insert_tail(self):
        pass



###############################################
# BINARY SEARCH
###############################################
def binary_search(list_input, target):
    left = 0
    right = len(list_input) + 1
    while left <= right:
        mid = (left + right) // 2
        a  = list_input[mid]
        if list_input[mid] == target:
            return f"Found at {mid}"
        elif list_input[mid] < target:
            left = mid + 1
        elif list_input[mid] > target:
            right = mid - 1


if __name__ == '__main__':
    list_input = [1,3,5,6,7,8,12,15,22,33]
    a = binary_search(list_input, 15)
    print(a)