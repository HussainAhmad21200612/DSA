class Solution:
    def minimumNumberOfDeletions(self,S):
        # code here 
        def lps(str):
            n = len(str)
            
            L = [0] * n
            
            for i in range(n - 1, -1, -1):
                back_up = 0
                for j in range(i, n):
                    if j == i:
                        L[j] = 1
                    elif str[i] == str[j]:
                        temp = L[j]
                        L[j] = back_up + 2
                        back_up = temp
                    else:
                        back_up = L[j]
                        L[j] = max(L[j], L[j - 1])
            
            return L[n - 1]
        n = len(S)
        
        length = lps(S)
        
        return (n - length)
