class Solution:
    def minOperations(self, s: str) -> int:
        A = B = 0
        for i in range(len(s)):
            A += (i&1) ^ (s[i] == '1')
            B += (i&1) ^ (s[i] == '0')
        return min(A, B)  
