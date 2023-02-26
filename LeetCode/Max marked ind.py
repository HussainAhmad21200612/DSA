class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        ans=0
        j=len(nums)-1
        nums.sort()
        for i in range(len(nums)//2-1,-1,-1):
            if nums[i]*2<=nums[j]:
                ans+=2
                j-=1
        return ans


        
                    
                
        
                    
        
