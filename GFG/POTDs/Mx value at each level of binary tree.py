
class Solution:
    def maximumValue(self,node):
        # code here
        dp={}
        def preorder(node,level,dp):
            if node!=None:
                d=node.data
                if level not in dp:
                    dp[level]=d
                else:
                    dp[level]=max(dp[level],d)
                preorder(node.left,level+1,dp)
                preorder(node.right,level+1,dp)
        preorder(node,0,dp)
        ans=[int(dp[i]) for i in range(len(dp))]
        return ans
   
