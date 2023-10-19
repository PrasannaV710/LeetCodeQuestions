# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversed=[]
        def visit(node):
            if not node:
                return
            visit(node.left)
            traversed.append(node.val)
            visit(node.right)
        visit(root)
        return traversed