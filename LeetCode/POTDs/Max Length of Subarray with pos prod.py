class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos, neg = 0, 0
        res = 0
        for n in nums:
            if n==0:
                neg, pos = 0, 0
            elif n>0:
                if neg>0: neg, pos = neg+1, pos+1
                else: neg, pos = 0, pos+1
            else:
                if neg>0: pos, neg = neg+1, pos+1
                else: neg, pos = pos+1, 0
            res = max(res,pos)
        return res
