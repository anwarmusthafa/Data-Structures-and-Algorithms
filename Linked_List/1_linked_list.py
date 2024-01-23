class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print("Middle element:", slow.data)

# Example usage:
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.insert_at_front(3)
linked_list.append(4)
linked_list.insert_at_front(4)
linked_list.display()
linked_list.find_middle()




# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# class Linkedlist:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#     def append(self, Node):
#         if not self.head:
#             self.head = Node
#             self.tail = Node
#         else:
#             self.tail.next = Node
#             self.tail = Node
#     def insertAtFront(self,Node):
#         Node.next = self.head
#         self.head = Node
    
#     def print(self):
#         current = self.head
#         while current:
#             print(current.data)
#             current = current.next
    
# li = Linkedlist()
# li.append(Node(1))
# li.append(Node(2))
# li.insertAtFront(Node(3))
# li.append(Node(4))
# li.print()
