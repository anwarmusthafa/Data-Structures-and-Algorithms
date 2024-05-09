class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            dequeued_item = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return dequeued_item

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.front.data

    def display(self):
        current = self.front
        if self.is_empty():
            print("Queue is empty")
            return
        while current is not None:
            print(current.data)
            current = current.next

# Test the implementation
q = Queue()
q.enqueue(12)
q.enqueue(10)
q.enqueue(6)
q.dequeue()  # Removing the first item (12)
q.display()  # Displaying the remaining items
