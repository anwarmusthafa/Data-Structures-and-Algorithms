class Node():
    def __init__(self,data = None,next = None) -> None:
        self.data = data
        self.next = next
class Linkedlist():
    def __init__(self) -> None:
        self.head =None
    def append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print("\n Middle is ",slow.data)
    def display(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
ll = Linkedlist()
ll.append(5)
ll.append(6)
ll.append(4)
ll.append(10)
ll.append(3)
ll.append(1)
ll.append(7)
ll.display()
ll.middle()

             
