import bisect 
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        hp=[nums[0]]
        for i in range(1,len(nums)):
            ind=bisect.bisect_left(hp,nums[i])
            if ind==len(hp):
                hp.append(nums[i])
            else:
                hp[ind]=min(hp[ind],nums[i])
        
        return len(hp)
