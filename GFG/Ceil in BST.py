class Solution:
    def findCeil(self,root, inp):
        # code here
            def inor(r):
                if r==None:
                    return ans
                
                inor(r.left)
                ans.append(r.key)
                inor(r.right)
            ans=[]
            inor(root)
            for i in ans:
                if i>=inp:
                    return i
            return -1
