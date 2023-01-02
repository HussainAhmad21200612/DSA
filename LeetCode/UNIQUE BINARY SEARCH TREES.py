class Solution:
    def numTrees(self, n: int) -> int:
        dp={0:1,1:1}
        def answer(n,dp):
            if n<=1:
                return 1
            if n in dp:
                return dp[n]
            ans=0
            for i in range(1,n+1):
                ans+=answer(i-1,dp)*answer(n-i,dp)
            dp[n]=ans
            return dp[n]
        return answer(n,dp)
         
