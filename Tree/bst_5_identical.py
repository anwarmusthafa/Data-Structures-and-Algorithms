class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def is_identical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.val != root2.val:
        return False
    return is_identical(root1.left, root2.left) and is_identical(root1.right, root2.right)

root1 = TreeNode(5)
root1.left = TreeNode(3)
root1.right = TreeNode(8)
root1.left.left = TreeNode(2)
root1.left.right = TreeNode(4)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(9)

root2 = TreeNode(5)
root2.left = TreeNode(3)
root2.right = TreeNode(8)
root2.left.left = TreeNode(2)
root2.left.right = TreeNode(4)
root2.right.left = TreeNode(6)
root2.right.right = TreeNode(9)

if is_identical(root1, root2):
    print("BSTs are identical")
else:
    print("BSTs are not identical")
