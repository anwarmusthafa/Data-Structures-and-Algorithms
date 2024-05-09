class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def height_of_tree(node):
    if not node:
        return 0
    max_child_height = 0
    for child in node.children:
        max_child_height = max(max_child_height, height_of_tree(child))
    return 1 + max_child_height

def is_balanced(node):
    if not node:
        return True
    heights = []
    for child in node.children:
        heights.append(height_of_tree(child))
    if not heights:
        return True
    if max(heights) - min(heights) > 1:
        return False
    return all(is_balanced(child) for child in node.children)

root = TreeNode("A")
root.add_child(TreeNode("B"))
root.add_child(TreeNode("C"))
root.children[0].add_child(TreeNode("D"))
root.children[0].add_child(TreeNode("E"))
root.children[1].add_child(TreeNode("F"))
root.children[1].add_child(TreeNode("G"))
root.children[1].children[0].add_child(TreeNode("H"))

print("Height of the tree:", height_of_tree(root))
print("Is the tree balanced?", is_balanced(root))
