class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        s=1
        maxp=nums[0]
        for i in range(0,len(nums)):
            s*=nums[i]
            maxp=max(maxp,s)
            if s==0:
                s=1
        s=1
        for i in range(len(nums)-1,-1,-1):
            s*=nums[i]
            maxp=max(maxp,s)
            if s==0:
                s=1
        return maxp
