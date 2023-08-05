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
#Another way to do same task using HAsh
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        a={}
        b={}
        for i in secret:            #Frequency of digits in secret
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        for i in guess:             #Frequency of digits in guess
            if i in b:
                b[i]+=1
            else:
                b[i]=1
        bulls=0
        for i in range(len(secret)):    #Counting bulls
            if secret[i]==guess[i]:
                bulls+=1
                a[secret[i]]-=1
                b[secret[i]]-=1
        cows=0
        for i in a:                     #Counting cows
            if i in b:
                cows+=min(a[i],b[i])
        res=str(bulls)+"A"+str(cows)+"B"
        return res
