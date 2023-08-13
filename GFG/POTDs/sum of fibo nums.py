class Solution:
    def fibSum (self,n):
        #code here
        d={0:0,1:1}
        s=1
        for i in range(2,n+1):
            d[i]=(d[i-1]+d[i-2])%(10**9+7)
            s+=d[i]
        return s%(10**9+7)
