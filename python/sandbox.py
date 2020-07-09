
# LINKED LIST

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None

        if nodes is not None:
            node = Node(data=nodes.pop(0)) # removes from initial index to be head
            self.head = node

            for data in nodes:
                node.next = Node(data=data)
                node = node.next
    
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


if __name__ == '__main__':
    llist = LinkedList(["a", "b", "c", "d", "e"])
    print(llist)
