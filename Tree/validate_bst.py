class TreeNode:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None
def validate(root, prev = None):
    if root is None:
        return True
    if not validate(root.left,prev):
        return False
    if prev is not None and root.data <= prev.data:
        return False
    prev = root
    return validate(root.right,prev)

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

if validate(root):
    print("True")
else:
    print("false")
