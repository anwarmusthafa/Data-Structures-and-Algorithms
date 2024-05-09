class Stack:
    def __init__(self) -> None:
        self.stack = []
    def is_empty(self):
        return len(self.stack) == 0
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return IndexError('Stack is empty')
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty")
    def display(self):
        if not self.is_empty():
            for item in reversed(self.stack):
                print(item)
        else:
            raise IndexError("Stack is empty")

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.display()