class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ll={}
        used={}
        j=0
        s=s.split()
        if len(s)!=len(pattern):
            return False
        for i in pattern:
            if i not in ll:
                ll[i]=s[j]
            else:
                if ll[i]!=s[j]:
                    return False
            if s[j] not in used:
                    used[s[j]]=i
            else:
                if used[s[j]]!=i:
                    return False
            j+=1
        return True
