class Solution:
    # def buy_sell(self,ind,buy,prices,fee,n,dp):
        
    #     if ind==n:
    #         return 0
    #     if dp[ind][buy]!=-1:
    #         return dp[ind][buy]
    #     profit=0
    #     if buy:
    #         profit=max(-prices[ind]-fee+self.buy_sell(ind+1,0,prices,fee,n,dp),0+self.buy_sell(ind+1,1,prices,fee,n,dp))
    #     else:
    #         profit=max(prices[ind]+self.buy_sell(ind+1,1,prices,fee,n,dp),0+self.buy_sell(ind+1,0,prices,fee,n,dp))
    #     dp[ind][buy]=profit
    #     return profit
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp=[[-1]*2]*(len(prices))
        n=len(prices)
        buy=[0,0]
        cur=[0,0]
        
        for i in range(n-1,-1,-1):
            for j in range(2):
                profit=0
                if j:
                    profit=max(-prices[i]-fee+buy[0],0+buy[1])
                else:
                    profit=max(prices[i]+buy[1],0+buy[0])
                cur[j]=profit
            buy=cur
        return buy[1]
    #     profit=0
    #     for i in range(1,len(prices)):
    #         if prices[i]>prices[i-1]:
    #             profit+=(prices[i]-prices[i-1])
    #     return profit
    # def maxProfit(self, prices: List[int], fee: int) -> int:
    #     profit=0
    #     for i in range(1,len(prices)):
    #         if prices[i]>prices[i-1]:
    #             profit+=(prices[i]-prices[i-1]-fee)
    #     return profit
