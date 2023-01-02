class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        c=0
        for i in word:
            if i>='A' and i<='Z':
                c+=1
        if c==len(word) or (c==1 and word[0]>='A' and word[0]<="Z") or c==0:
            return True
        else:
            return False
