class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        candidates=[1,2,3,4,5,6,7,8,9]
        def sol(i,c,k,candidates,target):
            if target==0 and k==0:
                res.append(c.copy())
                return
            if k<0 or target<0 or i==9:
                return
            c.append(candidates[i])
            sol(i+1,c,k-1,candidates,target-candidates[i])
            c.pop()
            sol(i+1,c,k,candidates,target)
        sol(0,[],k,candidates,n)
        return res
