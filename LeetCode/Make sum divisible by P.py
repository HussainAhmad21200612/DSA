class Solution:
    def minSubarray(self, A, p):
        #find the remainder
        need = sum(A) % p 
        dic = {0:-1}
        n = res = len(A)
        c = 0
        
        for i, val in enumerate(A):
            c = (c+val) % p
            dic[c] = i
            if (c-need) % p in dic:
                res = min(res, i - dic[(c-need)%p])
            
        return res if res != n else -1
