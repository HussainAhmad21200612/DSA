"""
definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""
import sys
class Solution:
    def summ(self,root,ans):
        if root==None:
            return 0
        currsum=root.data+self.summ(root.left,ans)+self.summ(root.right,ans)
        ans[0]=max(ans[0],currsum)
        return currsum
    def findLargestSubtreeSum(self, root : Optional['Node']) -> int:
        # code here
        if root==None:
            return 0
        ans=[-sys.maxsize-1]
        self.summ(root,ans)
        return ans[0]

