# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# incomplete

class Solution:
    def recurse(self, out, node):
        print(out)
        if(node.left is None and node.right is None):
            out.append(node.val)
            return out
        elif(node.left is None):
            out.append(node.val)
            if(node.right is not None):
                self.recurse(out,node.right)
        self.recurse(out, node.left)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.recurse([], root)
