class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        minb=[float('inf')]*k
        maxs=[0]*(k)
        
        for j in range(len(prices)):
            #USE SOLUTION of buy n sell stock 3 problem for generalisation
            # minb1=min(minb1,prices[i])
            # maxs1=max(maxs1,prices[i]-minb1)
            # minb2=min(minb2,prices[i]-maxs1)
            # maxs2=max(maxs2,prices[i]-minb2)
            for i in range(k):
                if i!=0:
                    minb[i]=min(minb[i],prices[j]-maxs[i-1])
                else:
                    minb[i]=min(minb[i],prices[j])
                maxs[i]=max(maxs[i],prices[j]-minb[i])
        return maxs[k-1]
