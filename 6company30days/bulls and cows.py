class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        b,c=0,0
        s={}
        g={}
        for i in range(len(guess)):
            if guess[i]==secret[i]:
                b+=1
            else:
                if secret[i] in s:
                    s[secret[i]]+=1
                else:
                    s[secret[i]]=1
                if guess[i] in g:
                    g[guess[i]]+=1
                else:
                    g[guess[i]]=1
        for i,j in s.items():
            if i in g:
                c+=min(j,g[i])
 
        return str(b)+"A"+str(c)+"B"
