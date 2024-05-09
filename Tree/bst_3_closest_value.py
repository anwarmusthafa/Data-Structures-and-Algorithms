class BST:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BST(data)
    
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements
    
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
    
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
    
    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right =  self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self
    
    def find_closest_value(self, target):
        closest = 1000
        current = self 
        while current:
            if abs(current.data - target) < abs(closest - target):
                closest = current.data
            if target < current.data:
                current = current.left
            elif target > current.data:
                current = current.right
            else:
                break  
        return closest


def build_tree(elements):
    root = BST(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

elements = [5, 6, 2, 5, 2, 87, 5, 3, 5, 0, 5]
tree = build_tree(elements)
print("In-order traversal:", tree.in_order_traversal())

target = 0
closest_value = tree.find_closest_value(target)
print(f"The closest value to {target} in the tree is {closest_value}")
