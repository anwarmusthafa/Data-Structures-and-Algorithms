class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
    def display(self):
        space = " " * self.get_level() * 3
        prefix = space + "|--"
        print(prefix ,self.data)
        if self.children:
            for child in self.children:
                child.display()
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level+= 1
            p = p.parent
        return level

root = TreeNode("Electronics")
laptop = TreeNode('Laptop')
laptop.add_child(TreeNode("Mac"))
laptop.add_child(TreeNode("Surface"))
laptop.add_child(TreeNode("Thinkpad"))
cellphone = TreeNode("Cell Phone")
cellphone.add_child(TreeNode("iPhone"))
cellphone.add_child(TreeNode("Google Pixel"))
cellphone.add_child(TreeNode("Vivo"))
tv = TreeNode("TV")
tv.add_child(TreeNode("Samsung"))
tv.add_child(TreeNode("LG"))
root.add_child(laptop)
root.add_child(cellphone)
root.add_child(tv)
root.display()

