class Solution:
    # def buy_sell(self,ind,buy,prices,n,dp):
        
    #     if ind==n:
    #         return 0
    #     if dp[ind][buy]!=-1:
    #         return dp[ind][buy]
    #     profit=0
    #     if buy:
    #         profit=max(-prices[ind]+self.buy_sell(ind+1,0,prices,n,dp),0+self.buy_sell(ind+1,1,prices,n,dp))
    #     else:
    #         profit=max(prices[ind]+self.buy_sell(ind+1,1,prices,n,dp),0+self.buy_sell(ind+1,0,prices,n,dp))
    #     dp[ind][buy]=profit
    #     return profit
    def maxProfit(self, prices: List[int]) -> int:
        # dp=[[-1]*2]*(len(prices))
        # return self.buy_sell(0,1,prices,len(prices),dp)
        profit=0
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                profit+=(prices[i]-prices[i-1])
        return profit
