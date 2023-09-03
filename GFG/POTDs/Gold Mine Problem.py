class Solution:
    def maxGold(self, n, m, M):
        # code here
        def collectGold(gold, x, y, n, m, dp):
         
            # Base condition.
            if ((x < 0) or (x == n) or (y == m)):
                return 0
         
            if(dp[x][y] != -1):
                return dp[x][y]
            rightUpperDiagonal = collectGold(gold, x - 1, y + 1, n, m, dp)
            right = collectGold(gold, x, y + 1, n, m, dp)
            rightLowerDiagonal = collectGold(gold, x + 1, y + 1, n, m, dp)
            dp[x][y] = gold[x][y] + max(max(rightUpperDiagonal, rightLowerDiagonal), right)
            return dp[x][y]
          
         
        def getMaxGold(gold,n,m):
         
            maxG = 0
            dp = [[-1 for i in range(m)]for j in range(n)]
             
            for i in range(n):
                goldCollected = collectGold(gold, i, 0, n, m, dp) 
                maxG = max(maxG, goldCollected)
         
            return maxG
        return getMaxGold(M,n,m)
