class Solution {
public:
int sol(int i,int j,vector<vector<int>>&  dp,vector<vector<int>>& og){
    if (i==0 && j==0 && og[i][j]!=1){
        return 1;
    }
    if (i<0 || j<0 || og[i][j]==1){
        return 0;
    }
    if(dp[i][j]!=-1){
        return dp[i][j];
    }
    int p1=sol(i-1,j,dp,og);
    int p2=sol(i,j-1,dp,og);
    return dp[i][j]=p1+p2;
}
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m=obstacleGrid.size();
        int n=obstacleGrid[0].size();
        vector<vector<int>>dp(m,vector<int>(n,-1));
        return sol(m-1,n-1,dp,obstacleGrid);
    }
};
