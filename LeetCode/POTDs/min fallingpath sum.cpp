class Solution {
public:
    int recur(int i,int j,vector<vector<int>>& matrix,vector<vector<int>>& dp){
        if(j<0 || j>=matrix[0].size())
        {
            return 10000000;
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
        dp[i][j]=min(su,min(sl,sr));
        return dp[i][j];
    }
    int minFallingPathSum(vector<vector<int>>& matrix) {
        int n=matrix.size(),m=matrix[0].size();
        vector<vector<int>> dp(n,vector<int>(m,-1));
        int min_sum=INT_MAX;
        for(int j=0;j<m;j++){
            min_sum=min(recur(n-1,j,matrix,dp),min_sum);
        }
        return min_sum;
    }
};
