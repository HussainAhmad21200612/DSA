from bisect import bisect_left
class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        # code here
        dp=[a[0]]
        for i in range(1,n):
            ind=bisect_left(dp,a[i])
            if ind==len(dp):
                dp.append(a[i])
            else:
                dp[ind]=min(dp[ind],a[i])
        return len(dp)
