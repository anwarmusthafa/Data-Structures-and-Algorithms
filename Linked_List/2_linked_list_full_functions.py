class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
class linked_list():
    def __init__(self) -> None:
        self.head = None
    def insert_at_begining(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def display(self):
        if self.head is None:
            print("linkedlist is empty")
        current = self.head
        while current:
            print(current.data," ->",end=" ")
            current = current.next
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def insert_value(self,data_list):
        for data in data_list:
            self.append(data)
    def get_length(self):
        current = self.head
        count = 0
        while current:
            current = current.next
            count += 1
        print("\n length : ",count)
        return count
    
    def remove_at(self,index):
        if  index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        current = self.head
        while current:
            if count == index - 1:
                current.next = current.next.next
                break
            current = current.next
            count += 1
    def insert_at(self,index,data):
        if index < 0 or index > self.get_length():
            raise Exception("invalid index")
        if index == 0:
            # new_node = Node(data)
            # new_node.next = self.head
            # self.head = new_node
            self.insert_at_begining(data)
        count = 0
        current = self.head
        while current:
            if count == index - 1:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                break
            current = current.next
            count = count + 1


ll = linked_list()
ll.insert_value([1,2,3,4,5,6])
ll.get_length()
ll.insert_at(3,"new node")
ll.insert_at(3,"new node")
ll.display()
ll.get_length() 
