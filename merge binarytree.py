class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mergeTrees(t1, t2):
    if not t1 or not t2:
        return t1 or t2
    root = TreeNode(t1.val + t2.val)
    root.left = mergeTrees(t1.left, t2.left)
    root.right = mergeTrees(t1.right, t2.right)
    return root
    
print("--- Setup Tree 1 ---")
val1 = int(input("Enter Root value for Tree 1: "))
left1 = int(input("Enter Left Child value for Tree 1: "))
right1 = int(input("Enter Right Child value for Tree 1: "))
tree1 = TreeNode(val1)
tree1.left = TreeNode(left1)
tree1.right = TreeNode(right1)
print("\n--- Setup Tree 2 ---")
val2 = int(input("Enter Root value for Tree 2: "))
left2 = int(input("Enter Left Child value for Tree 2: "))
right2 = int(input("Enter Right Child value for Tree 2: "))

tree2 = TreeNode(val2)
tree2.left = TreeNode(left2)
tree2.right = TreeNode(right2)

result = mergeTrees(tree1, tree2)

print("\n--- Merged Output ---")
print("Root:", result.val)
print("Left:", result.left.val)
print("Right:", result.right.val)
