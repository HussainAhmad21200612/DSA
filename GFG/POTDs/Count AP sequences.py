class Solution:
    def count(self,n,a):
        # code here
        MAX=2**10
        minarr = +2147483647
        maxarr = -2147483648
        for i in range(n):
            minarr = min(minarr, a[i])
            maxarr = max(maxarr, a[i]) 
        dp = [0 for i in range(n + 1)]
        ans = n + 1
        for d in range((minarr - maxarr), (maxarr - minarr) + 1):
            sum = [0 for i in range(MAX + 1)]
            for i in range(n):
                dp[i] = 1
                if (a[i] - d >= 1 and a[i] - d <= 1000000):
                    dp[i] += sum[a[i] - d]
     
                ans += dp[i] - 1
                sum[a[i]] += dp[i]
     
        return ans
