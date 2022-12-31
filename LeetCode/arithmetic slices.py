class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums)<3:
            return 0
        ap=[0]*(len(nums))
        for i in range(2,len(nums)):
            if nums[i]-nums[i-1]==nums[i-1]-nums[i-2]:
                ap[i]=ap[i-1]+1
        return sum(ap)
