class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        ans=[0]*len(word)
        s=0
        for i in range(len(word)):
            s=s*10+int(word[i])
            if  not s%m:
                ans[i]=1
            s=s%m
        return ans
            
        
