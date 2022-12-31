
class Solution
{
    int solution(int a,int b,vector<vector<int>> &dp){
        if(a==0 && b==0){
            return 1;
        }
        if (a<0 || b<0){
            return 0;
        }
        if (dp[a][b] !=-1){
            return dp[a][b];
        }
        
        return dp[a][b]=solution(a-1,b,dp)+solution(a,b-1,dp);
    }
    public:
    //Function to find total number of unique paths.
    int NumberOfPath(int a, int b)
    {
        //code here
        vector<vector<int>>dp(a,vector<int>(b,-1));
        return solution(a-1,b-1,dp);
    }
};
