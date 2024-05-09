class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def height_of_tree(root):
    if not root:
        return 0
    left_height = height_of_tree(root.left)
    right_height = height_of_tree(root.right)
    return max(left_height, right_height) + 1

# Sample usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)

print("Height of the tree:", height_of_tree(root))
