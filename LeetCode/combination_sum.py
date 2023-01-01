class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def sol(i,c,tot,candidates,target):
            if tot==target:
                res.append(c.copy())
                return
            if i>=len(candidates) or target<tot:
                return
            c.append(candidates[i])
            sol(i,c,tot+candidates[i],candidates,target)
            c.pop()
            sol(i+1,c,tot,candidates,target)
        sol(0,[],0,candidates,target)
        return res
