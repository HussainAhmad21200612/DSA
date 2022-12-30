# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        left=root.left==None or root.val==root.left.val and self.isUnivalTree(root.left)
        right=root.right==None or root.val==root.right.val and self.isUnivalTree(root.right)
        return left and right
