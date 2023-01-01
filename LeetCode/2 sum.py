class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dp = {}
        for i, j in enumerate(nums):
            s = target - j
            if s in d:
                 return [dp[s], i]
            d[j] = i
		
		
      
