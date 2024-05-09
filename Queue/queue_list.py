class Queue:
    def __init__(self):
        self.queue = []
    def is_empty(self):
        return  len(self.queue) == 0
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return None
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return None
    def display(self):
        if not self.is_empty():
            for item in self.queue:
                print(item)
        else:
            print("queue is empty")

q = Queue()
q.enqueue(12)
q.enqueue(10)
q.enqueue(6)
q.dequeue()
q.display()