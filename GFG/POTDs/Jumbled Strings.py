class Solution:
	def TotalWays(self, S1):
		# Code here
		S2="GEEKS"
        m = len(S1)
        n = len(S2)
        count = [0] * n
        for i in range(m): # Traversing the string a
            for j in range(n-1, -1, -1): # Reverse traversal of b
                if S1[i] == S2[j]:
                    count[j] += count[j-1] if j != 0 else 1
        return count[n-1]%(10**9+7)
