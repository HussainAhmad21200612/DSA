class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp=[[1]]
        if rowIndex==0:
            return dp[0]
        for i in range(rowIndex+1):
            r=[0]+dp[-1]+[0]
            t=[]
            for j in range(len(r)-1):
                t.append(r[j]+r[j+1])
            dp.append(t)
        return dp[rowIndex]
