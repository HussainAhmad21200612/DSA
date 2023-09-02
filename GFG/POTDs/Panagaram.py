#User function Template for python3
class Solution:
    def isPanagram(self, S):
        # code here
        l={}
        c=0
        for i in S:
            i=i.lower()
            if l.get(i,-1)==-1:
                if 'a'<=i<='z':
                    c+=1
            l[i]=1
#         print(l)
        return int(c==26)
