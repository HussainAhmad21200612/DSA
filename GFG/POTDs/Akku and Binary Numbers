from bisect import bisect_right,bisect_left
class Solution:
    global ll
    ll=[]
    def solve (self, L, R):
        return bisect_right(ll,R)-bisect_left(ll,L)
    def precompute (self):
        c=0
        for i in range(63):
            for j in range(i+1,63):
                for k in range(j+1,63):
                    number=pow(2,i)+pow(2,j)+pow(2,k)
                    ll.append(number)
                  
        ll.sort()
        
