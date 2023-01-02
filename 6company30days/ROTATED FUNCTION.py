class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        '''F(0)=0*a0+a1*1+....a(n-1)*(n-1)
        F(1)=1*a0+a1*2+....a(n-1)*0
        -->F(1)-F(0)=a0+a1+....a(n-2)-(n-1)*a(n-1)
        -->F(1)-F(0)=a0+a1+....+a(n-2)+a(n-1)-a(n-1)
        -->F(1)=F(0)+Sum(array)-n*a(n-1)
        -->F(2)=F(1)+sum(array)-n*a(n-2)
        '''
        total_sum=sum(nums)
        curr_sum=sum([i*nums[i] for i in range(len(nums))])
        ans=curr_sum
        for i in range(len(nums)-1,-1,-1):
            curr_sum=curr_sum+total_sum-nums[i]*(len(nums))
            ans=max(ans,curr_sum)
        return ans
