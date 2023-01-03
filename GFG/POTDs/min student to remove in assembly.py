from bisect import bisect_left
class Solution:
    def removeStudents(self, H, N):
        # code here
        dp=[H[0]]
        for i in range(1,N):
            ind=bisect_left(dp,H[i])
            if ind==len(dp):
                dp.append(H[i])
            else:
                dp[ind]=min(dp[ind],H[i])
        return N-len(dp)
