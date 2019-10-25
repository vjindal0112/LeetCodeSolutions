# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# incomplete

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

    def recurse(self, out, node):
        if(node.left == None):
            out.append(node.val)
            recurse(out,node.right)
            return out

        recurse(out, node.right)
