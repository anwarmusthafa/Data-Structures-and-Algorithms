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
    def delete_middle(self):
        n = len(self.queue) // 2
        arr = []
        for i in range(n):
            arr.append(self.dequeue())
        self.dequeue()
        for i in range(len(self.queue)):
            arr.append(self.dequeue())
        return arr
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q.delete_middle())
q.display()