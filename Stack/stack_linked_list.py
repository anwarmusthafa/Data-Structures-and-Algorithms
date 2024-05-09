class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        else:
            popped = self.top.data
            self.top = self.top.next
            return popped

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from an empty stack")
        else:
            return self.top.data

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            current = self.top
            print("Stack elements:")
            while current:
                print(current.data)
                current = current.next

stack = Stack()
stack.push(10)
stack.push(15)
stack.display()