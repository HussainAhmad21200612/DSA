class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        c=0
        cols=[]
        for i in range(len(strs[0])):
            s=""
            for j in strs:
                s+=j[i]
            cols.append(s)
        for i in cols:
            if i!="".join(sorted(i)):
                c+=1
        return c
