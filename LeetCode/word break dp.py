class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False]*(len(s)+1)
        dp[len(s)]=True
        for i in range(len(s)-1,-1,-1):
            for j in wordDict:
                if i+len(j)<=len(s) and j==s[i:i+len(j)]:
                    dp[i]=dp[i+len(j)]
                if dp[i]:
                    break
        return dp[0]
        
