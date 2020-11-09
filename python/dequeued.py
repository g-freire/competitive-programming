# A linked list node
class Node :
    def __init__(self, data, left=None, right=None) :
        # set the data in allocated node and return the node
        self.data = data
        self.next = None


class Queue :
    rear = None
    front = None

    # Utility function to remove front element from the queue
    def dequeue(self) :  # delete at the beginning:

        if self.front is None :
            print("Queue Underflow")
            exit(1)

        temp = self.front
        print("Removing...", temp.data)

        # advance front to the next node
        self.front = self.front.next

        # if list becomes empty
        if self.front is None :
            self.rear = None

        # deallocate the memory of removed node and
        # optionally return the removed item
        item = temp.data
        return item

    # Utility function to add an item in the queue
    def enqueue(self, item) :  # insertion at the end:

        # Allocate the node in the heap
        node = Node(item)
        print("Inserting...", item)

        # special case: queue was empty
        if self.front is None :
            # initialize both front and rear
            self.front = node
            self.rear = node
        else :
            # update rear
            self.rear.next = node
            self.rear = node

    # Utility function to return top element in a queue
    def peek(self) :

        # check for empty queue
        if self.front :
            return self.front.data
        else :
            exit(1)

        return -1

    # Utility function to check if the queue is empty or not
    def isEmpty(self) :

        return self.rear is None and self.front is None


if __name__ == '__main__' :

    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)

    print("Front element is", q.peek())

    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()

    if q.isEmpty() :
        print("Queue is empty")
    else :
        print("Queue is not empty")
