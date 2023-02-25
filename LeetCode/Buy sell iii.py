class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minb1=float('inf')
        minb2=float('inf')
        maxs1=0000000000
        maxs2=0000000000
        for i in range(len(prices)):
            minb1=min(minb1,prices[i])
            maxs1=max(maxs1,prices[i]-minb1)
            minb2=min(minb2,prices[i]-maxs1)
            maxs2=max(maxs2,prices[i]-minb2)
        return maxs2
