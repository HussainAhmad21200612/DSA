class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        cnt = [0] * 26
        ans = ""
        
        def isSubsequence():
            nonlocal ans
            matched = 0
            i = 0
            j = 0
            M = len(s)
            N = len(ans)
            while i < M and matched < k:
                if s[i] == ans[j]:
                    j += 1
                if j == N:
                    j = 0
                    matched += 1
                i += 1
            return matched == k
        
        def dfs(len):
            nonlocal ans
            if len(ans) == len:
                return True
            for i in range(25, -1, -1):
                if cnt[i] == 0:
                    continue
                ans += chr(ord('a') + i)
                if isSubsequence() and dfs(len):
                    return True
                ans = ans[:-1]
            return False
        
        for c in s:
            cnt[ord(c) - ord('a')] += 1
        for i in range(len(cnt)):
            cnt[i] //= k
        
        j = 0
        for i in range(len(s)):
            if cnt[ord(s[i]) - ord('a')]:
                s[j] = s[i]
                j += 1
        s = s[:j]
        
        for length in range(7, 0, -1):
            if dfs(length):
                return ans
        return ""
