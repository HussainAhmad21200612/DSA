class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=prices[0]
        pr=0
        for i in range(1,len(prices)):
            c=prices[i]-mini
            pr=max(pr,c)
            mini=min(prices[i],mini)
        return pr
