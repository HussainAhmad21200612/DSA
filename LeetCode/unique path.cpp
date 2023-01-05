class Solution {
public:
int sol(int i,int j,vector<vector<int>>&  dp){
    if (i==0 && j==0){
        return 1;
    }
    if (i<0 || j<0){
        return 0;
    }
    if(dp[i][j]!=-1){
        return dp[i][j];
    }
    int p1=sol(i-1,j,dp);
    int p2=sol(i,j-1,dp);
    return dp[i][j]=p1+p2;
}
    int uniquePaths(int m, int n) {
        vector<vector<int>>dp(m,vector<int>(n,-1));
        return sol(m-1,n-1,dp);
    }
};
