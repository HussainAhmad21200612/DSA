class Solution{
public:
    int recur(int i,int j,vector<vector<int>>& matrix,vector<vector<int>>& dp){
        if(j<0 || j>=matrix[0].size())
        {
            return -1000000000;
        }
        if(i==0){
            return matrix[0][j];
        }
        if(dp[i][j]!=-1){
            return dp[i][j];
        }
        int su=matrix[i][j]+recur(i-1,j,matrix,dp);
        int sl=matrix[i][j]+recur(i-1,j-1,matrix,dp);
        int sr=matrix[i][j]+recur(i-1,j+1,matrix,dp);
        dp[i][j]=max(su,max(sl,sr));
        return dp[i][j];
    }
    int maximumPath(int N, vector<vector<int>> Matrix)
    {
        // code here
            int m=Matrix[0].size();
        vector<vector<int>> dp(N,vector<int>(m,-1));
        int max_sum=INT_MIN;
        for(int j=0;j<m;j++){
            max_sum=max(recur(N-1,j,Matrix,dp),max_sum);
        }
        return max_sum;
    }
};
