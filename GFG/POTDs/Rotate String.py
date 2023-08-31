class Solution:
    def StringQuery(self,N,Q,S,Q1,Q2):
        #code here
        ans=[]
        for i in range(Q):
            if Q1[i]==1:
                Q2[i]%=N
                c=S[-Q2[i]::]
                d=S[:-Q2[i]]
                S=c+d
                # print(s)
            elif Q1[i]==2:
                ans.append(S[Q2[i]])
        return ans
