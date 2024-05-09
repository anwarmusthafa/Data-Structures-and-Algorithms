class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def is_bst(root, prev=None):
    if root is None:
        return True
    # Check left subtree
    if not is_bst(root.left, prev):
        return False
    # Check current node
    if prev is not None and root.data <= prev.data:
        return False
    prev = root
    # Check right subtree
    return is_bst(root.right, prev)

# Test the function with an example tree
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

if is_bst(root):
    print("The given tree is a Binary Search Tree (BST).")
else:
    print("The given tree is not a Binary Search Tree (BST).")
