class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sol=set()
        l=0
        ans=0
        for i in range(len(s)):
            while s[i] in sol:
                sol.remove(s[l])
                l+=1
            sol.add(s[i])
            ans=max(ans,i-l+1)
        return ans
