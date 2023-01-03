class Solution {
public:
int recur(int i,int j,vector<vector<int>>& triangle,vector<vector<int>>& dp){
    if (i==triangle.size()-1){
        return triangle[i][j];
    }
    if(dp[i][j]!=-1) return dp[i][j];
    int s=triangle[i][j]+recur(i+1,j,triangle,dp);
    int s1=triangle[i][j]+recur(i+1,j+1,triangle,dp);
    return dp[i][j]=min(s,s1);
}
    int minimumTotal(vector<vector<int>>& triangle) {
    vector<vector<int>>dp(triangle.size(),vector<int>(triangle[triangle.size()-1].size(),-1));
        return recur(0,0,triangle,dp);
    }
};
