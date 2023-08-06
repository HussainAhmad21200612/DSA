class Solution:
    def numMusicPlaylists(self, n, goal, k):
        self.n = n
        self.k = k
        
        self.dp = [[-1] * (n + 1) for _ in range(goal + 1)]
        return self.playlists(goal, n)
    
    def playlists(self, i, j):
        if i == 0:
            return int(j == 0)
        if j == 0:
            return 0
        if self.dp[i][j] >= 0:
            return self.dp[i][j]
        self.dp[i][j] = self.playlists(i - 1, j - 1) * (self.n - (j - 1))
        self.dp[i][j] += self.playlists(i - 1, j) * max(0, j - self.k)
        return self.dp[i][j] % (10**9+7)
