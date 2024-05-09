class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None
class DLL:
    def __init__(self) -> None:
        self.head = None
    def insert_at_begining(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    def display(self):
        current = self.head
        while current:
            print(current.data, end="-->")
            current = current.next
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current
    def delete(self,value):
        current = self.head
        while current:
            if current.data == value:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                return
            current = current.next
        print("invalid value")
            
            
dll = DLL()
dll.insert_at_begining(10)
dll.insert_at_begining(15)
dll.append(20)
dll.append(25)
dll.delete(25)
dll.display()