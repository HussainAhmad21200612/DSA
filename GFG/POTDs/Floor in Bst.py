class Solution:
    def floor(self, root, x):
        # code here
            def inor(r):
                if r==None:
                    return ans
                
                inor(r.left)
                ans.append(r.data)
                inor(r.right)
            ans=[]
            inor(root)
            for i in ans[::-1]:
                if i<=x:
                    return i
            return -1
