class Solution:
    def permutation(self,s):
        ans=[]
        def permute(a,l,r):
            if l == r:
                ans.append("".join(a))
            else:
                for i in range(l, r):
                    a[l], a[i] = a[i], a[l]
                    permute(a, l+1, r)
                    a[l], a[i] = a[i], a[l]  # backtrack
        permute(list(s),0,len(s))
        ans.sort()
        return ans 
